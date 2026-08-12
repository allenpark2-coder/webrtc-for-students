Gate: editorial
Round: 1
Content-SHA256: 0a9673a4bbf89a6b51b8da3a1c65d2328f0c6e9a0a90f4d6a3741a84a7933d16
Result: GATE PASS

# Chapter 01 最終編輯審查 r01

## 審查範圍

- 正文：`.work/chapter-01/draft-r03.md`
- 章節範圍：`.work/chapter-01/scope.md`
- 正式計畫：`book/plan.md` 的 Chapter 01 與 Chapter 02
- 讀者狀態：`state/current/`；目前仍是 Chapter 00，`known-concepts.md` 尚無核准術語
- 書籍基準：全部 `bible/*.md`
- 前置正文 Gate：`structure-r03.md`、`body-technical-r03.md`
- 前置圖 Gate：`figure-technical-r02.md`、`figure-accessibility-r02.md`
- 圖規格與 metadata：`story-spec-r01.md`、`technical-spec-r01.md`、`metadata-r02.md`
- 實際圖：`story-r02.mmd/.svg/.png`、`technical-r02.mmd/.svg/.png`
- 正式 Lab：不適用；本章只有安全的產品層觀察與紙上替代

正文 SHA-256 已重新計算，等於本 Gate 綁定值。四份前置 review 均綁定相同正文 hash，圖 Gate 另綁定 artifact-set SHA-256 `19f5197167bbec5f7e19426441479143b723f051c1420ae81ee59284a152cb7c`，結果皆為 `GATE PASS`。

## 學習目標與章節定位

1. 正文清楚比較「完整內容先完成再傳送」與「內容持續產生時持續交換」；沒有把差異簡化為影片長短或傳輸速度。
2. 取得內容、交換協調資訊、找出到達方式、保護交換、持續傳送、適應變化六類問題均完整出現，且反覆提醒它們可能交錯或同時發生，不是固定單一路線。
3. WebRTC 被限定為一組標準化瀏覽器能力與處理模型，不被描述成單一 server、protocol、檔案格式或固定路徑。
4. Peer 被限定為一次通訊中的端點角色；正文、圖與題目都明確排除「peer 必然代表直接傳送」的推論。
5. 單向畫面、mute 指示與對端收音現象都只支持有限結論；正文完成了「目標、證據、結論範圍一致」的入門學習目標。
6. 沒有安全操作環境時可完成紙上情境，故設備不足不會阻塞本章成果。

六項 scope 學習目標皆有對應正文、觀察活動或理解題，沒有新增超出 Chapter 01 的學習負擔。

## 14 段結構與難度曲線

- 固定 `## 1.` 至 `## 14.` 依序完整，章末另有 `## 本章參考資料`。
- 第 1～3 段依序完成問題、故事與讀者先猜需求；第 4～5 段才引入正式名稱和小卡，符合先直覺後名稱的教學順序。
- 第 6～8 段以兩張圖及六問地圖把故事轉成概念架構，仍不進入後章實作細節。
- 第 9～12 段從觀察表、正常 baseline、單一 mute 故障到恢復與 cleanup，難度每次只增加一個可觀察步驟。
- 第 13 段沒有加入新概念；第 14 段恰有五題及五份解析，涵蓋差異、六問、peer 邊界、單向現象與證據限制，重點是「為什麼」而非背縮寫。
- 對 15～18 歲且沒有網路程式背景的讀者，文字、表格與活動均可理解；沒有要求程式碼、網路設定、封包工具或規範細節。

## 知識依賴、術語與前後銜接

- `state/current/known-concepts.md` 尚無術語；正文只正式引入「即時通訊（Real-Time Communication）」「網頁即時通訊（Web Real-Time Communication, WebRTC）」與「對等端（peer）」三項，和 scope、正式 plan、術語 crosswalk 一致。
- 三張小卡均具有英文、中文、一句話、生活比喻、真正作用、常見誤解、適用範圍、首次章節與來源；尚未直接寫入 `bible/glossary.md`。
- Browser、mute/unmute、baseline、Debug 與 cleanup 只在讀者已熟悉的產品操作或工程活動語境使用，不被當成未教 protocol、API 或內部元件。
- 正文未正式教授 client/server、IP/port、NAT/firewall、媒體擷取 API、PeerConnection、signaling、ICE/STUN/TURN、安全 transport、RTP/RTCP、codec、Stats 或後段工具。
- Chapter 01 留下「兩端可能位於不同環境，資料如何到達」的明確問題；Chapter 02 接著教授 client/server、IP、port、LAN/WAN，銜接自然且不需要讀者預先知道 Chapter 02 術語。
- Chapter 02 可沿用本章「端點角色」「證據不能超過觀察」的心智模型，不需回頭補教 Chapter 01 遺漏概念。

