import json
from abc import ABC, abstractmethod
from .models import Handoff

ROLES = ("orchestrator", "planner", "researcher", "builder", "reviewer", "challenger", "tester", "integrator")

class Agent(ABC):
    @abstractmethod
    def run(self, task, context): ...

class RoleAgent(Agent):
    def __init__(self, role, provider):
        if role not in ROLES:
            raise ValueError("Unknown role")
        self.role, self.provider = role, provider

    def run(self, task, context):
        response = self.provider.generate(self.role, context)
        value = json.loads(response.text)
        if not isinstance(value, dict) or not isinstance(value.get("completed"), list):
            raise ValueError("Invalid structured agent output")
        if not isinstance(value.get("summary"), str) or not value["summary"].strip():
            raise ValueError("Agent summary is required")
        return Handoff(agent=self.role, task_id=task.task_id, **value), response
