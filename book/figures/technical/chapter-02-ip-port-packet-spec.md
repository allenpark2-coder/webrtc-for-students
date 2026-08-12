# Chapter 02 專業圖規格 r01

Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69

> 對應正文：`.work/chapter-02/draft-r03.md`
> 正文技術 Gate：`.work/chapter-02/reviews/body-technical-r02.md`，GATE PASS
> 圖片狀態：規格草案；尚未生成正式圖。
> 預定正式規格路徑：`book/figures/technical/chapter-02-ip-port-packet-spec.md`
> 預定正式圖片路徑：`book/figures/technical/chapter-02-ip-port-packet.svg`

## 目的

用一張分區專業概念圖，把本章五種責任視覺上拆開：

1. 裝置名稱與本次 HTTP connection 的 client／server 角色。
2. 來源／目的 IP 所表示的網路位置欄位。
3. 來源／目的 port 所表示的分開傳輸欄位與目的端特定服務。
4. packet 作為獨立、有限的資料單位。
5. LAN 與 WAN 的相對尺度，以及圖上箭頭不構成送達或最短路徑保證。

本圖是版本中立的分層概念圖，不畫 header 位元格式，不呈現真實拓撲，不解釋資料如何選路，也不教授任何 Chapter 03 或更後章機制。

## 讀者必須理解

- 兩端固定命名為 `裝置 A`、`裝置 B`；client／server 角色附著於 `本次 localhost HTTP connection`，不是裝置的永久類型。
- 概念要求方向中，A 的來源 IP／來源 port 與 B 的目的 IP／目的 port 是不同層次、不同欄位；port 不能被包進 IP address。
- B 的 `特定服務` 與 `目的 port` 有對應關係，但 port 不是服務本身，也不保證該服務正在執行或可取得。
- packet 是獨立資料卡，分成網路位置欄位、傳輸欄位與所攜內容；它不是一封帶簽收保證的信。
- LAN／WAN 圖只比較相對範圍：LAN 相對有限；WAN 通常跨較大地理範圍並服務更多獨立使用者。沒有單一距離門檻。
- 任一箭頭只表示概念方向或概念前進，不表示實際路徑、最短路徑，也不保證到達、順序、只出現一次或準時。

## 元件

### 圖的固定分區

- `A　端點、角色與欄位`
- `B　packet 是獨立資料單位`
- `C　LAN／WAN 相對尺度`
- 底部 `圖例／推論邊界`

三區必須由標題、留白和外框分開，避免讀者把 localhost connection 畫面誤解成真的跨 WAN 路徑。

### A：端點、角色與欄位

- 左端點框：`裝置 A`
  - 第一列：`網路位置欄位：來源 IP`
  - 第二列：`分開的傳輸欄位：來源 port`
- 右端點框：`裝置 B`
  - 第一列：`網路位置欄位：目的 IP`
  - 第二列：`分開的傳輸欄位：目的 port`
  - 第三列：`特定服務`
- 端點框名稱不得包含 client／server；兩個端點框等寬，欄位列以水平分隔線清楚分層。
- 兩端之間放一個括號標題：`本次 localhost HTTP connection`。
- 上行箭頭由 A 指向 B，文字：`建立這條 connection／概念要求方向`。
  - A 端箭頭徽章：`client：建立這條 connection`。
  - B 端箭頭徽章：`server：接受這條 connection`。
- 下行箭頭由 B 指向 A，文字：`概念回應方向`。
- client／server 徽章只能貼在 connection 的箭頭端點，不得放進裝置框或欄位列。
- A、B 區不顯示任何真實位址、數字、主機名稱或傳輸協定名稱。

### B：獨立 packet 卡

- 一張與端點框分離、外框明顯的卡片，標題 `packet：有限的資料單位`。
- 卡片內固定三層，由上至下：
  1. `網路位置欄位`：左右並列 `來源 IP`、`目的 IP`。
  2. `分開的傳輸欄位`：左右並列 `來源 port`、`目的 port`。
  3. `所攜內容`。
- IP 與 port 所在層必須使用不同列、不同小標和明顯分隔線；不可把 port 縮排在 IP 文字內，也不可把它畫成 IP address 的子欄位。
- packet 卡旁放固定限制標籤：`資料處理單位 ≠ 送達保證`。
- 可用一條短虛線由 A→B 概念要求箭頭指向 packet 卡，標示 `概念拆解`；它不得接續成穿越 LAN／WAN 的單一真實路線。

### C：LAN／WAN 相對尺度

