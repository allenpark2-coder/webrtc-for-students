Gate: structure
Round: 2
Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6
Result: GATE PASS

# Chapter 03 Structure Review — Round 02

## 審查邊界

本輪依 `$book-linter` 檢查 r01 唯一阻擋項及完整結構回歸；不判斷 RFC 主張、Python／namespace 行為或命令的技術正確性，也未修改草稿。受審正文 SHA-256 已重算，與頁首綁定值相同。

## r01 必改項驗證

- `draft-r02.md:19-36` 已把故事與工程師假設改為「暫時對照／規則判斷／兩種運送方式／等待者」等白話描述。排除章名後，第 4 段以前不再出現 `private IP address`、`public IP address`、NAT、NAPT、mapping、firewall、UDP 或 TCP 核心正式標籤；教學順序恢復為問題 → 故事 → 猜解法 → 正式名稱。
- `draft-r02.md:40-54` 依序以「私有 IP 位址（private IP address）」、「公用 IP 位址（public IP address）」、「網路位址轉換（Network Address Translation, NAT）」、「網路位址與連接埠轉換（Network Address Port Translation, NAPT）」、「對應（mapping）」、「防火牆（firewall）」、「使用者資料包協定（User Datagram Protocol, UDP）」與「傳輸控制協定（Transmission Control Protocol, TCP）」完成首次教學。
- r01 未展開的 `NAT44` 標籤已移除，改成「單播 UDP、內外都只談 IPv4 的 Traditional NAT 情境」。新增的「外側觀察位址（outside observed address）」在首次出現處立即定義、說明與 public IP address 的差別，並明示是觀察位置相關的輔助說法而非第九張候選小卡。

## 完整回歸結果

- 14 個固定二級標題依序且各僅一次，之後另有「本章參考資料」；沒有用無關內容填補不適用段落。
- 第 5 段恰有八張候選小卡，編號 1／8 至 8／8。每張的英文、中文、一句話、生活比喻、真正作用、常見誤解、適用版本／範圍、首次出現章節、來源九欄均恰有一份。
- 第 14 段恰有五題與五份答案解析，且未使用 Chapter 04+ 概念解釋答案。
- 固定人物只有小明、小華；總機／警衛和明信片／連續紙帶的成立與失真界線仍完整，NAT/firewall 與 UDP/TCP 沒有被混成同一責任或抽象快慢排名。
- 兩張預定 SVG 引用都有非空 alt text 與 caption；圖用途、禁止元素、非顏色辨識及外側觀察位址／public IP 邊界已同步修訂。後續圖 artifact 仍須逐字對齊通過正文 Gate 的圖文字。
- 正式 Lab 明列 N/A，累積式 Lab 自 Chapter 04 開始；章內觀察沒有建立正式 Lab artifact，也沒有把 listener 故障冒充 NAT／firewall 故障。
- Namespace 觀察保留隔離與權限邊界、OS／architecture／工具版本、自寫程式 source hash、固定目的／port、資源與 timebox、成功 evidence、停止條件、逐一故障、逐一恢復、cleanup、cleanup 驗證及紙上替代。內嵌 Python 重算 SHA-256 仍為 `e9b0e0723bc8bfbeac48bb20ce3b0699a6feceb08454d9a20a6f00bfdc6c1c7e`，與正文宣告一致。
- 章末現有 13 筆來源均列 2026-08-12 查核日期與採用範圍；規範與工具來源欄位存在。來源充分性與技術主張正確性留給 body technical Gate。

本輪未發現結構、首次教學、圖文字或安全欄位阻擋項；可將同一正文 hash 送交 body technical Gate。
