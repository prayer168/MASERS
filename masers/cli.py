import argparse
import json
from pathlib import Path
from .state import Store
from .orchestrator import Orchestrator
from .agents import ROLES

def main(argv=None):
    parser = argparse.ArgumentParser(description="MASERS Phase 1 — mock pipeline")
    parser.add_argument("--root", default=".masers")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    run = sub.add_parser("run")
    run.add_argument("description")
    resume = sub.add_parser("resume")
    resume.add_argument("task_id")
    for command in ("status", "tasks", "logs", "budget", "models"):
        sub.add_parser(command)
    review = sub.add_parser("review")
    review.add_argument("task_id")
    args = parser.parse_args(argv)
    store = Store(Path(args.root).resolve())
    engine = Orchestrator(store)
    if args.command == "init":
        output = {"root": str(store.root), "mode": "mock", "roles": ROLES}
    elif args.command in ("run", "resume"):
        task_id = engine.create(args.description) if args.command == "run" else args.task_id
        output = engine.run(task_id)
    elif args.command == "models":
        output = {"available": ["mock"], "live_providers": "Phase 2 pending"}
    elif args.command == "logs":
        path = store.root / "logs" / "events.jsonl"
        output = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()] if path.exists() else []
    elif args.command == "review":
        from .state import safe_id
        safe_id(args.task_id)
        output = [json.loads(p.read_text(encoding="utf-8")) for p in (store.root / "handoffs").glob(args.task_id + "-*.json")]
    else:
        directory = "tasks" if args.command == "tasks" else "state"
        output = [json.loads(p.read_text(encoding="utf-8")) for p in (store.root / directory).glob("*.json")]
        if args.command == "budget":
            output = [{"task_id": s["task_id"], "token_usage": s["token_usage"],
                       "budget": store.read("tasks", s["task_id"])["budget"]} for s in output]
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 1 if isinstance(output, dict) and output.get("status") == "failed" else 0

if __name__ == "__main__":
    raise SystemExit(main())