- 左側示例框：`LAN：相對有限區域`，使用實線邊界，內含少量抽象裝置圖形。
- 中央只放一個背景節點：`網路互連位置（本章不展開）`。不使用 router 英文標籤，不畫內部結構或處理規則。
- 右側寬示例框：`WAN：通常較大地理範圍／更多獨立使用者`，使用長虛線邊界，內含至少兩個較小網路群組和較多通用使用者／裝置符號。
- C 區上方共同文字：`相對尺度；無單一距離門檻`。
- C 區下方文字：`WAN 可互連較小網路，但 WAN 不等於 Internet；真實分類仍須看具體網路設計。`
- 由 LAN 示例到互連位置、再到 WAN 示例可放兩段「概念前進」虛線箭頭；兩段必須中斷，不畫成一條固定或最短路線。
- C 區不得聲稱 A／B 的 localhost connection 實際穿越 LAN 或 WAN；必須以分區標題和底部警語明說 C 是獨立尺度示例。

### 圖例／推論邊界

圖底保留四條完整文字，不得只以驚嘆號圖示代替：

1. `角色附著於本次 localhost HTTP connection，不是裝置的永久類型。`
2. `IP 與 port 是分開欄位；port 不能離開 IP 與傳輸脈絡單獨指出完整目的地。`
3. `LAN／WAN 是相對尺度，不能只由距離或故事邊界決定。`
4. `packet 與箭頭只表示概念資料單位／方向；不保證到達、順序、只出現一次、準時或最短路徑。`

## 關係與方向

- A 區的上行要求箭頭固定 A → B，下行回應箭頭固定 B → A。只有上行箭頭兩端帶 client／server 徽章，並用括號把兩行歸入 `本次 localhost HTTP connection`。
- A 的 `來源 IP` 對應 packet 卡的 `來源 IP`；A 的 `來源 port` 對應 packet 卡的 `來源 port`。B 的目的兩欄採相同對應。
- B 的 `目的 port` 以一條短垂直關聯線連到 `特定服務`，線上寫 `指出服務端點`；旁邊加 `不代表服務必然執行`。
- packet 卡與 A→B 箭頭只有 `概念拆解` 關係，不畫 packet 從裝置內「飛出」並保證落入 B。
- C 區的 LAN、互連位置、WAN 只表示相對尺度與可能互連關係，不與 A 區共用實線或編號，不聲稱 localhost 流量走過該路徑。
- 所有方向箭頭旁都需有文字：`概念要求方向`、`概念回應方向` 或 `概念前進`，避免被當成實測路線。

## 版面

- 建議橫式頁寬比例約 2.0:1，最低輸出寬度 1,600 px；保留向量來源供印刷。
- 上半部左側約 68% 放 A，右側約 32% 放 B；下半部橫跨全寬放 C；最底保留全寬圖例框。
- 裝置 A／B 左右對稱，兩條箭頭在中央分列；packet 卡置於右上，不與角色徽章重疊。
- packet 三層欄位排列順序固定，IP 層與 port 層至少以 12 px 留白及 1.5 pt 分隔線區別。
- LAN／WAN 框不按實際公里比例繪製；WAN 框可較寬作輔助，但必須搭配完整文字，不能讓面積成為唯一編碼。
- 閱讀順序：裝置名稱 → connection 角色 → IP／port 分層 → packet 卡 → LAN／WAN 尺度 → 底部推論邊界。
- 不使用地圖背景、衛星照片、道路網、資料中心照片或會讓概念示例看似真實拓撲的素材。
- 如果 Mermaid 草圖無法讓長警語清楚排版，正式 SVG 必須手動調整文字換行，不能刪減正文凍結語意。

## 圖說（caption，正文凍結文字）

**圖 2-2　IP、port 與 packet 的分層概念。**角色附著於本次 localhost HTTP connection；IP 與 port 分層，packet 箭頭不代表送達保證，實際路徑也不保證最短。

## 替代文字（alt text，正文凍結文字）

專業圖：裝置 A 與裝置 B 之間的要求與回應箭頭標示本次 HTTP connection 角色；來源與目的 IP、來源與目的 port 分列，packet 是獨立資料單位，近端 LAN 與跨網路 WAN 範圍另以文字和線型區分。

## 非顏色辨識方式

- A、B、C 分區以字母、完整標題、位置與外框識別。
- 裝置 A／B 以字母與左右位置辨識；角色以箭頭端點的 `client／server` 文字徽章辨識，不靠裝置色彩。
- 要求箭頭為實線，回應箭頭為雙線或點線；兩者都有方向箭頭和完整文字標籤。
- IP 與 port 以不同資料列、列標題、水平分隔線及垂直順序四重區分。
- packet 卡使用獨立粗外框；三個資料層均有完整文字，不以色塊表示欄位種類。
- LAN 使用實線邊界；WAN 使用長虛線邊界；互連位置使用雙線小框。三者都直接寫完整名稱和尺度說明。
- 不送達／非最短路徑限制以完整警語文字呈現，不能只靠紅色、叉號或警告圖示。

