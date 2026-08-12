Gate: editorial
Round: 1
Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6
Result: GATE PASS

# Chapter 03 最終編輯審查

## 審查範圍與候選鏈

- 受審正文為 `.work/chapter-03/draft-r02.md`；已重算 SHA-256，與頁首綁定值一致。
- `structure-r02`、`body-technical-r02` 均通過且綁定同一正文 hash。
- `figure-technical-r02`、`figure-accessibility-r02` 均通過，並共同綁定圖候選集 `302b6630def6f8370f2c1967ce17da5c219212db1e06e868af13c9ae1ca976fb`。
- 本審查另核對 Chapter 03 scope、source audit、正式計畫 Chapter 03–05、Chapter 02 最新讀者狀態與正式正文銜接、全部 bible、兩張 r02 圖候選及其 Gate evidence。
- 正式 Lab 為不適用；章內只有 rootless user＋network namespace 安全觀察，正文技術 Gate 已實際執行並核准其證據、恢復與 cleanup。

## 學習目標與難度曲線

- 正文完成 Chapter 03 的核心目標：分開 RFC 1918 private IPv4、public/global realm 與 outside observation；辨識 NAT／NAPT 及 mapping；把 mapping evidence 與 firewall policy evidence 分層；比較 UDP datagram 與 TCP reliable in-order byte-stream service；把跨網路失敗拆成可驗證假設。
- Public IP 的正文模型比早期 scope 中的「外側便利用語」更精確：r02 依已通過的 body technical Gate，把 public/global realm 與觀察位置相關的 outside observed address 分開。這仍實現原學習目標，並消除「非 RFC 1918 或位於 NAT 外側即為 public」的錯誤二分。
- 難度依問題、生活故事、工程師假設表、正式名稱、八張小卡、兩圖、流程、最小觀察、故障與理解題逐級增加。四個容易混淆的層次會反覆出現，但每次負責不同教學功能，而非堆疊新主張。
- Namespace 操作對無 Linux 背景讀者較進階，但正文先鎖版本、source hash、唯一 loopback 目標、資源上限與停止條件，並提供完整紙上 trace 替代；讀者不必具備 Linux 管理能力才能完成概念學習。
- Scope 原先構想 disposable container network，正文改採一次性 rootless user／network namespace。正文直接揭露這項替換，未假稱具備 image digest；新的實作仍滿足隔離、單一變因、可復原、可清理與不碰 host 網路的編輯目的，且已有實跑 evidence，因此不構成學習目標偏離。

## Chapter 02 先備與未教先用

- Chapter 02 結尾已提出「跨不同網路時位址可見範圍可能不同、網路可能依規則允許或阻擋」但未命名機制；Chapter 03 第一段正面承接 localhost 的 address＋port 模型，銜接自然。
- 正文只直接依賴 Chapter 01–02 已知的 WebRTC／peer 鳥瞰、IP address、port、LAN/WAN、packet 非送達保證，以及「證據範圍必須配合結論」；沒有要求讀者已學 NAT、firewall 或 transport 細節。
- `listener`、log、marker、exit status、namespace 等只作章內工具詞，均以用途、成功 evidence 或停止條件就地限定，不列為新的 WebRTC 核心小卡。
- 測試程式中的 `client` 只作「主動送出 echo marker 的 CLI role」操作標籤，正文沒有把 Chapter 02 的 HTTP client/server 定義改寫成所有協定的永久分類；UDP/TCP 正式教學仍以 service semantics 為主。
- `application congestion responsibility` 只作 UDP 使用責任的必要限制，沒有展開後章才教的 congestion-control 演算法、指標或調節流程；Chapter 14 的首次系統教學邊界仍完整。
- 獨立掃描未發現 `getUserMedia()`、MediaStream／track、`RTCPeerConnection`、signaling／SDP、ICE／candidate、Stats、STUN/TURN、DTLS-SRTP、RTP/RTCP、codec 或 gateway 等 Chapter 04+ 正向教學偷渡。

## 固定結構、八張小卡與重複控制

- 正文含依序且僅一次出現的固定 14 段，之後另有「本章參考資料」；第 14 段恰有五題及五份答案解析。
- 第 5 段恰有八張候選小卡：private IP address、public IP address、NAT、NAPT、mapping、firewall、UDP、TCP。每張均含九個固定欄位；NAPT 的獨立卡是避免把所有 NAT 說成一定改 port 的必要精準拆分。
- Outside observed address 明示為觀察位置相關的輔助說法，不是第九張候選小卡；datagram、byte stream、reliable、in-order 亦只在 UDP/TCP 小卡中立即解釋，沒有擴張詞庫候選數量。
- 重複內容形成清楚鷹架：故事建立分工直覺，正式名稱提供邊界，小卡供查閱，圖整理關係，流程建立證據順序，namespace 觀察只驗證 listener／transport，理解題再限制推論。沒有同段重複或藉重述新增未審查機制。

## 故事、比喻與人物一致性

