Gate: figure_accessibility
Round: 2
Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6
Artifact-Set-SHA256: 302b6630def6f8370f2c1967ce17da5c219212db1e06e868af13c9ae1ca976fb
Result: GATE PASS

# Chapter 03 Figure Accessibility Review — Round 02

## 審查邊界與綁定集合

- 已重算 `.work/chapter-03/draft-r02.md`，SHA-256 與頁首綁定值一致。
- 本 Gate 綁定主代理提供的 r02 七檔正式 mapping 與 artifact-set SHA-256；兩張 PNG 只作實際渲染預覽，不加入正式 mapping：
  - `.work/chapter-03/figures/metadata-r02.md` → `book/assets/figures/chapter-03-figure-metadata.md`
  - `.work/chapter-03/figures/story-spec-r01.md` → `book/figures/story/chapter-03-switchboard-guard-spec.md`
  - `.work/chapter-03/figures/story-r02.mmd` → `book/figures/story/chapter-03-switchboard-guard.mmd`
  - `.work/chapter-03/figures/story-r02.svg` → `book/figures/story/chapter-03-switchboard-guard.svg`
  - `.work/chapter-03/figures/technical-spec-r01.md` → `book/figures/technical/chapter-03-mapping-policy-transport-spec.md`
  - `.work/chapter-03/figures/technical-r02.mmd` → `book/figures/technical/chapter-03-mapping-policy-transport.mmd`
  - `.work/chapter-03/figures/technical-r02.svg` → `book/figures/technical/chapter-03-mapping-policy-transport.svg`
- 本輪獨立檢查 r02 artifact；r01 accessibility evidence 綁定舊 artifact-set，不適用於本候選。本輪未修改任何受審 artifact。

## Caption 與 alt text

- 圖 3-1 caption 在正文、`story-spec-r01.md` 與 `metadata-r02.md` 三處逐字一致；圖 3-2 的三處比對亦一致。
- 圖 3-1 alt text 在正文 Markdown、story spec、metadata、r02 Mermaid `accDescr` 與 r02 SVG `<desc>` 五處逐字一致；圖 3-2 的五處比對亦一致。
- 兩段 alt 均涵蓋主要閱讀順序、關係與限制，沒有用檔名或泛稱「示意圖」代替內容；caption 不要求讀者辨認特定顏色。

## SVG title、desc、role 與 ARIA

- Story r02 SVG 根節點為 `role="img"`，`aria-labelledby="ch03-story-title ch03-story-desc"` 與 `aria-describedby="ch03-story-desc"` 都指向存在且唯一的元素；title 為「總機與警衛分工，以及 UDP／TCP 服務語意」，desc 逐字等於凍結 alt。
- Technical r02 SVG 根節點為 `role="img"`，`aria-labelledby="ch03-tech-title ch03-tech-desc"` 與 `aria-describedby="ch03-tech-desc"` 都指向存在且唯一的元素；title 為「IPv4 mapping、獨立 firewall policy 與 UDP／TCP 服務語意」，desc 逐字等於凍結 alt。
- 兩個根 id、title id 與 desc id 互不衝突。輸出為靜態圖，沒有動畫、閃爍、tab stop 或 hover-only 資訊；image role 讓 Mermaid 內部裝飾圖元不會被誤當成逐一操作的互動控制項。

## 非顏色辨識

- Story 的 A、B 與比喻界線以位置、標題、外框和留白分開；r02 不再用可見箭頭跨接這三區，因此不需靠底色判斷 panel 邊界。
- Story 內以矩形 mapping 節點、菱形 policy 節點、實線 allow 箭頭、平頭 block 線、虛線阻擋框與完整文字共同辨識；UDP 與 TCP 另以各自泳道、標題、資料邊界／連續 stream 結構及文字區分。
- Technical 的 host、平行 mapping 卡、中介分層界線、policy 菱形及 outside evidence 虛線區都有不同形狀、位置與完整標籤；mapping boundary 與 policy 之間沒有可見資料箭頭。
- Technical 的 allow 使用尖頭線，block 使用平頭線及虛線 evidence 框。`mapping record ≠ policy evidence`、`mapping ≠ allow`、`allow ≠ listener exists` 均直接顯示，沒有以色彩替代不等式。
- UDP 與 TCP 的新增限制各自位於有標題的泳道；delivery／duplicate／ordering／congestion 及 failure／immediate／processed／security 均為可見文字。兩者不靠藍紫色區分，也沒有速度色階或排名圖例。

## 灰階與實際預覽

- 已實際查看 `story-r02.png` 及 `technical-r02.png` 原尺寸。沒有文字、箭頭、平頭終止線、虛線 evidence 或外框遭裁切、重疊或遮蔽。
- 已以 FFmpeg 產生並人工查看 1,280 px 寬的 100% 灰階代理：story 為 1,280 × 480，technical 為 1,280 × 622。
- 灰階下，mapping／policy 仍由矩形／菱形、實線／虛線、標題與文字辨識；allow／block 仍由箭頭／平頭線及標籤辨識；outside conditional evidence 仍可由虛線區塊辨識。
- UDP 與 TCP 的外框、內部節點、方向、service 限制與不排名速度文字在灰階代理中仍可辨；沒有關鍵語意隨顏色消失。

## 對比與字級

- 兩份 r02 Mermaid source 的 theme 基準字級都是 18 px，全部明示 node class 的字級下限也都是 18 px。
- 對 source 中宣告的文字／底色、主線／白底與 cluster 線／底色 token 依 WCAG 相對亮度公式計算，受檢集合最低值為 cluster 線 `#52677D` 對 `#FAFCFE` 的 5.68:1；其餘受檢文字與主線配對為 11.91:1–16.87:1。
- 上述數值只代表 source palette 指定色對，足以覆核一般文字 4.5:1 與非文字圖形 3:1 的設計目標；本 Gate 沒有把它誤稱為整張抗鋸齒 raster 的逐像素量測。
- 原尺寸、1,280 px 彩色與灰階人工預覽中，深色文字、外框、箭頭與 evidence 虛線在淡色／白色背景上均清楚；沒有文字置於照片、紋理或漸層上。

## 尺寸、比例與單欄可讀性

- `story-r02.png` 實際為 1,984 × 743 px，寬高比 2.67，符合 story `>= 1.5`。
- `technical-r02.png` 實際為 1,984 × 964 px，寬高比 2.06，符合 technical `>= 1.6`。
- 1,280 px 單欄代理中，Story 的 A／B／比喻界線、主要節點與限制可讀，且跨 panel 沒有殘留可見箭頭。
- Technical 的 mapping/policy 三條界線、E/public 條件、UDP 新增限制、TCP 新增限制與底部全圖界線在原生 1,280 px 檢視下仍可辨；沒有字元糊成不可判讀或框線合併。
- Technical 的 evidence、service 限制及全圖邊界是密度最高區域。正式 HTML／A4 排版應保留向量來源與完整欄寬，不應用低於本次代理的 raster 取代 SVG；這是出版放置條件，不是本候選的 blocking finding。

## 結論

r02 候選的凍結 caption／alt、SVG image semantics、非顏色辨識、source palette 對比、18 px 基準字級、橫式比例，以及原尺寸／1,280 px／灰階實際預覽均符合本輪無障礙要求。沒有需要退回 artifact 的 blocking finding。