## 對比要求

- 一般文字與背景對比至少 4.5:1；大型分區標題至少 3:1。
- 箭頭、欄位分隔線、端點框、packet 外框及 LAN／WAN 邊界與背景對比至少 3:1。
- 主要線寬不小於 2 pt；欄位分隔線不小於 1.5 pt；長虛線在書頁單欄縮圖下仍須可辨識。
- 所有標籤放在純色底或留白區，不能直接壓在相交線條上。
- 色彩只作次要提示；若 IP 與 port 使用不同輔助色，仍必須保留資料列與文字標題。

## 灰階列印

- 轉為 100% 灰階後，要求／回應箭頭的線型、角色徽章、IP／port 資料列、packet 外框、LAN 實線與 WAN 長虛線仍須可辨識。
- 端點框和 packet 卡不得只靠底色深淺區別；各自必須有標題與不同外框樣式。
- `不代表送達保證`、`實際路徑不保證最短`、`無單一距離門檻` 三項警語在單欄縮圖下仍須清楚可讀。
- 正式圖完成後需以實際書頁尺寸做灰階列印／預覽檢查；若虛線或小字消失，應加粗線條或重新排版，不以新增顏色補救。

## 來源與授權

- 內容依據：Chapter 02 凍結正文、`scope-r02.md`、通過的 `body-technical-r02.md`、`bible/source-policy.md` 與 `bible/spec-baseline.md`。
- client／server 角色依據：[RFC 9110 §3.3](https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3)，且只用於本圖的 localhost HTTP connection 情境。
- IPv4／IPv6 最小共同的來源／目的位址模型依據：[RFC 791](https://www.rfc-editor.org/info/rfc791) 與 [RFC 8200](https://www.rfc-editor.org/info/rfc8200)；本圖不畫版本專屬位元格式。
- port 分開傳輸欄位及登錄背景依據：[RFC 6335](https://www.rfc-editor.org/info/rfc6335)、[BCP 165](https://www.rfc-editor.org/info/bcp165) 與 [IANA Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)；本圖不顯示號碼，也不從登錄推論服務可用或可信。
- packet 的版本中立入門模型由正文核准範圍約束；IPv6 packet 的直接來源為 RFC 8200。本圖不增加送達、順序或時效主張。
- LAN／WAN 措辭依據：[NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) glossary；只表達相對有限／通常較大範圍與更多獨立使用者。
- 圖形應由本專案自行繪製。若使用第三方字型、圖示或模板，必須確認可再散布授權，並在 `book/assets/figures/ATTRIBUTION.md` 記錄來源、作者、版本／日期、授權與修改；授權不明者不可使用。
- 若後續使用生成工具，必須另行登記工具、日期、完整 prompt、修改、授權與對應章節；本規格本身不授權開始生圖。
- 禁止讀取、引用、複製或改編 `/home/felix/work/webrtc_story` 的文字、程式碼、動畫與輸出。

## 禁止元素與禁止推論

- 不把 client／server 寫進 `裝置 A`／`裝置 B` 名稱，不把角色畫成永久硬體類型，也不把 HTTP 定義泛化到所有通訊方式。
- 不把 port 畫在 IP address 內，不把 port 畫成實體孔洞、應用程式、全球唯一號碼或服務必然存在的證明。
- 不顯示真實或示例 IP address、port number、主機名稱、URL、可連線目的地或任何個資。
- 不把 packet 畫成完整檔案、已簽收信件、固定大小方格、保證成功的動畫或單一路徑上的連續車隊。
- 不用打勾、抵達旗或無警語的箭頭暗示 packet 一定送達、依序、只出現一次或準時。
- 不把 LAN／WAN 只用距離、行政線或故事邊界分類，不把 WAN 畫成 Internet 的同義詞；不宣稱同棟建築必然只有一個 LAN。
- 不畫一條看似最短的固定路線，不以直線長度或地圖距離表示真實路徑；互連位置不顯示內部行為。
- 不出現 router 的獨立術語教學；若後續因排版需要保留，只能併列為 `網路互連位置（本章不展開）` 的背景括註，且不得增加評量負擔。
- 不出現 Chapter 03 或更後章的技術名稱、縮寫、機制或設備；禁止位址轉換、政策閘門、具體傳輸協定、握手、重傳、WebRTC signaling、ICE、STUN、TURN、SDP、安全機制、媒體協定、codec、packetization 或 stats。
- 不用圖例、caption 或 alt text新增正文未通過 Gate 的技術主張；不讀取或改編排除專案素材。
