# 後續拍攝與紀錄操作

## 已保存的歷史素材

歷史素材包包含使用者提供的三張 PNG 原檔、MASERS 三次 demo 的 tasks/state/handoffs/events，以及當前 Git 歷史和 status。`ASSET_MANIFEST.json` 為每個素材記錄相對路徑、byte size、SHA-256 和來源。這些檔案可以直接交給剪輯者；副本是否一致可用 `Get-FileHash -Algorithm SHA256` 核對。

先前的互動沒有啟動桌面錄影或 PowerShell `Start-Transcript`，所以不存在完整的歷史影片、音軌或逐字終端日誌。Git 和 JSON artifact 是當時自然產生的執行證據；本資料包內的時間線和旁白是依那些證據與對話事後整理。

## 即時錄製新建置階段

1. 開啟 OBS Studio，新增「顯示器擷取」或「視窗擷取」，選擇 PowerShell/編輯器；先確認預覽只有要公開的畫面。設定 1920×1080、30 fps，錄影格式選 MKV，完成後再用 OBS Remux 成 MP4。
2. PowerShell 切到 repository，直接在互動式命令列輸入以下命令：

   ```powershell
   Set-Location "C:\Users\NNKIEH\Documents\ChatGPT\系統開發"
   $captureDir = Join-Path $PWD "docs\video\evidence\transcripts"
   New-Item -ItemType Directory -Path $captureDir -Force | Out-Null
   $captureStamp = Get-Date -Format "yyyyMMdd-HHmmss"
   Start-Transcript -Path (Join-Path $captureDir "build-$captureStamp.txt") -NoClobber
   ```

   這些是互動式命令，不會載入 `.ps1` 檔，因此不會觸發畫面所示的 script execution policy 拒絕。

3. 在同一個 PowerShell 視窗手動操作並口述；Transcript 會持續到輸入 `Stop-Transcript`。重要節點可另存 OBS 片段或使用 OBS screenshot。
4. 每個可驗證小階段後記下 milestone、commit ID、測試命令/結果、已知問題與下一步至根目錄 `BUILD_LOG.md`，並以 Git commit 保存文件與程式。不要把 `.masers` 全域忽略的狀態檔忘記歸檔：選擇性複製到 `docs/video/evidence/runs/`。
5. 建置告一段落時，在同一 PowerShell 視窗執行：

   ```powershell
   Stop-Transcript
   ```

6. 對 transcript、圖片、測試輸出和 demo JSON 更新 `ASSET_MANIFEST.json`，保存來源與 SHA-256。原始錄影和無損原圖放在素材目錄；剪輯輸出另放，不覆寫原件。

## Transcript 包含範圍

PowerShell transcript 會保存該視窗的命令與輸出，包含路徑、錯誤文字和任何使用者打出的內容，開頭也會記錄 Windows 帳戶及電腦名稱。原始 `.txt` 已由根目錄 `.gitignore` 排除，僅保存在本機；公開前應複製一份，遮蔽帳戶名稱、裝置名稱、私人路徑及憑證，再把已審核版本加入素材清冊。開始前清除不想入鏡的私人資料；不要在畫面或命令列顯示 API keys、token、`.env` 或 credential。錄影及 transcript 必須同一階段開始，才有同步可核對的旁白和文字。