## 故事、比喻與圖引用

- 故事只使用核准的小明與小華；沒有啟用介紹人、警衛、地址詢問站、物流中心或其他後章角色。
- 完成影片／持續對話的比喻同時列出成立範圍與失真處，明確禁止由「直接說話」推論實際路徑。
- 正文恰有兩個 SVG 引用，位於第 6、7 段；未來從 `book/chapters/chapter-01.md` 解析時，分別指向正式 story 與 technical 路徑。
- 兩組正文 alt text、caption 與 `metadata-r02.md` 一致，內容也和實際 r02 PNG/SVG 圖面相符。
- 生活圖目視可清楚區分完整影片的串行等待與持續互動的交錯回應；專業圖目視可清楚區分協調資訊的點狀／虛線樣式與即時影音的實線樣式。
- 兩張圖都包含不表示真實資料路徑的文字限制；專業圖另明示不表示直接傳送、實際拓撲或內部做法。圖面沒有提前加入 server、network、protocol、安全或封包元件。
- 圖技術、caption、alt、灰階、對比與 ARIA 的前置 Gate 已通過；本輪沒有發現正文引用和實際圖內容不一致。

## 來源與版本

- 章末只使用兩項與本章實際主張直接相關的第一手來源：W3C WebRTC Recommendation 2025-03-13 與 RFC 8825。
- 每項來源都包含版本／發布日期、2026-08-12 查核日期與支援主張。
- RFC 8825 和目前 `bible/spec-baseline.md`、scope、正式 plan 一致，標為 Proposed Standard／Internet Standards Track；正文同時說明它是 applicability statement／規範 roadmap，本身不另行定義 protocol。
- 原始需求沒有被當成技術正確性來源；正文沒有長篇引用或未註明第三方程式碼。

## 安全、正式 Lab N/A 與恢復

- 本章明說沒有正式 Lab，也不寫 WebRTC 程式；正式累積式 Lab 從 Chapter 04 開始。因此本章沒有 Lab artifact 是合理的 `not_applicable`，而非遺漏。
- 章內活動只允許兩部自有裝置、兩個自有帳號、無第三人、無錄音錄影的測試通話；不符合條件時有完整紙上替代。
- 耳機／低音量、非自有設備、錄製、付費、第三人、回授、不適與過熱等停止條件均明確。
- 故障只改動小明端既有 mute 狀態；正文禁止同時修改網路、權限、系統聲音、攝影機或小華端，控制變因清楚。
- 正常 baseline、故障證據、有限結論、unmute 復原、未恢復處理、結束通話、關閉分頁／應用、確認裝置停止使用與不保留個資均完整。

## 晉升判定與主代理交接

本章在 editorial 範圍內沒有阻擋項，可以進入主代理的候選晉升流程。這個判定不直接完成正式晉升；主代理仍須：

1. 依已核准 mapping 複製正文、兩張圖的 spec/Mermaid/SVG 與 metadata 至正式路徑。
2. 將 `structure`、`body_technical`、`figure_technical`、`figure_accessibility`、`editorial` 設為 pass；將 `lab_execution`、`lab_technical` 設為 `not_applicable` 並附「概念入口章、正式 Lab 自 Chapter 04 開始」的 note。
3. 建立綁定正文與 figure artifact set hash 的 Chapter 01 manifest/evidence，先執行 repository validator。
4. Validator 通過後才追加三個核准 glossary 詞條、debug log 與 Chapter 01 state snapshot，原子更新 `state/current`，再執行一次 validator。

目前 `state/current` 保持 Chapter 00、glossary 尚未追加，符合候選晉升前狀態，不構成本 Gate 阻擋。

Result: GATE PASS
