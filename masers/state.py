import json
import os
import re
from pathlib import Path
from datetime import datetime, timezone
from uuid import uuid4

TRANSITIONS = {
    "pending": {"running"},
    "running": {"running", "failed", "completed"},
    "failed": {"running"},
    "completed": set(),
}

def now():
    return datetime.now(timezone.utc).isoformat()

def safe_id(value):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise ValueError("Unsafe identifier")
    return value

class Store:
    """Single-process JSON storage; atomic replacement, not distributed locking."""
    def __init__(self, root):
        self.root = Path(root)
        for directory in ("tasks", "state", "handoffs", "logs", "artifacts", "reviews"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)

    def write(self, directory, name, value):
        path = self.root / directory / (safe_id(name) + ".json")
        temporary = path.with_suffix("." + uuid4().hex + ".tmp")
        try:
            temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)

    def read(self, directory, name):
        return json.loads((self.root / directory / (safe_id(name) + ".json")).read_text(encoding="utf-8"))

    def transition(self, state, status):
        if status not in TRANSITIONS[state["status"]]:
            raise ValueError(f"Invalid transition: {state['status']} -> {status}")
        state.update(status=status, last_updated=now())
        self.write("state", state["task_id"], state)

    def log(self, **event):
        entry = dict(timestamp=now(), project_id=self.root.parent.name, task_id=None,
                     agent=None, model="mock", action=None, duration=0,
                     tokens_in=0, tokens_out=0, status=None, error=None)
        entry.update(event)
        with (self.root / "logs" / "events.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(entry, ensure_ascii=False) + "\n")
