# MASERS 建置影片素材包

這個資料夾保存影片企劃、可核對的建置證據，以及後續拍攝流程。入口文件：[SHOTLIST.md](SHOTLIST.md)、[NARRATION.md](NARRATION.md)、[RECORDING_GUIDE.md](RECORDING_GUIDE.md)。素材逐項列在 [ASSET_MANIFEST.json](ASSET_MANIFEST.json)，含 SHA-256。

目前素材包有 2 張使用者提供的 PowerShell 截圖、3 次 Demo 的 Task/State、18 份 Handoff、結構化事件 log 與 Git 歷史。所有 JSON 原始記錄都保存在 evidence/，截圖未裁切或修改。

## 素材可信度標記

- `原始畫面`：使用者直接提供的截圖，複製原圖保存。
- `系統輸出`：MASERS 執行時寫入的 JSON/JSONL；複製原檔並雜湊。
- `Git 證據`：從本機 repository 擷取的 commit/status。
- `事後整理`：依本對話和已知執行結果整理成拍攝提綱；不是錄影，也不是原始 PowerShell transcript。
- `後續錄製`：使用 RECORDING_GUIDE 的 PowerShell transcript 和 OBS 螢幕錄影。

首次建立素材包時並未持續錄製桌面或麥克風，因此無法還原未錄到的逐字操作或聲音。之後每次開始建置工作，先啟動 transcript 和螢幕錄影，再操作系統。
