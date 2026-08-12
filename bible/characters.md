# 故事人物與比喻對照表

> 第一階段固定角色候選。開始撰寫正文後視為唯讀；新增或調整時先寫入 `.work/proposals/characters-change.md`，取得使用者同意。

## 人物與物件

| 故事角色／物件 | 對應技術概念 | 比喻成立的範圍 | 比喻失真處 |
|---|---|---|---|
| 小明 | Browser／Peer A | 發起通話、提出能力與候選路徑 | Browser 內含多層 API、協定與作業系統，不是一個單一人物 |
| 小華 | Browser／Peer B | 接受或回應通話並交換媒體 | Offerer/answerer 不是永久角色，重新協商時行為可能改變 |
| 介紹人 | Signaling Server | 幫雙方交換應用層訊息、SDP 與 candidate | WebRTC 不規定 signaling transport；介紹人通常不承載媒體 |
| 雙方能力履歷表 | SDP | 描述媒體能力、方向與連線所需參數 | SDP 不會自己送達，也不是「影片格式清單」而已 |
| 聯絡方式清單 | ICE Candidate | 表示一個可能可達的 transport address | Candidate 不是保證可通的完整路徑，還需配對與檢查 |
| 警衛與社區出入口 | NAT／Firewall | 說明內外位址、映射與政策如何影響可達性 | NAT 與 firewall 是不同能力；真實映射與過濾行為比門禁複雜 |
| 地址詢問站 | STUN Server | 從外部觀察 mapped address，協助形成 server-reflexive candidate | STUN 不會替雙方轉送媒體，也不保證穿越所有 NAT |
| 物流轉運中心 | TURN Server | 直連不可行時 relay 雙方流量 | TURN 不解碼媒體內容，也不是 signaling server |
| 試路小隊 | ICE Connectivity Check | 測試 candidate pair 是否可達並選出路徑 | ICE 有優先序、角色與 nomination，不只是依序 ping 每條路 |
| 安全握手 | DTLS Handshake | 驗證 fingerprint 並建立 SRTP 所需金鑰材料 | DTLS 本身不是媒體封裝，也不等於網站 HTTPS |
| 防拆封條 | SRTP／SRTCP | 保護 RTP／RTCP 的機密性與完整性 | 真實安全性依賴金鑰、重放保護與端點安全，不只是貼封條 |
| 視訊包裹／追蹤回條 | RTP／RTCP | RTP 承載即時媒體；RTCP 回報品質與同步資訊 | RTP 不保證送達或順序；RTCP 也不只是一張單一回條 |
| 包裝規格 | Codec／Packetization | 說明媒體如何編碼，以及編碼資料如何放進 RTP payload | Codec 與 packetization 是不同層次；相同 H.264 不代表一定互通 |
| 道路壅塞觀察員 | Congestion Control／Stats | 從 loss、RTT、jitter、bitrate 等證據調整傳送 | 演算法不是只看單一指標，也不保證畫質永遠穩定 |
| 攝影機工廠與轉運站 | IP Camera／RTSP Gateway | 區分攝影機輸出、RTSP/RTP 與瀏覽器 WebRTC 邊界 | Gateway 可能只重封裝，也可能轉碼、終止安全連線與重做 signaling |

## 使用規則

- 全書固定使用小明與小華，不引用或改編相鄰的 `webrtc_story` 專案。
- 同一技術概念只使用上表的核心比喻；新比喻需先提案。
- 正文第一次使用比喻時，必須緊接正式元件、流程及「成立／失真」說明。
- 不把 signaling 流畫成媒體流，不把 TURN 畫成必經路徑，不把 NAT 與 firewall 合併成同一元件。
- 人物對應概念只有在章節全部 Gate 通過後，才由主代理追加至 glossary。
