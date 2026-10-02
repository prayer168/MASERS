from dataclasses import dataclass, field, asdict
from enum import Enum
from uuid import uuid4

class Status(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    FAILED = "failed"
    COMPLETED = "completed"

@dataclass
class Task:
    title: str
    description: str
    requirements: list[str]
    acceptance_criteria: list[str]
    task_id: str = field(default_factory=lambda: "TASK-" + uuid4().hex[:12])
    dependencies: list[str] = field(default_factory=list)
    assigned_role: str = "planner"
    input_artifacts: list[str] = field(default_factory=list)
    expected_output: str = "structured handoffs"
    status: str = "pending"
    priority: int = 1
    budget: int = 20000
    review_required: bool = True
    test_required: bool = True

    def __post_init__(self):
        if not self.title.strip() or not self.description.strip():
            raise ValueError("Task title and description are required")
        if not self.requirements or not self.acceptance_criteria:
            raise ValueError("Requirements and acceptance criteria are required")
        if self.budget <= 0 or self.task_id in self.dependencies:
            raise ValueError("Invalid budget or self dependency")
        if self.status not in {s.value for s in Status}:
            raise ValueError("Invalid task status")

@dataclass
class Handoff:
    agent: str
    task_id: str
    summary: str
    completed: list[str]
    files_created: list[str] = field(default_factory=list)
    files_modified: list[str] = field(default_factory=list)
    commands_run: list[str] = field(default_factory=list)
    tests: dict = field(default_factory=dict)
    known_issues: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    next_recommended_agent: str | None = None
    next_action: str = "continue"

    def __post_init__(self):
        if not self.agent or not self.task_id or not self.summary:
            raise ValueError("Incomplete handoff")

    def to_dict(self):
        return asdict(self)
