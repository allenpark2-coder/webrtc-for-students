# WebRTC for Students

《從視訊按鈕到即時連線：高中生也能懂的 WebRTC》的 Codex 書籍專案。

本書面向 15～18 歲、只有少量或沒有網路程式背景的讀者，以小明與小華的持續故事、真實架構圖、原生 JavaScript 與可重現 Lab，建立 WebRTC 的完整心智模型。它不是 API Reference，也不逐條改寫 RFC。

## 目前狀態

- 階段：正式逐章製作。
- 正式章節：Chapter 01～03 已通過全部適用 Gate 並晉升。
- 正式規劃：`book/plan.md`；使用者已於 2026-08-12 核准開始 Chapter 01。
- 最新 manifest：`book/manifests/chapter-03.json`。
- 原始需求：`references/original-webrtc-brief.txt`，只作需求與範圍來源。

下一步依正式 roadmap 建立 Chapter 04 scope與正式 Lab 01／02。

## 學生閱讀版

- 線上閱讀：<https://allenpark2-coder.github.io/webrtc-for-students/>
- `dist/chapter-01.html`：瀏覽器閱讀版，兩張 SVG 已內嵌，可離線開啟。
- `dist/chapter-01.pdf`：A4 下載與列印版。
- `dist/chapter-02.html`：Chapter 02 瀏覽器閱讀版，兩張 SVG 已內嵌，可離線開啟。
- `dist/chapter-02.pdf`：Chapter 02 A4 下載與列印版。
- `dist/chapter-03.html`：Chapter 03 瀏覽器閱讀版，兩張 SVG 已內嵌，可離線開啟。
- `dist/chapter-03.pdf`：Chapter 03 A4 下載與列印版。
- `dist/book.md`：通過 manifest 驗證後組裝的出版來源稿。

給學生時優先分享 HTML；需要傳到班級群組、Google Classroom 或列印時使用 PDF。

## 技術主線

- 桌面 Chrome Stable 與 `chrome://webrtc-internals`。
- 原生 HTML／JavaScript、Node.js 24 LTS 與 WebSocket signaling。
- coturn 作 STUN／TURN 實驗。
- FFmpeg + MediaMTX 建立可重現的 RTSP/H.264 → WebRTC 特別篇。
- Ubuntu 24.04 LTS 是完整 Lab 驗證基準。

確切規範、版本、支援平台與安全界線以 `bible/book-config.md` 與 `bible/source-policy.md` 為準。

## 工作方式

Codex 依根目錄 `AGENTS.md` 協調五個 custom agents 與四個 repo skills。所有未核准內容留在 `.work/`；正式章節、圖與 Lab 只有通過對應 Gate 並綁定 SHA-256 後，才能晉升至 `book/`。

```text
範圍與依賴
  → 14 段正文 + structure Gate
  → 正文技術 Gate
  → 圖技術／無障礙 Gate
  → Lab 執行／技術 Gate
  → editor Gate
  → 正文／圖／Lab SHA-256 manifest
  → 正式晉升
```

## 驗證

```bash
python3 scripts/validate_kit.py
python3 -m unittest discover -s tests
```

## 內容與素材邊界

- 不讀取、引用、複製或改編相鄰的 `/home/felix/work/webrtc_story` 專案。
- 不在 production、未授權網路或他人設備上執行 Lab。
- 第三方技術內容、程式碼與圖片遵守 `bible/source-policy.md` 及 attribution 規則。

## 授權

本專案框架採 MIT License。未來書稿、第三方引用與媒體資產的最終出版授權，須在正式出版前另行確認。
