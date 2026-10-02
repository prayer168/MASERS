# MASERS Agent contract

Read README.md and DECISIONS.md before editing. Use state, task requirements, artifact references and Git diffs; do not exchange full conversation histories. This version is a mock protocol harness.

| Role | Responsibility | Input | Output | Allowed actions | Forbidden actions | Exit condition |
|---|---|---|---|---|---|---|
| Orchestrator | Route and persist work | Task, dependencies, state | phase/state | choose stages, retry within limits | bypass budgets or acceptance | persisted terminal state |
| Planner | Requirements and design | Task, decisions | plan handoff | propose architecture | silently change requirements | acceptance mapped |
| Researcher | Verify references | scoped questions | sourced findings | read official references | invent evidence | references recorded |
| Builder | Implement approved plan | plan, review, diff | implementation handoff | scoped source edits | destructive Git/deploy | implementation ready for testing |
| Reviewer | Find defects | diff, requirements | Critical/Major/Minor findings | inspect defects and edge cases | empty praise or fabricated findings | findings or documented checked areas |
| Challenger | Challenge assumptions | plan, decisions | alternative and tradeoffs | propose at least one alternative | silently override decisions | comparison recorded |
| Tester | Verify acceptance | code, criteria | structured real test results | approved tests | claim mock tests passed | evidence saved |
| Integrator | Accept/revise/reject | review, tests, criteria, Git diff | integration decision | assess evidence | accept solely on Builder claim | all DoD checks satisfied |

All handoffs include agent, task_id, summary, completed, files_created, files_modified, commands_run, tests, known_issues, risks, decisions, next_recommended_agent and next_action. Save under project handoffs/. Phase 1 outputs are explicitly simulated.

No shell/tool executor exists yet. Before adding one, enforce explicit human approval for mass deletion, destructive Git, production deploy, database migration, credential changes, budget increases, unresolved disagreement, repeated failures and major architecture changes. Do not perform force push, reset --hard or rewrite history during repository maintenance.

Run `python -m unittest discover -s tests -v` after each small batch. Do not introduce distributed infrastructure or claim later phases complete before their acceptance tests pass.
