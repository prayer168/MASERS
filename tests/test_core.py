import json
import subprocess
import sys
import tempfile
import unittest
from dataclasses import asdict
from pathlib import Path
from masers.models import Task, Handoff
from masers.state import Store
from masers.providers import MockProvider
from masers.agents import RoleAgent
from masers.orchestrator import Orchestrator

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.store = Store(self.tmp.name)
        self.engine = Orchestrator(self.store)

    def test_task_validation(self):
        with self.assertRaises(ValueError):
            Task("", "description", ["r"], ["a"])
        with self.assertRaises(ValueError):
            Task("t", "d", ["r"], ["a"], budget=0)

    def test_transition(self):
        tid = self.engine.create("Todo")
        state = self.store.read("state", tid)
        with self.assertRaises(ValueError):
            self.store.transition(state, "completed")
        self.store.transition(state, "running")
        self.store.transition(state, "failed")
        self.store.transition(state, "running")

    def test_handoff(self):
        handoff = Handoff("builder", "TASK-1", "summary", ["done"])
        self.store.write("handoffs", "TASK-1", handoff.to_dict())
        self.assertEqual(self.store.read("handoffs", "TASK-1")["summary"], "summary")

    def test_path_safety(self):
        with self.assertRaises(ValueError):
            self.store.read("state", "../outside")

    def test_mock_agent(self):
        task = Task("t", "d", ["r"], ["a"])
        handoff, response = RoleAgent("builder", MockProvider()).run(task, {"title": "Todo"})
        self.assertEqual(handoff.agent, "builder")
        self.assertGreater(response.tokens_out, 0)

    def test_integration_and_resume_idempotence(self):
        tid = self.engine.create("Todo CLI")
        state = self.engine.run(tid)
        self.assertEqual(state["status"], "completed")
        self.assertEqual(state["step"], 6)
        self.assertEqual(state["test_status"], "simulated")
        self.assertEqual(self.engine.run(tid)["token_usage"], state["token_usage"])
        self.assertEqual(len(list((self.store.root / "handoffs").glob("*.json"))), 6)

    def test_failure_recovery(self):
        class Broken(MockProvider):
            def generate(self, role, context):
                raise TimeoutError("API timeout")
        tid = self.engine.create("Todo")
        failed = Orchestrator(self.store, Broken()).run(tid)
        self.assertEqual(failed["status"], "failed")
        self.assertEqual(failed["attempts"]["0"], 3)
        self.assertEqual(self.engine.run(tid)["status"], "completed")

    def test_budget_gate(self):
        tid = self.engine.create("Todo")
        task = self.store.read("tasks", tid)
        task["budget"] = 1
        self.store.write("tasks", tid, task)
        state = self.engine.run(tid)
        self.assertEqual(state["status"], "failed")
        self.assertEqual(state["token_usage"], 0)

    def test_optional_routing(self):
        tid = self.engine.create("Small change")
        task = self.store.read("tasks", tid)
        task["review_required"] = False
        self.store.write("tasks", tid, task)
        self.assertEqual(self.engine.run(tid)["step"], 4)

    def test_dependency_gate(self):
        dep = self.engine.create("Dependency")
        tid = self.engine.create("Dependent")
        task = self.store.read("tasks", tid)
        task["dependencies"] = [dep]
        self.store.write("tasks", tid, task)
        with self.assertRaises(ValueError):
            self.engine.run(tid)

    def test_cli_end_to_end(self):
        result = subprocess.run([sys.executable, "-m", "masers", "--root", self.tmp.name,
                                 "run", "Build Todo CLI"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "completed")
        for command in ("status", "tasks", "budget", "models", "logs"):
            result = subprocess.run([sys.executable, "-m", "masers", "--root", self.tmp.name, command],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            json.loads(result.stdout)

if __name__ == "__main__":
    unittest.main()
