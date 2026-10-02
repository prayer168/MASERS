# MASERS 建置紀錄

此文件以 Git 版本記錄建置過程與每次可驗證成果；CLI 終端輸出與測試結果保存在提交紀錄所對應的執行摘要。

## 2026-10-02 — Phase 1 核心及安裝修正

- 初始檢查：工作區是空的 Git repository，沒有 Starter 原始碼、README、AGENTS 或 tests。
- 建置核心：加入 Task、JSON State、Handoff、Agent/Provider interface、MockProvider、Orchestrator、CLI、錯誤重試和 resume。
- Demo：以 Mock 模式跑六階段 Todo CLI 任務；輸出標記為 simulated，不代表建立 Todo App 或真實 code review/test。
- 驗證：11 項 unittest 通過，包括 CLI E2E、budget gate、失敗恢復和依賴檢查。
- 安裝問題：使用者從家目錄執行時 Python 找不到未安裝的 package。執行 `python -m pip install -e .`，從家目錄使用指定 `--root` 驗證成功；README 補上安裝、Python 環境與狀態路徑說明。
- Git checkpoints：`7e04e11` 初始 Phase 1；`cbadfa1` 安裝文件修正。
- 下一階段：Phase 2 provider adapters 尚待實作；實際服務呼叫需設定 API keys。

## 2026-10-02 — 影片素材封存

- 歸檔兩張使用者提供的 PowerShell 截圖原檔，保留原尺寸。
- 複製三次 Mock Demo 的 Task/State、18 份 Handoff 與 events.jsonl 至 `docs/video/evidence/runs/`。
- 新增 SHA-256 資產清冊、建置時間線、鏡頭清單、旁白稿、證據來源說明與後續錄製指南。
- 提供 PowerShell Start/Stop-Transcript 腳本，從此後的工作階段同步記錄指令和輸出；搭配 OBS 錄螢幕。
- 歷史限制：先前沒有背景螢幕錄影或 PowerShell transcript；未錄到的步驟不補造逐字稿。
- GitHub：本機未設定 remote；登入帳戶清單與同名搜尋均未找到 MASERS repo，push 待 repo URL/目的地確認。
