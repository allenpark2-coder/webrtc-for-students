# 書籍設定

> 本檔是第一階段的核准候選設定。開始撰寫正文後若需修改，先在 `.work/proposals/` 提案並取得使用者同意。

## 書籍識別

- 工作書名：《從視訊按鈕到即時連線：高中生也能懂的 WebRTC》
- 副標題：用故事、瀏覽器實驗與 Debug 建立真正的即時通訊心智模型
- 作者／團隊：allenpark2-coder
- 版本／版次：第一版規劃稿
- 預計出版日期：Roadmap 核准後排定

## 領域與範圍

- 領域主題：瀏覽器 WebRTC、即時影音網路、可觀察性與 RTSP／IP Camera gateway 入門。
- 核心問題：讓沒有網路程式背景的高中生理解兩個瀏覽器如何找到彼此、協商能力、安全傳送影音、適應不穩定網路，並能用證據 Debug。
- 涵蓋範圍：Internet 基礎、媒體擷取、PeerConnection、signaling、SDP/JSEP、ICE/STUN/TURN、DTLS-SRTP、RTP/RTCP、codec、網路品質、stats、兩端實作與 RTSP/H.264 gateway。
- 明確不涵蓋：逐條改寫 RFC、production 級身份／權限／擴縮／高可用、從零實作 TURN 或媒體伺服器、未授權網路測試、完整 SFU/MCU 實作、手機原生 SDK。

## 目標讀者

- 年齡／背景：15～18 歲，熟悉瀏覽器、手機與視訊通話產品。
- 已知：基本電腦操作；可以讀懂少量 HTML 與 JavaScript，沒有也能從最小範例跟上。
- 不假設的先備知識：TCP/IP 課程、非同步網路程式設計、密碼學、影音編碼、Linux 管理。
- 數學／技術程度：高中數學；只使用理解延遲、比例、速率與簡單統計所需的數學。
- 完成本書後能做到：完成兩瀏覽器 WebRTC 通話、部署測試 signaling/STUN/TURN、讀懂關鍵 SDP/candidate/stats、系統化 Debug，並完成模擬 RTSP/H.264 到瀏覽器的 gateway Lab。

## 核心教學哲學

從生活中「為什麼視訊按鈕不是一按就通」的問題建立心智模型，再依序進入正式名稱、真實元件、可觀察封包、最小程式與 Debug。比喻是腳手架，不是技術定義；每次都標示成立範圍與失真處。

## 教學展開順序

生活問題 → 小明與小華的持續故事 → 讀者先提出解法 → 簡單模型 → 正式名稱
→ 真實 WebRTC 架構 → 協商／連線／媒體流程 → 最小程式 → 瀏覽器實驗 → 故障 → 證據導向 Debug

## 技術基線

- Web API：W3C WebRTC Recommendation 2025-03-13；Media Capture and Streams 使用撰寫時最新發布版本並記錄查核日期。
- IETF：RFC 9429（JSEP）、8445（ICE）、8489（STUN）、8656（TURN）、8838（Trickle ICE）、8834/8835（WebRTC media/transport）及其規範性引用。
- 語言與 runtime：HTML、CSS、原生 JavaScript；Node.js 24 LTS；WebSocket 套件以 lockfile 鎖定確切版本。
- 瀏覽器：桌面 Chrome Stable 為正式目標；規劃基準為 Chrome 151，執行每個 Lab 時記錄完整版本。Firefox、Safari 只提供相容性提醒。
- TURN／媒體工具：coturn 4.17.2、FFmpeg 8.1.2、MediaMTX 1.20.0；實作時使用 `bible/spec-baseline.md` 指定版本，並在首次執行前鎖定下載 checksum 或 container image digest。
- 支援作業系統：Ubuntu 24.04 LTS 為完整驗證基準；一般瀏覽器 Lab 補 Windows 11 與目前受支援 macOS 步驟。
- 依賴鎖定：`package-lock.json`、container image digest、工具版本與測試輸出共同記錄。
- 技術查核截止日期：2026-08-12；規範狀態見 `bible/spec-baseline.md`，每章送審時重新查核易變資訊。

## 全書主題草稿

1. 網路與瀏覽器媒體的必要基礎。
2. WebRTC 的協商、找路、安全媒體與品質控制。
3. 可重現的兩端應用、網路故障與證據導向 Debug。
4. 從 RTSP/H.264/IP Camera 到瀏覽器 WebRTC 的工程整合。

## 領域專家審查重點

- 最容易講錯：signaling 不屬於 WebRTC wire protocol、STUN 不負責 relay、TURN 不等於 signaling、SDP 是描述而非傳輸協定、WebRTC 不保證 P2P。
- 最容易讓比喻失真：NAT 與 firewall、candidate 與路徑、DTLS 與 SRTP、RTP/RTCP、packetization 與 codec。
- 可能快速過時：瀏覽器支援、codec 能力、webrtc-internals UI、Node/coturn/FFmpeg/MediaMTX 版本。
- 需要實機驗證：權限與 secure context、candidate 產生、UDP 阻擋、TURN relay、stats 欄位、H.264 profile/B-frame 相容性與 RTSP gateway。

## Lab 環境與安全界線

- 允許環境：localhost、自己擁有或明確核准的 LAN、container、VM、專用測試設備及本機產生的媒體。
- 禁止環境：production、學校／公司未授權網路、他人攝影機、公開掃描、真實服務憑證與唯一一份設備。
- 費用／資源上限：必要 Lab 可在一般 4-core、8 GB RAM 電腦完成；預設不依賴付費雲端，TURN 外網測試需使用者另行核准。
- 備份與復原：所有設定版控；故障注入限 container/VM，執行前記錄基線，提供反向指令與重新建立步驟。
- 敏感資料：只用假帳密與 `.env.example`；真實秘密不得進入 repository、書稿、截圖或執行 evidence。

## 建議規模

- 頁數：360～420 頁。
- 插圖數量：至少 42 張，其中每章至少一張生活圖與一張專業圖。
- Lab 數量：15 個漸進式、可實際執行的 Lab。
