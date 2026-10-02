# 拍攝鏡頭清單

建議成片 3–5 分鐘，16:9，1080p，30 fps。每段先錄原始畫面，再剪接；截圖只用於補足沒有錄影的既有事件，字幕標示「使用者提供畫面／歷史截圖」。

| 鏡頭 | 畫面 | 素材／動作 | 旁白重點 |
|---|---|---|---|
| 1 開場 | 專案資料夾與標題卡 MASERS | 重新錄製；README | 多模型協作靠結構化狀態與可追蹤成果 |
| 2 起點 | Git 狀態、空的初始 repo，再切到架構樹 | `evidence/git-history.txt` 與 source tree；空 repo 畫面需用 Git history 誠實重演 | 先檢查 Starter；這個工作區起始時沒有程式碼 |
| 3 Phase 1 | 顯示 Task、State、Handoff、Provider、Orchestrator 檔案 | 原始程式碼；commit `7e04e11` | 核心拆成小模組，Mock 可以離線跑 |
| 4 安裝錯誤 | 插入 screenshot 01，再現終端情境 | `evidence/screenshots/01-package-not-installed.png` | Python 從家目錄找不到尚未安裝的 package |
| 5 修復 | 顯示 editable install 指令、README diff/commit | commit `cbadfa1`；重錄安裝指令輸出 | 安裝到目前使用的 Python 後，跨目錄可執行 |
| 6 Pipeline | 插入 screenshot 02；接著重跑 demo，切換 state/handoff 檔 | `evidence/screenshots/02-mock-pipeline-complete.png` 和 `evidence/runs/` | 六階段依序輸出交接與狀態 |
| 7 驗證 | 即時重跑 unittest，展示摘要；CLI status/logs | 必須從錄影現場即時取得輸出，不要做成歷史逐字稿 | 11 項既有測試曾通過；畫面中的本次測試要以新的執行為準 |
| 8 誠實界線 | `mode: mock`, `review_status: simulated`, `test_status: simulated` 放大 | State JSON | Mock 證明 orchestration 協定可走通，不代表 Todo 已寫好或真實測試成功 |
| 9 Git 與去向 | 展示 `git log`, `git status`, GitHub repository 查詢結果 | Git evidence；重新拍 GitHub 最新查詢 | 三個本地 checkpoints；遠端 MASERS repo 尚未確認 |
| 10 收尾 | Phase 2 roadmap 和素材清冊 | README、manifest | 下一步是 Provider adapters；影片素材有來源、雜湊與版本紀錄 |

## 避免誤導的剪輯規則

1. 歷史截圖明確標註「使用者提供的截圖」，不要配音說成我們正在即時錄製。
2. 不把 `simulated` 改字幕為 passed。
3. 不用 mock JSON 畫面暗示模型真的產生了 Todo 原始碼。
4. 過往沒有原始 transcript 的步驟，不補造 shell 逐字稿；重拍時即時重跑。
5. 上傳前確認 GitHub repo URL、可見度和 credential 畫面，避免曝光金鑰。