- 小明、小華延續 bible 固定人物；沒有新增具名常駐角色，也沒有引用排除專案素材。
- 總機只負責內外聯絡表示與暫時對照；警衛只負責另依 policy 判斷。正文緊接著標出失真處：兩項工作可共置、分離或只存在其一，圖上兩站不是物理拓撲定律。
- 明信片只承擔 UDP 保留 datagram 邊界與非保證語意；連續紙帶只承擔 TCP 建立狀態後的可靠、按序 byte stream。正文同時說明應用可補可靠性、TCP 可等待或失敗、不保留應用 message boundary，且兩者不能抽象排名速度。
- 外線聯絡表示沒有被當作 public/global realm、全球可達或永久身分；mapping、allow 與 listener existence 的三層結論上限在故事、正式名稱、圖與問題中一致。

## 兩張圖與正文功能

- 正文的 story／technical SVG 引用路徑會在正式 Chapter 03 位置正確解析；兩段 caption、alt 與 r02 metadata、spec、MMD、SVG 均經 figure Gate 核對一致。
- 生活圖把 mapping、policy、allow/block、listener 及 UDP/TCP 兩種服務放在彼此分離的 panel；A、B 與全圖比喻界線之間沒有可見資料箭頭，不會把故事拓撲與 transport 時間線串成單一路徑。
- 專業圖清楚分開兩個平行 mapping 案例、中介 evidence 界線、獨立 firewall policy 與 outside observation；圖面直接寫出 `mapping record ≠ policy evidence`、`mapping ≠ allow`、`allow ≠ listener exists`。
- Technical 的 UDP/TCP 泳道保留 delivery／duplicate／ordering／congestion 與 failure／immediate／processed／security 限制，並明示 TCP 面板不接 NAT、兩者不排名速度。兩張圖沒有加入 Chapter 04+ 元件或正文 Gate 後的新技術主張。

## 章內觀察、安全閉環與正式 Lab 判定

- 全書累積式 Lab 自 Chapter 04 開始，因此 Chapter 03 正式 Lab N/A 合理；namespace 觀察不建立 `book/labs/chapter-03/` artifact，也不模擬 NAT 或 firewall。
- 活動只在一次性 rootless user＋network namespace 內啟用 loopback，目標固定為 `127.0.0.1:49152`；不建立 veth、route、NAT 或 firewall rule，不連 Internet／LAN／production，不要求 `sudo` 或 host capability。
- 正文明列 Ubuntu、CPU、Python、util-linux、iproute2 版本及自寫程式 source SHA-256；成功需同時具有 client `ECHO_OK`、相同 transport／marker 的 listener log 與 exit `0`，UDP `SEND_OK` 單獨不算收到。
- 故障一次只停止一個已記錄 listener PID，另一 transport 必須仍成功；之後只重啟剛才停止者並重驗 baseline。正文禁止把此故障稱為 NAT mapping、firewall、Internet loss 或效能實驗。
- 停止條件涵蓋版本／hash 不符、非 loopback address／route、需要提升權限、出現外部 marker、無法辨認 PID 等情況；不符合時改讀紙上 trace。
- Cleanup 只處理兩個已知 PID、三個明確檔案與精確暫存目錄，並確認 PID、檔案、目錄及 probe process 均消失。Body technical evidence 顯示 baseline、逐一故障、逐一恢復與 cleanup 已在鎖定環境實際完成。

## 來源政策與參考資料

- 章末共有 13 筆來源，涵蓋 RFC 1918、2663、4787／6888／7857、8085、9293、NIST firewall guidance、IANA registry，以及 Python／namespace／iproute2 工具來源。
- RFC 條目列出 status、updates／obsoletes、查核日期與本章採用／排除範圍；工具來源也綁定實測版本或 source hash。來源格式與 `source-policy.md` 一致。
- 規範來源支撐概念與邊界，工具來源只支撐 namespace／命令行為；正文沒有用原始需求、部落格或未核准相鄰專案作技術正確性依據。
- Source audit 指出的三個主要風險均已關閉：private/public 不是 RFC 1918 二分；RFC 4787 的 mapping 例只限單播 UDP／IPv4 Traditional NAT；firewall 使用直接 NIST 來源而不從 NAT 文件泛化。

## Chapter 04／05 銜接與晉升判斷

- Chapter 04 只依賴 Chapter 01 的 media-capture 起點；Chapter 03 未要求讀者先把 network namespace 或 transport 練習當成取得攝影機／麥克風的先備，故不製造不必要依賴。
- Chapter 05 正式依賴 Chapter 03 與 04。Chapter 03 已交付其所需的最小網路心智模型：address／port 之外仍有 mapping、獨立 policy、transport／listener 與證據範圍；但沒有提前教授 PeerConnection、track、sender slot 或 connection state。
- Chapter 05 可把自己的控制桌與 WebRTC API 建立在本章網路底座及 Chapter 04 media tracks 上；Chapter 03 的 namespace 工具細節不成為向後依賴，也不把 TCP connection 等同未來的 `RTCPeerConnection`。
- 學習目標、固定結構、術語首次教學、故事比喻、圖文映射、來源、安全觀察及章際依賴均一致；未發現需退回 storyteller、domain-expert 或 diagram-designer 的編輯阻擋項。此候選可交由主代理建立正式 manifest 候選並執行 `scripts/validate_kit.py`；本 Gate 本身不代表已完成正式晉升、glossary 或 state 更新。
