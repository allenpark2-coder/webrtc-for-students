Gate: figure_accessibility
Round: 2
Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69
Artifact-Set-SHA256: c6a76a305a02b8c6c12f1bcc2c2bc5975101169b3272c7cf1242b41f974c8a1d
Result: GATE PASS

# Chapter 02 正式候選圖無障礙審查 r02

## 重審原因與受審範圍

- r01 accessibility evidence 綁定舊 r02 artifact；其後 figure technical r01 發現 technical packet 卡內兩支未定義方向箭頭，因此舊 artifact 未通過整體圖 Gate。
- 本輪綁定新候選：`.work/chapter-02/figures/metadata-r03.md`、未修改的 `story-spec-r01.md`／`story-r02.mmd`／`story-r02.svg`、未修改的 `technical-spec-r01.md`、更新的 `technical-r03.mmd`／`technical-r03.svg`。
- 綁定正文 `.work/chapter-02/draft-r03.md`；重算 SHA-256 為 `a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69`，與 header 一致。
- 實際目視預覽：`story-r02.png`（1,784×862）與 `technical-r03.png`（1,784×980）。兩份 PNG 只供人工檢視，不列入正式 artifact set。
- 另將兩份 PNG 等比例縮至 1,280 px 寬，並各自產生 100% 灰階代理供螢幕人工預覽；暫存檔已清除，未修改任何 artifact。
- 前置技術 Gate：`.work/chapter-02/reviews/figure-technical-r02.md` 已對同一正文及 artifact-set hash PASS。本 Gate 獨立檢查可讀性與可存取性，不以技術 Gate 代替目視判斷。

## 七檔正式 mapping 與 artifact set

| 候選來源 | 未來正式路徑 | SHA-256 |
| --- | --- | --- |
| `.work/chapter-02/figures/metadata-r03.md` | `book/assets/figures/chapter-02-figure-metadata.md` | `2a749bd0ffbbc2c7e8cd168304968395d2fe57a29ce9c6611fa41e4992d6a65c` |
| `.work/chapter-02/figures/story-spec-r01.md` | `book/figures/story/chapter-02-address-and-range-spec.md` | `d5ee82f21c4942ed205abdb88e48361e15cb16f07d185a8897447758d80f7596` |
| `.work/chapter-02/figures/story-r02.mmd` | `book/figures/story/chapter-02-address-and-range.mmd` | `4c8c7632434bdfe8bd3defdb3e3dc357594d01ecb6664f862c990c8b691d7bc6` |
| `.work/chapter-02/figures/story-r02.svg` | `book/figures/story/chapter-02-address-and-range.svg` | `a0f3dd56e41d8aa994afc6d8f9a551c9f088ffe65108c4e434b8a78a7821f804` |
| `.work/chapter-02/figures/technical-spec-r01.md` | `book/figures/technical/chapter-02-ip-port-packet-spec.md` | `f18726cacb753aa01daf4977bdc967690a404b70c3a44fafe033fa9b931ee585` |
| `.work/chapter-02/figures/technical-r03.mmd` | `book/figures/technical/chapter-02-ip-port-packet.mmd` | `009f9622d99a6c99a264cee69fc771233b9822d5a0c093ee12ac005957329001` |
| `.work/chapter-02/figures/technical-r03.svg` | `book/figures/technical/chapter-02-ip-port-packet.svg` | `1d8ef64385f4aa3b2df34cef22a44c980198c7a77591048aa47ca1a72970d917` |

依未來正式 `file` 排序，每項只保留 `file`／`sha256`，使用 `scripts/validate_kit.py::artifact_set_sha256` 的 compact JSON 正規化方式重算，結果為 `c6a76a305a02b8c6c12f1bcc2c2bc5975101169b3272c7cf1242b41f974c8a1d`，與 header 及主代理指定值一致。任一檔案或正式路徑變更都會使本 Gate 失效。

## r03 修正的無障礙回歸

- `technical-r03` 只把 packet 卡內 `網路位置欄位 → 分開的傳輸欄位 → 所攜內容` 之間兩支可見方向箭頭改為不可見 layout 關係；節點文字、垂直排列、外框、留白、caption、alt、title、desc 與其他有語意線條均未改。
- 原尺寸 PNG 與 1,280 px 縮圖確認：兩支箭頭已消失，三個框仍能由 B 區標題、上下位置、完整欄位名稱與共同粗外框讀成 packet 的三項組成；移除箭頭沒有造成框線斷裂、文字位移、重疊或閱讀順序不明。
- 對螢幕閱讀器而言，SVG desc 本來就只描述 IP／port 分列與 packet 獨立資料單位，不宣稱 packet 內部處理方向；新 render 與 desc 的關係因此更一致。
- 對低視力／灰階閱讀者而言，組成關係不依靠箭頭或顏色；區名 B、外框、位置與文字仍完整，無需以新增色彩補償。

## Caption 與 alt text 逐字一致性

### 圖 2-1

- 正文 Markdown alt、`metadata-r03.md`、`story-spec-r01.md`、`story-r02.mmd` 的 `accDescr` 與 `story-r02.svg` 的 `<desc>` 逐字一致。
- 正文 caption、metadata 與 spec 逐字一致。
- Alt 完整描述左右相對尺度、地址與服務入口、角色交換及沒有單一距離門檻；caption 補充尺度非距離公式、角色只屬 localhost HTTP connection。兩者都不要求以顏色辨認關係。

### 圖 2-2

