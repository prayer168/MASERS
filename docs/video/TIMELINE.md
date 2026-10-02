# 建置時間線與畫面順序

日期皆為 2026-10-02，台北時間 UTC+8。時刻依 Git commit 紀錄或畫面內程式時間；截圖沒有可確認的拍攝時間時，只標示流程順序。

| 順序 | 時間／來源 | 建置事件 | 可用素材 | 畫面可說明的事 |
|---|---|---|---|---|
| 1 | 初始檢查，commit 11:45 | 工作區只有空 Git repository，無 Starter 原始碼、README、tests | Git root commit 前後記錄；當時沒有截圖 | 為何先掃描現況 |
| 2 | 11:45 commit `7e04e11` | 建立 Phase 1 Python 套件：Task、State、Handoff、Provider/Agent 介面、Mock orchestrator、CLI、11 項測試 | Git commit、目前 source/tests | 小批次核心架構 |
| 3 | 使用者提供截圖 01 | 從 `C:\Users\NNKIEH` 執行，發生 `No module named masers` | `evidence/screenshots/01-package-not-installed.png` | 套件未安裝時，非專案路徑無法 import |
| 4 | 11:49 commit `cbadfa1` | 執行 editable install，調整 README 安裝步驟及 Python/狀態路徑說明 | Git commit；畫面 02 的後續成功狀態 | 修正啟動方式 |
| 5 | 順序承接畫面 03 | 在專案路徑下執行 Todo prompt，六階段 Mock 流程完成；test/review 標記 simulated | 使用者截圖 `02-mock-pipeline-complete.png`；Task/State/Handoff/JSONL | 成功的是 pipeline 模擬；沒有建立 Todo CLI 軟體 |
| 6 | 11:57 commit `cc44793` | 增加建置日誌 | Git commit | 開始以文件保存建置軌跡 |
| 7 | 目前歸檔 | 複製兩張使用者截圖、3 次 Demo 的 Task/State、18 份 Handoff、JSONL events，產生 SHA-256 清冊 | `evidence/`、`ASSET_MANIFEST.json` | 證據來源和完整性如何管理 |
| 8 | 本次處理 | 使用者要求公開 repo，確認後從 private 轉為 public；更新 GitHub Description/Topics | GitHub repo metadata | 程式碼及歷史 commits 現在可供所有人瀏覽 |
| 9 | 本次處理 | 使用者提供執行原則錯誤畫面；移除需載入的錄製腳本，改為直接輸入 transcript 命令 | `evidence/screenshots/03-powershell-script-policy-block.png` | 尊重本機執行原則，以互動式 cmdlet 錄製 |
| 10 | 本次處理 | README 新增 SEO 摘要、關鍵字及 AEO 常見問答 | README / GitHub description and topics | GitHub 儲存庫欄位與 README 正文共同改善可搜尋和可回答性 |

## 數量核對

- Task：3 份；State：3 份。
- Handoff：18 份，三次各六階段。
- 事件 log：由當時的 Mock runs 產生，見 `evidence/runs/events.jsonl`。
- 螢幕截圖：2 張。第一張證明套件匯入失敗；第二張證明使用者看到 pipeline 完成狀態。
- 測試：建置當時 unittest 11 項通過。對話中留有完整 pytest/unittest 命令輸出，但沒有保存當時原始 transcript；旁白可說明既有測試結果，需重新拍攝時應依錄製指南即時重跑，並保存新的 transcript。
