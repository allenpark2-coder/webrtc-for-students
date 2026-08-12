Gate: structure
Round: 3
Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69
Result: GATE PASS

# Chapter 02 Structure Review — Round 03

## 核查結果

- 14 個固定二級標題依序完整，另有「本章參考資料」；恰有五題及五份答案解析。
- 七張候選術語卡全部採全書固定九欄格式，沒有增加第八個候選詞。
- Chapter 01 已知概念、Chapter 02 七個新術語與 Chapter 03+ 排除範圍清楚分離。
- client／server 的文字、故事、題目、圖說與小卡都限定於本章 localhost HTTP connection，不描述為永久機器類型，也不泛化到所有通訊方式。
- IPv4／IPv6 最小共同模型，及只限 IPv6 的介面多位址與自動設定位址生命週期，均在正文、小卡、題目與來源中明確標界。
- LAN／WAN 已改成「相對有限區域」與「通常較大地理範圍／更多獨立使用者」，並明說沒有單一距離門檻；故事行政線不再充當正式定義。
- 兩個正式預定 SVG 引用都有 alt 與 caption，並仍說明圖的用途、比喻失真、非顏色辨識與禁止元素；後續圖稿必須對齊這些已審文字。
- 正式 Lab 為 N/A；localhost 練習仍具單機隔離、固定 port、一般權限、版本紀錄、停止條件、證據上限、故障、恢復與 cleanup 驗證。
- 執行環境清楚區分「Ubuntu 22.04.5／Python 3.10.12 已實跑」與「Ubuntu 24.04／Python 3.12.3 family 僅官方套件背景」，未把兩者混為同一證據。
- 章末來源皆記載狀態／版本、查核日期、支援主張與採用限制；RFC 791 使用 `replaces RFC 760`，RFC 1122／9293 與 BCP 165／RFC 7605 的關係也有明列。
- r01 的格式／首次介紹問題及 body technical r01 導致的結構性修訂均已落實，其他已通過項無退步。

本 Gate 不核准技術正確性、來源充分性或命令行為；這些須由綁定同一 SHA-256 的 body technical Gate 判定。
