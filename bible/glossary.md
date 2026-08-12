# 專有名詞小卡資料庫

> 本檔累積正式核准詞條。作者只在草稿提出候選詞條；主代理於章節所有 Gate 通過後追加。

---

<!-- 正確格式範例；此註解不代表本書已正式教過 NAPT。

## NAPT
英文：Network Address Port Translation
中文：網路位址與連接埠轉換
一句話：同時轉換位址與傳輸層識別碼，讓多台私有網路主機的連線共用外部位址
生活比喻：總機用不同分機號碼，把多位同事的通話對應到同一支公司代表號
真正作用：在位址轉換之外也轉換 TCP／UDP port 等識別碼，將多個內部 session multiplex 到一個或一組外部位址
常見誤解：NAPT 不是防火牆，也不提供加密、身分驗證或授權
適用版本／範圍：IPv4；術語依 RFC 2663
首次出現章節：Chapter N
來源：https://www.rfc-editor.org/rfc/rfc2663.html#section-4.1.2

-->

## 即時通訊

英文：Real-Time Communication
中文：即時通訊
一句話：資訊產生後，在足以支援互動的時間內持續交換
生活比喻：小明說話時，小華不必等完整影片做完，就能聽見、理解並回應
真正作用：描述一種重視持續交換與互動時間的通訊需求
常見誤解：「即時」不代表完全零等待、永不失敗或品質永遠相同
適用版本／範圍：本書的瀏覽器即時影音與資料通訊入門範圍
首次出現章節：Chapter 01
來源：https://www.rfc-editor.org/rfc/rfc8825.html

## WebRTC

英文：Web Real-Time Communication
中文：網頁即時通訊
一句話：讓瀏覽器與相容端點建立即時通訊所需的一組標準化能力與處理模型
生活比喻：小明與小華要持續對話，需要一整套互相配合的準備與處理能力
真正作用：支援瀏覽器建立即時聲音、畫面或資料通訊；Chapter 01 只介紹整體定位
常見誤解：WebRTC 不是單一設備、單一傳送規則、視訊檔格式，也不保證固定的資料到達方式
適用版本／範圍：W3C WebRTC Recommendation 2025-03-13；本書以瀏覽器情境為主
首次出現章節：Chapter 01
來源：https://www.w3.org/TR/2025/REC-webrtc-20250313/

## 用戶端

英文：client
中文：用戶端
一句話：在本章 localhost HTTP 情境中，建立一條 connection 的參與者
生活比喻：這次走到服務窗口提出要求的小明
真正作用：依這一條 HTTP connection 判定角色；例如瀏覽器建立通往同一台電腦測試服務的 connection 時，瀏覽器是該 connection 的 client
常見誤解：client 不是永久機器類型；同一程式可在不同 HTTP connection 中交換角色，本章也不把定義泛化到所有通訊方式
適用版本／範圍：僅限本章 localhost HTTP connection 與 RFC 9110 §3.3
首次出現章節：Chapter 02
來源：https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3

## 伺服器

英文：server
中文：伺服器
一句話：在本章 localhost HTTP 情境中，接受一條 connection 的參與者
生活比喻：這次等待校務文件並提供結果的服務窗口
真正作用：依這一條 HTTP connection 判定角色；例如本機測試程式接受瀏覽器建立的 connection 時，它是該 connection 的 server
常見誤解：server 不等於整台機器，也不一定在雲端、比較強或永久只提供服務；本章不把定義泛化到所有通訊方式
適用版本／範圍：僅限本章 localhost HTTP connection 與 RFC 9110 §3.3；不引入系統內部服務管理
首次出現章節：Chapter 02
來源：https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3

## 網際網路協定位址

