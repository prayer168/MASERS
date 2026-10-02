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
