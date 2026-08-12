# Chapter 03 專業圖規格 r01

Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6

> 對應正文：`.work/chapter-03/draft-r02.md`
> 正文技術 Gate：`.work/chapter-03/reviews/body-technical-r02.md`，GATE PASS
> 圖片狀態：規格草案；尚未生成 Mermaid、SVG 或其他正式圖。
> 預定正式規格路徑：`book/figures/technical/chapter-03-mapping-policy-transport-spec.md`
> 預定正式圖片路徑：`book/figures/technical/chapter-03-mapping-policy-transport.svg`

## 目的

用一張上下分區的專業概念圖完成兩件事，且不互相偷渡主張：

1. 上半部把 RFC 1918 private IPv4 host、NAT／NAPT mapping、獨立 firewall policy 與 outside network 分層，並把 `E` 嚴格定義為觀察位置相關的 outside observed address；只有另有 global-realm 證據時，才可另外標示 public IP address。
2. 下半部分開比較 UDP datagram 與 TCP reliable in-order byte-stream service semantics；此比較面板不連入上半部 NAT 拓撲，因此不宣稱 TCP-through-NAT 行為。

本圖是入門分層與比較圖，不是產品 mapping table、實際封包格式、實測網路拓撲、性能 benchmark 或 WebRTC flow。

## 讀者必須理解

- Private host、mapping、policy 與 outside network 是四個不同層次；NAT／NAPT 的 mapping evidence 不能替代 firewall policy evidence。
- Mapping 範例只限 RFC 4787 及其更新採用範圍：單播 UDP、內外均只談 IPv4 的 Traditional NAT 教學情境。
- Address-only NAT 只改來源 address 表示；NAPT 案例同時改來源 address 與 UDP port。兩個案例是同一輸入 tuple 的平行對照，不是依序先 NAT 再 NAPT。
- `E` 只代表特定觀察位置看到的 outside observed address。`E` 可能仍不是 public IP address；「在圖右側」「不屬 RFC 1918」或「經過 NAT」都不足以證明 public/global realm。
- 即使另有 registry allocation／global uniqueness evidence，使 `E` 可另標 public IP address，仍不保證 route、policy 放行、listener 存在或實際可達。
- UDP 面板保留 datagram 邊界並表示可能遺失／重排；TCP 面板在 connection establishment 後呈現 reliable in-order byte stream，且不保留應用 message boundary。
- 下半部只比較 transport service；不畫「UDP 快／TCP 慢」，也不把 TCP 面板連進上半部 mapping table。

## 元件

### 固定分區與圖例

- 圖頂標題：`Address 表示、mapping、policy 與 transport 語意分層`
- 上半部：`A　IPv4 Traditional NAT 的受限 UDP mapping 與獨立 policy`
- 下半部左：`B1　UDP datagram service`
- 下半部右：`B2　TCP byte-stream service`
- 最底部：`符號與推論邊界`
- A、B1、B2 必須以完整標題、外框與留白分開；B2 不得與 A 共用箭頭或 tuple。

### A：Private host 到 outside network

- 左端點框：`RFC 1918 private IPv4 host`
  - 固定來源表示：`10.0.0.8:49152`
  - 傳輸標籤：`UDP（單播教學 tuple）`
  - 目的欄：`目的 address:port（兩案例保持不變）`
- 中左獨立框：`NAT／NAPT mapping table（教學表示，不是產品格式）`
  - 表頭固定為：`案例`、`內側來源表示`、`外側來源表示`、`transport`、`目的欄`。
  - 案例 1：
    - `Address-only NAT`
    - `10.0.0.8:49152`
    - `E:49152`
    - `UDP`
    - `保持不變`
  - 案例 2：
    - `NAPT（address + port）`
    - `10.0.0.8:49152`
    - `E:62000`
    - `UDP`
    - `保持不變`
  - 表底固定警語：`兩列是平行教學案例，不是串聯處理；實際 key、方向、refresh 與 lifetime 依規範範圍及實作而異。`
- 中右獨立框：`Firewall policy boundary`
  - 輸入文字：`另查對應方向與條件`
  - 結果一：`允許：可繼續到 outside network`
  - 結果二：`阻擋：在 policy boundary 停止`
  - 框旁固定文字：`mapping record ≠ policy evidence`
- 右端點框：`Outside network／觀察位置`
  - 核心符號卡：`E = outside observed address／外側觀察位址`
  - 緊接限制：`依觀察位置而定；E ≠ 自動成為 public IP address`
  - 條件性旁註，以虛線證據括號而非主流程表示：`只有另有 registry allocation／global uniqueness evidence，才可在 E 旁另標 public/global realm。`
  - 第二行：`即使已確認 global uniqueness，仍不保證 route、policy、listener 或可達性。`

