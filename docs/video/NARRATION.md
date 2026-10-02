# 旁白稿（可調整）

## 開場

這是 MASERS，Multi-AI Software Engineering & Review System。它的核心不是把聊天記錄複製給每個 AI，而是讓工作狀態、任務、交接、測試結果和 Git 變更都有結構、有來源、可追蹤。

## 從空白工作區開始

建置前先掃描 repository、README、Agent 指引和測試。檢查結果是：這個工作區當時只有一個尚未提交的 Git repository，沒有 Starter 原始碼或現有測試。因此我們從小型 Phase 1 核心開始，沒有假裝接續不存在的程式。

## Phase 1

Phase 1 建立結構化 Task、持久化 State、Handoff 格式、Agent 和 Provider 介面、Orchestrator 及 CLI。Mock Provider 讓流程離線可執行。Planner、Builder、Reviewer、Builder Revision、Tester 和 Integrator 依序產生六份交接。

## 安裝修正

這張歷史截圖記錄第一次從使用者家目錄呼叫時的錯誤：Python 找不到 MASERS。原因是 repository 尚未安裝到當時選用的 Python。後續執行 editable install，並把完整路徑、安裝方式和狀態資料位置補進 README。

## Pipeline Demo

這裡展示的是 Todo CLI 的 Mock pipeline。每階段有 task ID 和 handoff，最後狀態是 completed；然而 mode、review_status 和 test_status 都清楚標示 mock 或 simulated。它驗證的是 MASERS 的流程與狀態保存，不是 Todo 軟體本身完成。

## 證據和影片記錄

建置紀錄由四類材料組成：Git commit 保留版本，BUILD_LOG 和時間線說明每次里程碑，MASERS 的 JSON/JSONL 保存任務、狀態、交接與事件，截圖保留使用者提供的終端畫面。素材清冊逐檔計算 SHA-256。過去沒有同步錄下的畫面或聲音會明確標成歷史資料；現在開始則可在 PowerShell 開 transcript 並用螢幕錄影軟體同步拍攝。

## 錄製工具錯誤

下一張歷史截圖顯示 PowerShell 阻擋載入未簽署的錄製腳本。這是電腦的執行原則，不是 MASERS 執行錯誤。我移除對 `.ps1` 啟動器的依賴，改成在互動式 PowerShell 逐行執行 `Start-Transcript`；完成後在相同視窗執行 `Stop-Transcript`。沒有要求降低安全原則。

## 收尾

目前已完成可測試的離線核心。Provider adapters、真正的模型執行、程式修改工具和真實測試仍在 roadmap。GitHub 帳戶尚未找到名為 MASERS 的 repository，所以本地提交已版本化，但遠端 push 還沒有發生。