- 正文 Markdown alt、`metadata-r03.md`、`technical-spec-r01.md`、`technical-r03.mmd` 的 `accDescr` 與 `technical-r03.svg` 的 `<desc>` 逐字一致。
- 正文 caption、metadata 與 spec 逐字一致。
- Alt 描述 A／B 要求與回應、IP／port 分列、獨立 packet，以及 LAN／WAN 文字與線型；caption 補足 localhost HTTP 範圍、非送達保證與非最短路徑。移除 packet 內箭頭後，兩者沒有描述圖中不存在的內部方向。

## SVG title、desc 與 ARIA

- `story-r02.mmd` 與 `technical-r03.mmd` 都有非空 `accTitle`、`accDescr`。
- 兩份根 `<svg>` 均含 `role="graphics-document document"`、`aria-roledescription="flowchart-v2"`、`aria-labelledby` 與 `aria-describedby`。
- 每份 SVG 的 `<title id="chart-title-my-svg">`、`<desc id="chart-desc-my-svg">` 各只有一個；根元素的 ARIA 引用逐一指向實際存在且正確的 id，無遺失或交叉。
- 生活圖 title 為「地址、入口、相對範圍與 connection 角色」；專業圖 title 為「IP、port 與 packet 的分層概念」。兩份 desc 逐字等於對應正文 alt。
- Markdown alt 與 SVG title／desc 同時存在，可分別服務嵌入文件及單獨開啟 SVG 的情境。

## 實際預覽、文字密度與橫式單欄可讀性

### 生活圖 story-r02

- 原尺寸圖無裁切、重疊、框線穿字或箭頭遮字；A 地址／入口、B 相對尺度、C 角色交換與三欄推論邊界均可定位。
- 1,280×618 橫式單欄代理中，標題、LAN 實線、WAN 長虛線、地址→入口、兩條 connection 的建立／接受角色及底部警語仍可讀。
- 文字集中於明確分區與警語框，沒有以超長段落取代 alt；視線可依 B→A→圖例→C 的實際排版逐區閱讀，資訊密度可接受。

### 專業圖 technical-r03

- 原尺寸圖無裁切、重疊、框線穿字或節點溢出；A 端點、B packet、四項推論邊界與 C 相對尺度示例維持清楚間隔。
- 1,280×704 橫式單欄代理中，A／B、來源／目的 IP 與 port、特定服務、packet 三層文字、四欄警語、LAN 實線／WAN 長虛線仍可讀。
- Packet 卡兩個箭頭移除後留白增加，沒有降低欄位辨識，反而避免視覺上誤認處理次序。
- 專業圖文字密度較高，但分區、完整標題、粗外框、欄位框與留白提供足夠 chunking；未發現需阻擋的極小字、碰撞或無法追蹤的線路。

「單欄可讀」以使用者指定的 1,280 px 橫式縮圖代理為本輪門檻。若最終書頁使用更窄欄、替換字型、重新 render 或點陣化，必須以實際出版尺寸重做 Gate；本次 PASS 不代表可任意縮小。

## 非顏色辨識

### 生活圖

- A／B／C 以區號、標題、位置與外框辨識。
- 地址與入口以文字及連續步驟箭頭辨識；不需顏色判斷順序。
- LAN 有實線框，WAN 有長虛線框，兩者也直接寫出完整名稱與尺度。
- 兩條 connection 以編號、相反方向及 `client（建立）`／`server（接受）` 文字共同區分。
- 三項限制使用完整句子，沒有只靠警告色、叉號或圖示。

### 專業圖

- A／B／C、裝置 A／B、packet、LAN／WAN 都有區名、標題、位置與獨立外框。
- IP 與 port 是不同資料框、不同列標題與不同位置；packet 以共同粗框包住三項文字。
- 要求／回應使用實線／點線、箭頭方向及文字；服務關係與概念前進也有標籤。
- LAN 使用實線，WAN 使用長虛線，互連位置使用獨立框；四項邊界以編號和完整文字呈現。
- r03 移除的只是未定義 packet 內箭頭；三層仍以文字、垂直次序與框線辨識，不造成色彩依賴。

兩圖即使移除色相，分類、方向與推論邊界仍有至少一種文字線索及一種形狀／線型／位置線索。

## 對比與灰階

- 新舊兩 SVG 實際宣告的主要色值不變：`#ffffff` 白底、`#f3f4f6` 淺灰底、`#111827` 近黑文字、`#1f2937`／`#374151` 深色框線。
- 依 SVG 宣告色值套用 WCAG 相對亮度公式：`#111827` 對白底約 17.74:1、對淺灰底約 16.12:1；`#1f2937` 對白底約 14.68:1；`#374151` 對白底約 10.31:1、對淺灰底約 9.37:1。文字組合高於 4.5:1，圖形／框線組合高於 3:1。
- 這些數字是 source-level 色值計算，不是對 PNG 或印刷品進行校準像素儀器測量。
- 人工查看 1,280 px 的 100% 灰階螢幕預覽後，兩圖的標題、框線、LAN 實線、WAN 長虛線、connection／要求／回應方向、IP／port 分列、packet 卡與警語仍可辨識。
- 本輪未做實體灰階列印，也未使用校準儀器；最終紙張、墨色、印表機或出版轉檔不同時，仍需製作實體或最終 PDF proof。

## 結論

新七檔 candidate 的正式 mapping、個別 hash 與 artifact-set hash 已重算一致。正文 alt／caption、metadata、spec、MMD 與 SVG 可存取資訊逐字對齊；title／desc／ARIA 完整。Story-r02 與 technical-r03 在原尺寸、1,280 px 橫式單欄代理及人工灰階預覽中均無裁切、重疊或不可讀退步，且不依賴色彩傳達分類與方向。Technical-r03 移除 packet 內未定義箭頭後仍保留清楚的文字與分區結構，因此新候選通過 Figure Accessibility Gate。