### B1：UDP datagram service

- 輸入側至少四個分離、有完整外框的 datagram 卡，標 `D1`、`D2`、`D3`、`D4`。
- 每張卡保持自己的邊界；標題文字：`message/datagram boundary 保留`。
- 中段用一個空缺虛線卡標 `可能遺失`，出口順序用 `D1、D3、D2` 標 `可能重排`。
- 固定限制：`不內建 delivery、duplicate protection 或 ordering 保證；應用仍有壅塞責任。`
- 不畫 mapping table、firewall、NAT、outside E 或速度數值。

### B2：TCP byte-stream service

- 起點狀態框：`Connection establishment`，其後才畫 stream。
- 輸入側用連續 byte 列表示應用資料，可用兩組不同位置的細刻度示意 send boundaries。
- 中段為連續紙帶／byte stream，不畫獨立 packet 卡；出口文字：`reliable、in-order byte stream`。
- 接收側刻度位置須與輸入 send boundaries 不同，或直接移除分隔，旁標 `不保留 application message boundary`。
- 固定限制：`若無法維持，connection 仍可能失敗；不表示立即抵達、應用已處理或具身分／機密性保證。`
- 面板頂端明寫：`只教 TCP service semantics；不宣稱 TCP-through-NAT 行為。`

### 符號與推論邊界

圖底保留以下完整文字：

1. `E 只表示 outside observed address；圖面位置與非 RFC 1918 都不足以證明 public IP address。`
2. `Mapping 與 firewall policy 是獨立 evidence；mapping 不等於放行，放行不等於 listener 存在。`
3. `UDP mapping table 只是一筆單播、IPv4-to-IPv4 Traditional NAT 教學表示，不是產品格式或所有 NAT 行為。`
4. `UDP／TCP 面板只比較 service semantics，不比較速度；TCP 面板與 NAT mapping 無連線主張。`

## 關係、方向與箭頭

- A 區主閱讀方向為左至右：private IPv4 host → mapping table → `另查` firewall policy → 允許分支 → outside network。
- Private host 到 mapping table 使用兩條由同一輸入分叉的箭頭，分別標 `案例 1：address-only NAT` 與 `案例 2：NAPT`；兩條箭頭不得首尾相接。
- Mapping table 到 policy boundary 的箭頭標 `有 mapping 後仍須獨立判斷 policy`，不可使用成功勾。
- Policy 的允許分支使用尖頭實線箭頭連到 outside；阻擋分支使用平頭終止線。兩者都有完整文字，不以綠／紅顏色代替。
- `E` 卡位於 outside observation 內。`registry allocation／global uniqueness evidence` 使用細虛線括號連到條件標籤，不屬於 packet/data path，也不能畫成 NAT 自動產生的屬性。
- B1、B2 各自左至右；A 與 B 之間不畫箭頭。B1 與 B2 之間只放 `service-semantics comparison` 雙向括號，不畫 fallback、選路或競速箭頭。
- 所有上半部箭頭代表教學資料關係與判斷順序，不代表真實裝置必定分離、固定物理路徑、最短路徑或成功到達。

## 版面

- 建議橫式比例約 2.0:1，正式 SVG viewBox 至少對應 2,000 × 1,100；保留向量來源供印刷。
- 上半部 A 約佔 60% 高度：private host 18%、mapping table 36%、policy 20%、outside 26% 的水平寬度參考。
- 下半部 B1／B2 各約一半寬度，外框等大、標題同層級；不得用面積或位置暗示優劣。
- Mapping table 的五欄在單欄書頁縮圖仍須可讀；若空間不足，允許把案例 1／2 改成上下兩張等寬卡，但欄位與「平行案例」警語不可刪除。
- `E` 的定義、非 public 警語與條件性 public/global 標籤應形成三層文字階層，不能擠成一行或靠 tooltip。
- 閱讀順序：A 標題 → private host → 平行 mapping 案例 → policy 兩結果 → E 定義／條件 → B1 → B2 → 四條推論邊界。
- 不使用地圖、真實路由器 UI、封包擷取、產品 NAT table、速度圖或可能被誤認為實測 topology 的背景。

## 做到／做不到

