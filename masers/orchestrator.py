from dataclasses import asdict
from time import monotonic
from .models import Task
from .state import now
from .agents import RoleAgent
from .providers import MockProvider

class Orchestrator:
    def __init__(self, store, provider=None, max_retry=2):
        self.store = store
        self.provider = provider or MockProvider()
        self.max_retry = max_retry

    def create(self, description):
        task = Task(title=description[:100], description=description,
                    requirements=[description], acceptance_criteria=["Mock pipeline completes and saves structured handoffs"])
        self.store.write("tasks", task.task_id, asdict(task))
        state = dict(project_id=self.store.root.parent.name, task_id=task.task_id,
                     current_phase="pending", assigned_agent=None, status="pending",
                     dependencies=task.dependencies, changed_files=[], git_commit=None,
                     test_status="pending", review_status="pending", token_usage=0,
                     cost_estimate=0, last_updated=now(), next_action="planner", step=0,
                     mode="mock", attempts={})
        self.store.write("state", task.task_id, state)
        return task.task_id

    def run(self, task_id):
        task = Task(**self.store.read("tasks", task_id))
        state = self.store.read("state", task_id)
        if state["status"] == "completed":
            return state
        for dependency in task.dependencies:
            if self.store.read("state", dependency)["status"] != "completed":
                raise ValueError("Dependency incomplete")
        self.store.transition(state, "running")
        phases = ["planner", "builder"]
        if task.review_required:
            phases += ["reviewer", "builder"]
        if task.test_required:
            phases += ["tester"]
        phases += ["integrator"]
        try:
            for index in range(state["step"], len(phases)):
                role = phases[index]
                state.update(current_phase=role, assigned_agent=role, next_action=role)
                self.store.write("state", task_id, state)
                context = dict(title=task.title, requirements=task.requirements,
                               acceptance_criteria=task.acceptance_criteria,
                               latest_handoff=self.store.read("handoffs", f"{task_id}-{index-1}") if index else None)
                for attempt in range(self.max_retry + 1):
                    started = monotonic()
                    try:
                        # Conservative preflight for the bounded deterministic mock response.
                        estimate = self.provider.estimate_tokens(__import__("json").dumps(context)) + 2000
                        if state["token_usage"] + estimate > task.budget:
                            raise ValueError("Budget limit: human action required")
                        handoff, response = RoleAgent(role, self.provider).run(task, context)
                        state["token_usage"] += response.tokens_in + response.tokens_out
                        if state["token_usage"] > task.budget:
                            raise ValueError("Budget exhausted")
                        handoff.next_recommended_agent = phases[index+1] if index+1 < len(phases) else None
                        self.store.write("handoffs", f"{task_id}-{index}", handoff.to_dict())
                        state["step"] = index + 1
                        state["review_status"] = "simulated" if role == "reviewer" else state["review_status"]
                        state["test_status"] = "simulated" if role == "tester" else state["test_status"]
                        self.store.write("state", task_id, state)
                        self.store.log(task_id=task_id, agent=role, action="generate", status="success",
                                       duration=monotonic()-started, tokens_in=response.tokens_in, tokens_out=response.tokens_out)
                        break
                    except Exception as error:
                        state["attempts"][str(index)] = state["attempts"].get(str(index), 0) + 1
                        self.store.log(task_id=task_id, agent=role, action="generate", status="failed", error=str(error))
                        if attempt == self.max_retry or "Budget" in str(error):
                            raise
            state.update(next_action="inspect_mock_artifacts", current_phase="final", assigned_agent=None)
            self.store.transition(state, "completed")
        except Exception as error:
            state.update(error=str(error), next_action="resolve_error_then_resume")
            self.store.transition(state, "failed")
        task.status = state["status"]
        self.store.write("tasks", task_id, asdict(task))
        return state
