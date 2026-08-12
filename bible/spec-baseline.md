# WebRTC 規範與工具基線

> 查核日：2026-08-12。此表是規劃基線；每章送審與 Lab 執行前仍需重新核對官方來源。RFC 的「更新關係」不代表後出的文件取代全部內容，正文必須說明採用範圍。

## Web 與 Runtime

| 項目 | 採用基線 | 狀態與用途 |
|---|---|---|
| WebRTC API | W3C Recommendation 2025-03-13 | 全書 PeerConnection API 與處理模型；候選修訂需逐項標示 |
| Media Capture and Streams | 執行章節時的 W3C published snapshot | Chapter 04；scope 記錄 snapshot URL 與查核日 |
| WebRTC Statistics | 執行章節時的 W3C published snapshot | Chapter 07 首次教最小 `getStats()`／`RTCStatsReport` 與 candidate-pair/transport 關聯；Chapter 11 起按媒體概念逐步開放欄位；Ch14、17 才做時間序列與跨指標診斷。各 scope 鎖 snapshot URL/date，只用當版未淘汰且實測存在的欄位 |
| Chrome | Desktop Stable 151；Lab 記錄完整 build | 正式測試目標；UI 與 stats 不當作跨瀏覽器保證 |
| Node.js | 24 LTS | Chapter 15 signaling；套件以 lockfile 鎖定 |

## 核心 RFC 狀態

| RFC／規範 | Status／更新關係 | 本書採用範圍 | 章節 |
|---|---|---|---:|
| RFC 8825 | Informational | WebRTC 整體問題與使用情境 | 01 |
| RFC 1918 | BCP | IPv4 私有位址 | 03 |
| RFC 2663 | Informational | NAT/NAPT 術語；不把 NAT 說成 firewall | 03 |
| RFC 4787 | BCP；被 RFC 6888、7857 更新 | UDP NAT 行為；連同更新文件一起解讀 | 03 |
| RFC 8085 | BCP | UDP 使用與壅塞責任 | 03、14 |
| RFC 9293 | Internet Standard | TCP 基本語意 | 03 |
| RFC 9429 | Proposed Standard；obsoletes RFC 8829 | JSEP offer/answer 狀態與 API 對應 | 06 |
| RFC 8866 | Proposed Standard；obsoletes RFC 4566 | SDP 語法與描述邊界 | 06、12 |
| RFC 8445 | Proposed Standard；obsoletes RFC 5245 | ICE candidate、pair、check、nomination | 07–09、16 |
| RFC 8838 | Proposed Standard | Trickle ICE | 07 |
| RFC 8489 | Proposed Standard；obsoletes RFC 5389 | STUN protocol 與 Binding discovery | 07、08 |
| RFC 8656 | Proposed Standard；obsoletes RFC 5766 | TURN allocation、permission、relay | 09、16 |
| RFC 5764 | Proposed Standard；被 RFC 7983、9443 更新 | DTLS-SRTP keying；連同 demux/update 文件解讀 | 10、17 |
| RFC 8827 | Proposed Standard | WebRTC security architecture | 10 |
| RFC 3711 | Proposed Standard；被 RFC 5506、6904、9335 更新 | SRTP/SRTCP 保護模型；Ch10/11 採核心保護語意與 WebRTC 所需更新，不展開非本書使用的 transform 細節 | 10、11 |
| RFC 8834／8835 | Proposed Standards | WebRTC media 與 transport requirements | 10–14 |
| RFC 3550 | Internet Standard；obsoletes RFC 1889；被 RFC 5506、5761、6051、6222、7022、7160、7164、8083、8108、8860 更新 | RTP/RTCP 核心語意；Ch11 直接納入 RFC 5506 reduced-size RTCP 與 RFC 5761 RTP/RTCP multiplexing，Ch13/14 視需要引用 RFC 8108 feedback，其餘更新記錄但不作入門教學主線 | 11、13 |
| RFC 6184 | Proposed Standard | H.264 RTP payload format | 12、18 |
| RFC 7741／9628 | Proposed Standards | VP8／VP9 RTP payload formats | 12 |
| RFC 7742 | Proposed Standard | WebRTC video processing 與 codec requirements；和執行時能力分開陳述 | 12 |
| AOMedia AV1 RTP Payload Specification | 章節 scope 鎖定 commit/date | AV1 packetization；不得引用浮動內容作永久事實 | 12 |
| RFC 4585 | Proposed Standard；被 RFC 5506、8108 更新 | RTP/RTCP feedback 與 NACK/PLI；連同 WebRTC 相關 updates 解讀 | 13 |
| RFC 5104 | Proposed Standard | FIR 等 codec-control feedback；不與 RFC 4585 的更新關係合併 | 13 |
| RFC 8836 | Informational | WebRTC congestion control guidance；不得表述為 Standards Track requirement | 14 |
| RFC 2326 | Proposed Standard；被 RFC 7826 obsoleted | 現存 IP Camera 的 RTSP 1.0 部署現況 | 18 |
| RFC 7826 | Proposed Standard | RTSP 2.0 對照；不與 RTSP 1.0 行為混用 | 18 |
| `draft-ietf-wish-whep-03` | 已過期／封存的 Internet-Draft；published 2025-08-18，expired 2026-02-19；不是 RFC 或現行 IETF Standard | Chapter 18 固定的教學參考 snapshot；只作 work-in-progress 背景。查核日已有後續 revision，正文不得宣稱此 snapshot 為最新或穩定標準 | 18 |

## Lab 工具

| 工具 | 規劃版本 | 鎖定與責任 |
|---|---:|---|
| coturn | 4.17.2 | 實作前鎖 container digest；顯式設定 listeners、relay port range 與短效假 credential，不依賴 default |
| FFmpeg | 8.1.2 | 鎖 release signature/checksum；負責產生測試源及必要的 H.264/audio transcoding |
| MediaMTX | 1.20.0 | 鎖 release checksum/image digest；終止 RTSP 與 WebRTC/WHEP 連線並轉接媒體，不宣稱它替 Lab transcoding |
| Wireshark | Ubuntu 24.04 repository 的鎖定套件版 | 只擷取自產 Lab 流量；不解密或保存真實媒體 |

## IP Camera 必要介面

必要 Lab 路徑固定為：FFmpeg 自產測試素材 → RTSP/H.264 publish → MediaMTX → MediaMTX WebRTC 播放頁或 `/{path}/whep` → Chrome。這條路不使用 Chapter 15 的 Node.js WebSocket signaling server；不相容的 codec/profile/B-frame/audio 必須由 FFmpeg 在 ingest 前明確轉碼。

WHEP 教學背景固定引用 `draft-ietf-wish-whep-03`（2025-08-18 snapshot；已於 2026-02-19 過期）。它是易變的 work in progress，不是 RFC。Lab 實際驗收依賴的是 **MediaMTX 1.20.0 官方文件與該版本 `/{path}/whep` endpoint 的 implementation behavior**；不得把該 URL shape 或實作行為宣稱為現行 IETF standard，且 Chapter 18 scope 必須重新記錄當時最新 I-D 狀態。