| 圖中元素 | 做到 | 做不到 |
|---|---|---|
| NAT mapping 案例 | 分開 address-only NAT 與 address+port NAPT | 不表示所有 NAT 都改 port、兩案例依序發生或 mapping 永久 |
| Firewall policy | 以獨立條件產生允許／阻擋 | 不建立 mapping、不因 mapping 存在而自動放行 |
| E | 表示特定 observation point 的 outside observed address | 不自動表示 public/global realm、永久身分或可達性 |
| 條件性 public 標籤 | 只在另有 registry allocation／global uniqueness evidence 時附加 | 不由圖面右側、非 RFC 1918 或 NAT 輸出推論 |
| UDP 面板 | 表達 datagram boundary 與非保證 | 不支持普遍 loss rate、速度、NAT 穿越或 WebRTC 選路 |
| TCP 面板 | 表達 connection-oriented reliable in-order byte stream | 不主張 TCP-through-NAT、不保留 message boundary、不保證永不失敗或一定較慢 |

## 圖說（caption，正文凍結文字）

**圖 3-2　Address 表示、mapping、policy 與 transport 語意分層。**Mapping table 只是一筆受控單播 UDP、內外都只談 IPv4 的 Traditional NAT 教學表示，不是產品表格格式；外側觀察位址 E 與 public/global realm 分開，firewall evidence 另列，TCP 時間線只教 transport service，不宣稱 TCP-through-NAT 行為。

## 替代文字（alt text，正文凍結文字）

專業圖：由左至右依序是 RFC 1918 private IPv4 host、獨立的 NAT 或 NAPT mapping table、獨立的 firewall policy boundary、outside network；表中以一筆 UDP 教學 tuple 分別示意 address-only NAT 與 address-plus-port NAPT，外側欄以 E 標示觀察位置相關的 outside observed address，並註明只有另有證據確定屬 public/global realm 才可另標 public IP address；下半部以分離時間線呈現 UDP datagram 邊界及可能遺失重排，與 TCP connection establishment 後的 reliable in-order byte stream，且不畫速度排名。

## 非顏色辨識方式

- A、B1、B2 以代號、完整標題、位置、留白與外框辨識。
- Private host 使用端點框；mapping 使用五欄表格；policy 使用雙結果決策框；outside 使用 `E` 符號卡。四者形狀與文字動詞不同。
- NAT／NAPT 平行案例用 `案例 1`／`案例 2`、分叉線與完整名稱辨識，不只靠兩種顏色。
- Allow 使用尖頭實線；block 使用平頭終止線；兩者直接標 `允許`／`阻擋`。
- `E ≠ public` 使用完整不等式文字；條件性 public/global evidence 使用虛線括號與 `只有…才可` 句，不用綠勾。
- UDP 使用分離且編號的 datagram 卡；TCP 使用 establishment 狀態框加連續 byte strip。線型、形狀與文字三重區分。

## 對比要求

- 一般文字與背景對比至少 4.5:1；大型標題至少 3:1。
- 箭頭、外框、表格線、終止線、datagram 卡與 byte strip 對背景至少 3:1。
- 主箭頭和模組外框不小於 2 pt；表格線與 evidence 虛線不小於 1.5 pt；縮至單欄時仍可分辨尖頭／平頭與實線／虛線。
- 標籤只能置於純色底或充分留白處，不得壓在線條交叉、漸層、照片或紋理上。
- 色彩只作次要分區提示；不得承擔 NAT/NAPT、mapping/policy、allow/block、E/public 或 UDP/TCP 的唯一辨識。

## 灰階列印

- 轉為 100% 灰階後，四個 A 區模組、兩個 mapping 案例、policy 兩結果、E 定義及 B1/B2 仍須由標題、形狀、線型與位置辨識。
- 表格列、分叉線、allow 箭頭、block 終止線、global-evidence 虛線括號在實際單欄寬度下不得合併或消失。
- UDP 的分離卡／空缺／重排序號與 TCP 的 establishment／連續 strip／不同 boundary 刻度皆須清楚。
- 四條推論邊界在單欄縮圖仍可讀；若灰階預覽失敗，調整線寬、留白或版面，不用新增顏色補救。
- 正式圖完成後須如實記錄人工灰階與縮圖預覽；沒有像素儀器時不得宣稱已量測實際對比值。

## SVG ARIA 與閱讀順序

