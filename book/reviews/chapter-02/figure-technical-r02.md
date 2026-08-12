Gate: figure_technical
Round: 2
Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69
Artifact-Set-SHA256: c6a76a305a02b8c6c12f1bcc2c2bc5975101169b3272c7cf1242b41f974c8a1d
Result: GATE PASS

# Chapter 02 正式候選圖技術審查 r02

## 審查範圍與 hash

- 綁定正文：`.work/chapter-02/draft-r03.md`；重算 SHA-256 與 Content-SHA256 一致。
- 新候選：`metadata-r03.md`、未修改的 `story-spec-r01.md`／`story-r02.mmd`／`story-r02.svg`、未修改的 `technical-spec-r01.md`、更新的 `technical-r03.mmd`／`technical-r03.svg`。
- 實際查看：`.work/chapter-02/figures/technical-r03.png` 原始 1,784×980 預覽；story-r02 位元內容與 r01 Gate 綁定檔相同，因此只回歸其 hash 與既有通過項。
- 對照：`figure-technical-r01.md` 的唯一阻擋、兩份核准圖規格、`body-technical-r02.md`、正文 caption／alt、scope 與 `bible/spec-baseline.md`。
- 未修改任何受審檔，也未讀取排除專案。

七檔正式路徑 mapping 與重算 SHA-256：

| 未來正式路徑 | 受審檔 SHA-256 |
|---|---|
| `book/assets/figures/chapter-02-figure-metadata.md` | `2a749bd0ffbbc2c7e8cd168304968395d2fe57a29ce9c6611fa41e4992d6a65c` |
| `book/figures/story/chapter-02-address-and-range-spec.md` | `d5ee82f21c4942ed205abdb88e48361e15cb16f07d185a8897447758d80f7596` |
| `book/figures/story/chapter-02-address-and-range.mmd` | `4c8c7632434bdfe8bd3defdb3e3dc357594d01ecb6664f862c990c8b691d7bc6` |
| `book/figures/story/chapter-02-address-and-range.svg` | `a0f3dd56e41d8aa994afc6d8f9a551c9f088ffe65108c4e434b8a78a7821f804` |
| `book/figures/technical/chapter-02-ip-port-packet-spec.md` | `f18726cacb753aa01daf4977bdc967690a404b70c3a44fafe033fa9b931ee585` |
| `book/figures/technical/chapter-02-ip-port-packet.mmd` | `009f9622d99a6c99a264cee69fc771233b9822d5a0c093ee12ac005957329001` |
| `book/figures/technical/chapter-02-ip-port-packet.svg` | `1d8ef64385f4aa3b2df34cef22a44c980198c7a77591048aa47ca1a72970d917` |

依 `scripts/validate_kit.py::artifact_set_sha256` 的正式 `file` 排序與 compact JSON 正規化方式獨立計算，得到 header 所列 artifact-set hash，與主代理提供值完全一致。

## r01 唯一阻擋回歸

位置：`technical-r03.mmd:31-40`、`technical-r03.svg` packet 卡、`technical-r03.png` 右上 B 區，以及 `metadata-r03.md:12-18,48-66`。

- `technical-r02.mmd` 到 `technical-r03.mmd` 的 diff 只有兩處：第 37 行 `P_IP --> P_PORT` 改為 `P_IP ~~~ P_PORT`，第 38 行 `P_PORT --> P_CONTENT` 改為 `P_PORT ~~~ P_CONTENT`。其他節點、文字、有意義的箭頭與技術主張未變。
- 新 SVG 中對應 `L_P_IP_P_PORT_0`、`L_P_PORT_P_CONTENT_0` 均為 Mermaid `edge-thickness-invisible` layout edge，沒有可見 arrowhead；原尺寸 PNG 也確認 packet 卡只以垂直排列、留白和各自框線呈現「網路位置欄位／分開的傳輸欄位／所攜內容」，兩支阻擋箭頭已消失。
- 因此新 artifact 不再暗示 `network → transport → content` 的處理順序或資料流，符合核准規格 `technical-spec-r01.md:63-70,91-98,105` 的三層欄位與箭頭語意要求。
- `metadata-r03.md` 正確揭露唯一修正、renderer、尺寸與新候選檔名，也明說 `~~~` 只作不可見 layout 關係；metadata 與 MMD、SVG、PNG 實際結果一致。

## 其餘通過項快速回歸

- **HTTP connection 角色：通過。**技術圖仍只把 A client（建立）／B server（接受）綁在「本次 localhost HTTP connection」，概念回應 B→A；裝置 A／B 名稱沒有永久角色。生活圖兩條反向 connection 的建立／接受角色及「不泛化到所有通訊方式」仍保持 r01 已通狀態。
- **LAN／WAN 相對尺度：通過。**兩圖仍使用 LAN「相對有限」、WAN「通常較大範圍／更多獨立使用者」、無單一距離門檻與 WAN≠Internet；故事行政線不能取代分類。技術圖 C 區仍明說與上方 localhost connection 分開，不把示例當真實拓撲。
- **IP／port：通過。**來源／目的 IP 與來源／目的 port 維持不同欄位框；port 指向特定服務時仍標示服務不代表必然執行，圖例保留 IP 與傳輸脈絡限制。沒有真實位址、port number、URL 或可連線目的地。
- **packet／箭頭／路徑：通過。**packet 卡維持「獨立、有限資料單位」及「資料處理單位 ≠ 送達保證」；其內已無方向箭頭。其餘可見箭頭均有服務關係、概念要求／回應或概念前進標籤；圖例明說不保證到達、順序、一次性、準時或最短路徑。
- **Chapter 03+ 邊界：通過。**沒有 private/public IP、NAT、firewall、UDP/TCP、router 內部、WebRTC signaling、ICE／STUN／TURN、SDP、安全、媒體、codec、packetization 或 stats 偷渡。
- **Caption／alt／SVG：通過。**metadata caption／alt 與正文凍結文字一致。兩份 SVG 均有 `role="graphics-document document"`、`aria-roledescription="flowchart-v2"` 以及引用實際存在 title／desc id 的 `aria-labelledby`／`aria-describedby`；title／desc 與各自 MMD `accTitle`／`accDescr` 一致，desc 逐字等於對應 alt。
- **正式圖範圍：通過。**新技術圖沒有新增或錯誤技術主張；story artifact 的 spec／MMD／SVG hash 與 r01 相同。本結論不替代獨立 accessibility Gate 對實際書頁尺寸、對比與灰階的裁決。

## 結論

r01 唯一阻擋已在 source、SVG 與實際 PNG 中完整移除；packet 卡現在只呈現核准的欄位分層，不再暗示未定義處理流程。其餘已通過的角色、相對尺度、IP／port、packet／路徑、ARIA 與後章邊界均未退步，更新後正式候選圖通過技術 Gate。
