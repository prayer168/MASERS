# Decisions

## D001 — 單機、標準函式庫 Mock 核心
- Date: 2026-10-02
- Agent: Codex implementation agent
- Context: 工作區只有空 Git repository，沒有 Starter。
- Decision: 先建立小型模組化 Python package，用 JSON 狀態與 deterministic mock 驗證 Phase 1。
- Alternatives: 立即引入資料庫、框架與真實多家 API。
- Reason: 核心流程可離線測試，避免基礎協定未穩定就增加外部依賴。
- Impact: 單程序；不提供真實 code execution 或多程序一致性。

## D002 — 模擬完成與工程驗收分開
- Date: 2026-10-02
- Agent: Codex implementation agent
- Context: Mock 不能證明產出的軟體符合需求。
- Decision: 保存 mode=mock、test_status=simulated、review_status=simulated。
- Alternatives: 將 mock 結果寫成 passed。
- Reason: 避免誤報真實測試通過。
- Impact: Phase 3 前 completed 僅表示 mock pipeline 完成。

## D003 — Phase 2 外部驗證 checkpoint
- Date: 2026-10-02
- Agent: Codex implementation agent
- Context: 沒有提供 API key 或指定可用模型。
- Decision: 不查找本機憑證、不呼叫計費 API；保留 .env.example 與接入計畫。
- Alternatives: 依賴本機既有 credentials。
- Reason: 使用者要求在需要 API key 的地方停止。
- Impact: Phase 2 尚未完成，須在 adapter contract tests 後進行授權的 live smoke test。