- SVG 根元素使用 `role="img"`、`aria-labelledby="ch03-tech-title ch03-tech-desc"`。
- `<title id="ch03-tech-title">` 建議為 `IPv4 mapping、獨立 firewall policy 與 UDP／TCP 服務語意`。
- `<desc id="ch03-tech-desc">` 必須逐字採用上方凍結 alt text。
- DOM／輔助科技閱讀順序固定為：全圖標題 → A 區 private host → NAT/NAPT 平行案例 → policy allow/block → E 與條件性 public evidence → B1 UDP → B2 TCP → 推論邊界。
- 純裝飾底色、陰影、分隔線與重複圖示設 `aria-hidden="true"`；必要的表格標頭、箭頭標籤、E 定義與警語不能隱藏。
- SVG 不加入動畫、閃爍、tab stop、hover-only tooltip 或以互動才能取得的資訊；所有關係必須靜態可讀。

## 來源與授權

- 內容依據：凍結正文 `.work/chapter-03/draft-r02.md`、通過的 `body-technical-r02.md`、`scope.md`、`bible/source-policy.md`、`bible/characters.md` 與 `bible/style.md`。
- RFC 1918 private IPv4 範圍依 [RFC 1918／BCP 5](https://www.rfc-editor.org/info/rfc1918)。
- NAT/NAPT、address realm、public/global realm 與 mapping 術語依 [RFC 2663](https://www.rfc-editor.org/info/rfc2663) 及正文採用邊界。
- 具體 mapping 案例只依 [RFC 4787／BCP 127](https://www.rfc-editor.org/info/rfc4787) 及其 [RFC 6888](https://www.rfc-editor.org/info/rfc6888)、[RFC 7857](https://www.rfc-editor.org/info/rfc7857) 更新所限定的單播 UDP、IPv4-to-IPv4 Traditional NAT 範圍。
- Firewall 的有限 policy 模型依 [NIST SP 800-41 Rev. 1](https://csrc.nist.gov/pubs/sp/800/41/r1/final)。
- UDP 服務語意依 [RFC 8085／BCP 145](https://www.rfc-editor.org/info/rfc8085)；TCP 服務語意依 [RFC 9293／STD 7](https://www.rfc-editor.org/info/rfc9293)。
- `E` 不是實際位址或 IANA 登錄值；它是正文定義的符號。Public/global 條件與 special-purpose 負向邊界依 RFC 2663 §2.7 及 [IANA IPv4 Special-Purpose Address Space](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)。
- 圖形、表格與符號應由本專案自行繪製，不使用真實設備 UI、實際 mapping table、真實位址、封包擷取或授權不明圖示。
- 若使用第三方字型、圖示或模板，須確認可再散布授權，並在 `book/assets/figures/ATTRIBUTION.md` 記錄來源、作者、版本／日期、授權與修改；授權不明者不可使用。
- 若後續使用生成工具，須另記工具、日期、完整 prompt、修改與授權；本規格不授權開始生圖。
- 禁止讀取、引用、複製或改編排除專案的文字、程式碼、動畫或輸出。

## 禁止元素與禁止推論

- 不把 NAT/NAPT mapping 與 firewall policy 合併成單一 box、箭頭、顏色或成功狀態；不以 mapping record 代替 policy evidence。
- 不把案例 1／2 畫成先後步驟，不把所有 NAT 都畫成改 port，不顯示 endpoint-independent/dependent、hairpinning、timeout 數值、CGN 細節、TCP NAT state 或 IPv6 NAT。
- 不把 `E` 標成 public IP、Internet-reachable、可信、永久或 endpoint identity；不以右側位置、地球圖示、雲朵、非 RFC 1918 或 NAT output 暗示 public/global。
- 不用真實或文件用途 IP 冒充 public 位址；除正文核准的 `10.0.0.8:49152`、`E:49152`、`E:62000` 教學符號外，不新增 address/port 數值。
- 不將 TCP panel 接到 mapping table、firewall 或 outside E；不聲稱 TCP-through-NAT、TCP fallback、WebRTC 選用 TCP 或 TCP 必然較慢。
- 不把 UDP 畫成保證 loss/reorder、完全無 state、必然更快或無壅塞責任；不把 TCP 畫成 packet 不會遺失、message boundary 保留、永不失敗、立即抵達或具安全／授權保證。
- 不畫產品 UI、router internals、真實 firewall rules、封包 header bits、DNS、route selection、性能曲線、latency 數值或實測結論。
- 不出現 Chapter 04+ 的 camera/microphone API、PeerConnection、signaling、offer/answer、SDP、ICE、candidate、STUN、TURN、DTLS/SRTP、RTP/RTCP、codec、packetization、jitter、congestion、stats、Node、Wireshark、RTSP、MediaMTX、FFmpeg 或 WHEP。
- 不讓 caption、alt、圖例、ARIA description 或圖形新增正文 Gate 未通過的技術主張。