英文：Internet Protocol address（IP address）
中文：網際網路協定位址
一句話：IPv4 與 IPv6 封包中用來表示來源與目的網路位置的位址
生活比喻：指出要前往哪棟大樓的地址
真正作用：RFC 791 與 RFC 8200 共同支持 IPv4／IPv6 都有來源與目的位址；在 IPv6 範圍，位址配給介面，單一介面可有多個位址
常見誤解：IP address 不是人、帳號、瀏覽器、房間、裝置序號或永久身份；位址生命週期的例子僅限 RFC 4862 的 IPv6 自動設定，不能外推到所有 IP 位址
適用版本／範圍：共同模型只含 IPv4／IPv6 的來源與目的位址；介面多位址限 RFC 4291 §2.1，生命週期限 RFC 4862 的 IPv6 自動設定
首次出現章節：Chapter 02
來源：https://www.rfc-editor.org/info/rfc791、https://www.rfc-editor.org/info/rfc8200、https://www.rfc-editor.org/rfc/rfc4291.html#section-2.1、https://www.rfc-editor.org/info/rfc4862

## 連接埠

英文：port
中文：連接埠
一句話：在特定傳輸脈絡中，用來識別服務端點的數字欄位
生活比喻：到達大樓後，還要前往正確辦公室入口
真正作用：區分同一 IP address 上的不同服務；例如測試服務位於 port A 時，舊 port B 不會因此提供同一服務
常見誤解：port 不是實體洞、不是應用程式本身、不是全球唯一房號，也不能離開 IP address 和傳輸脈絡單獨定位服務
適用版本／範圍：依 RFC 6335 與 IANA registry 的服務名稱／port number 管理背景；不比較具體傳輸規則
首次出現章節：Chapter 02
來源：https://www.rfc-editor.org/rfc/rfc6335.html#section-6

## 區域網路

英文：Local Area Network（LAN）
中文：區域網路
一句話：位於相對有限區域內的一組電腦與其他裝置
生活比喻：文件在一棟建築等相對有限區域內傳遞
真正作用：描述相對有限的網路範圍，例如一棟建築內；真實分類仍須查看具體網路設計
常見誤解：LAN 沒有本章自訂的單一距離門檻，也不表示任意兩台相近裝置一定互通；故事中的校園或行政線不是分類公式
適用版本／範圍：採 NIST SP 800-82 Rev. 3 glossary 的相對有限區域定義
首次出現章節：Chapter 02
來源：https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 廣域網路

英文：Wide Area Network（WAN）
中文：廣域網路
一句話：通常跨較大地理範圍並服務較多獨立使用者的網路
生活比喻：文件跨到較大地理範圍，連接更多獨立使用者
真正作用：描述通常較大的地理尺度與較多獨立使用者，也可把較小網路互連起來
常見誤解：WAN 不是「超過某個距離」的同義詞，也不等於 Internet；故事邊界不能代替真實分類
適用版本／範圍：採 NIST SP 800-82 Rev. 3 glossary；沒有單一距離門檻，不教授互連內部如何選路
首次出現章節：Chapter 02
來源：https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 封包

英文：packet
中文：封包
一句話：網路層處理的一個有格式、有限大小資料單位
生活比喻：一次一份、有邊界的寄件單位
真正作用：把處理資訊與所攜內容組成網路可處理的單位，而不是把整份檔案視為不可分割的一塊；版本中立概念圖會分層呈現來源 IP、目的 IP、傳輸欄位與所攜內容
常見誤解：packet 不是簽收保證；形成 packet 不保證送達、順序、只送一次或準時
適用版本／範圍：本書採版本中立入門模型；RFC 8200 直接支援 IPv6 header 加所攜內容的 packet 定義
首次出現章節：Chapter 02
來源：https://www.rfc-editor.org/rfc/rfc8200.html#section-3

## Peer

英文：Peer
中文：對等端
一句話：參與一次即時通訊的一端
生活比喻：故事中的小明端與小華端各代表一個參與通話的角色
真正作用：指出一次通訊中的參與端角色
常見誤解：peer 不等於一個人或一台永久固定的機器，也不保證資料直接在兩台裝置之間傳送
適用版本／範圍：Chapter 01 用於描述瀏覽器／peer 角色；實際資料到達方式留待後章
首次出現章節：Chapter 01
來源：https://www.w3.org/TR/2025/REC-webrtc-20250313/
