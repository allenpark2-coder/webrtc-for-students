# 來源、引用與授權政策

## 技術來源優先序

1. W3C WebRTC／Media Capture 規範、IETF RFC 與 Web Platform Tests。
2. Chrome／Chromium、Node.js、coturn、FFmpeg、MediaMTX 的官方文件、release notes 與原始碼。
3. MDN 只作教學補充；部落格、論壇與影片不得作為唯一技術依據。

每個易變主張必須記錄版本與查核日期。RFC 被更新或取代時，同時記錄舊新編號與本書採用範圍。找不到可靠來源時標示未知或刪除，不用印象補齊。

全書共同規範的 status、updates／obsoletes 與採用章節記錄在 `spec-baseline.md`；章節只引用自己實際使用的子集。

## 章末引用格式

```markdown
- [來源名稱](URL) — 版本／發布日期；查核日期 YYYY-MM-DD；支援的主張。
```

避免長篇逐字引用；用自己的話解釋並連回原始來源。程式碼片段必須是本專案自行撰寫，或記錄來源與相容授權。

## 原始需求與外部素材

- `references/original-webrtc-brief.txt` 是使用者需求與範圍來源，不是技術正確性的依據。
- `/home/felix/work/webrtc_story` 及其文字、程式碼、動畫與輸出完全排除，不得讀取、引用、複製或改編。
- 第三方測試影片、圖片、字型與封包檔必須有可再散布授權；否則以專案自行產生的素材取代。

## 圖像與資產

- 每張第三方或生成圖片登記於 `book/assets/figures/ATTRIBUTION.md`。
- 記錄來源、作者／工具、日期、授權、修改、prompt／規格與對應章節。
- 正式圖必須有 caption 與 alt text，不能只靠顏色，並通過對比與灰階列印檢查。

## Lab 與安全

- 只使用 localhost、自己擁有或明確核准的 LAN、container、VM 與測試設備。
- `tc netem`、封包阻擋與路由變更只在隔離 Ubuntu VM/container 執行，不碰 host 的主要連線。
- Wireshark capture 只擷取本書 Lab 產生的流量；不開啟 promiscuous capture 觀察他人資料。
- 不掃描、攻擊或修改未授權系統，不連接未知 IP Camera，不提交真實憑證、個資、媒體或 `.env`。
- 每個故障實驗都包含前置檢查、停止條件、預期現象、復原、cleanup 與驗證已恢復的步驟。
- 需要 Internet、公開 TURN 或產生成本的測試，必須先取得使用者同意。
