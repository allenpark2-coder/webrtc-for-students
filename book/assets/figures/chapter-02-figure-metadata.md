# Chapter 02 Mermaid 圖稿 metadata r03

Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69

> 對應正文：`.work/chapter-02/draft-r03.md`
> 核准規格：`story-spec-r01.md`、`technical-spec-r01.md`
> 圖規格技術 Gate：`.work/chapter-02/reviews/figure-spec-technical-r01.md`，GATE PASS
> 本輪候選：`story-r02.mmd/.svg/.png` ＋ `technical-r03.mmd/.svg/.png`
> r01、story-r02 與 technical-r02 均保留；本輪沒有修改正文或 spec。
> 狀態：待正式圖 artifact technical 與 accessibility Gate；本檔不代替兩個 Gate。

## r03 唯一修正

- `story-r02.*` 完全未修改。
- `technical-r03.mmd` 從 `technical-r02.mmd` 建立，只把 packet 卡內兩個有向關係改成無方向、不可見的 Mermaid layout 關係：
  - `P_IP --> P_PORT` 改為 `P_IP ~~~ P_PORT`。
  - `P_PORT --> P_CONTENT` 改為 `P_PORT ~~~ P_CONTENT`。
- 目的只是移除可能被讀成 packet 內部處理順序或資料流向的箭頭；節點、文字、位置關係、caption、alt、其他箭頭與全部技術主張均未變更。

## Renderer、尺寸與輸出

- Renderer：`@mermaid-js/mermaid-cli` 11.16.0，以固定版本 `npx --yes @mermaid-js/mermaid-cli@11.16.0` 執行。
- 未安裝 repo-local dependency，未修改 package manifest 或 lockfile。
- 白色背景、要求寬度 1,800 px；最終 PNG 尺寸：
  - `story-r02.png`：1,784 × 862 px，寬高比 2.07。
  - `technical-r03.png`：1,784 × 980 px，寬高比 1.82。
- technical-r03 SVG／PNG 均 render 成功，exit code 0；r03 保留 r02 的橫式比例與 18 px 基準字級。
- 預定正式 SVG 路徑：
  - `book/figures/story/chapter-02-address-and-range.svg`
  - `book/figures/technical/chapter-02-ip-port-packet.svg`

## 圖 2-1：地址、入口與網路範圍

### Caption（正文凍結文字）

**圖 2-1　地址、入口與網路範圍。**相對有限區域與通常較大地理範圍只是尺度示例，並非距離公式；角色只對應圖中的 localhost HTTP connection。

### Alt text（正文凍結文字）

生活故事圖：左側是相對有限區域內的地址與服務入口，右側是通常較大地理範圍並連接更多獨立使用者的情境；小插格顯示同一程式在不同 localhost HTTP connection 中可交換 client 與 server 角色，角色標籤附著於 connection，且沒有單一距離門檻。

### 非顏色、對比與灰階

- 沿用已預覽的 story-r02：A／B／C 區號、完整標題、地址牌／入口形狀、LAN 實線、WAN 長虛線、connection 編號與相反方向共同承載語意。
- client／server 角色以 connection 上的建立／接受文字表達，不靠人物、框色或永久名稱。
- Source 採白底、近黑文字、深灰線條；正式 accessibility Gate 仍須以實際書頁尺寸確認 WCAG 對比與 100% 灰階輸出。

## 圖 2-2：IP、port 與 packet 的分層概念

### Caption（正文凍結文字）

**圖 2-2　IP、port 與 packet 的分層概念。**角色附著於本次 localhost HTTP connection；IP 與 port 分層，packet 箭頭不代表送達保證，實際路徑也不保證最短。

### Alt text（正文凍結文字）

專業圖：裝置 A 與裝置 B 之間的要求與回應箭頭標示本次 HTTP connection 角色；來源與目的 IP、來源與目的 port 分列，packet 是獨立資料單位，近端 LAN 與跨網路 WAN 範圍另以文字和線型區分。

### 非顏色、對比與灰階

- 端點、packet、LAN／WAN 與推論邊界使用橫向分區、完整標題與外框；IP／port 由獨立欄位框和文字辨識。
- packet 卡中的 IP、port、所攜內容維持垂直排列，但 r03 只用不可見 `~~~` layout 關係，不再顯示方向箭頭，因此不暗示處理順序或流向。
- 本次 HTTP connection 的角色箭頭、服務端點關係與 LAN／WAN 的概念前進箭頭維持 r02 核准候選；packet 卡旁仍明示「資料處理單位 ≠ 送達保證」。
- LAN 使用實線、WAN 使用長虛線；四項推論邊界完整保留非永久角色、IP／port 分層、相對尺度與非送達／順序／一次／準時／最短路徑限制。
- Source 採白底、近黑文字、深灰線條；正式 accessibility Gate 仍須以實際書頁尺寸確認 WCAG 對比與 100% 灰階輸出。

## SVG accessibility

- `story-r02.mmd` 與 `technical-r03.mmd` 都使用 `accTitle`、`accDescr`。
- 兩個 SVG 根節點都具有 `role="graphics-document document"`、`aria-roledescription="flowchart-v2"`、`aria-labelledby="chart-title-my-svg"` 與 `aria-describedby="chart-desc-my-svg"`。
- 兩個 SVG 都有相符 id 的 `<title>` 與 `<desc>`；兩個 `<desc>` 分別逐字等於本文件對應的正文凍結 alt text。

## 實際預覽自檢

- 已實際查看 `technical-r03.png` 原尺寸；橫式 1,784 × 980 版面可讀，packet 卡仍保留 IP、port、所攜內容的分層，但兩個 blocking 有向箭頭已消失。
- 裝置 A／B、client／server 角色、來源／目的 IP、來源／目的 port、特定服務、LAN／WAN、相對尺度與完整推論邊界仍可見。
- 沒有新增標籤、技術主張、真實位址、port number、送達保證、最短路徑或後章機制。
- story-r02 已在前輪實際預覽且本輪位元內容不變；本輪不重繪、不另改版。

## 來源與授權

- 候選由本專案依凍結正文、核准規格與通過的圖規格技術 Gate 自行撰寫；本輪只修正圖中關係線的技術語意。
- 技術來源範圍不變：RFC 9110 §3.3、RFC 791／8200、RFC 6335／BCP 165、IANA registry 與 NIST SP 800-82 Rev. 3。
- 未使用第三方圖片、照片、圖示或模板，未呼叫 image generation；沒有複製字型檔進 repository。
- Renderer 為 Mermaid CLI 11.16.0；最終 attribution 仍依 `bible/source-policy.md` 由主代理於晉升時登記。
- 未讀取、引用、複製或改編排除專案素材。

## 重現命令

technical-r03 以以下固定命令輸出；`<ext>` 為 `svg` 或 `png`：

```bash
npx --yes @mermaid-js/mermaid-cli@11.16.0 \
  -i .work/chapter-02/figures/technical-r03.mmd \
  -o ".work/chapter-02/figures/technical-r03.<ext>" \
  -b white -w 1800
```

正式 artifact set 應綁定未修改的 story-r02 三檔、technical-r03 三檔與本 metadata-r03，並重新執行 figure technical 與 accessibility Gate。
