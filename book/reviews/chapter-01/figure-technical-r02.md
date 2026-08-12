Gate: figure_technical
Round: 2
Content-SHA256: 0a9673a4bbf89a6b51b8da3a1c65d2328f0c6e9a0a90f4d6a3741a84a7933d16
Artifact-Set-SHA256: 19f5197167bbec5f7e19426441479143b723f051c1420ae81ee59284a152cb7c
Result: GATE PASS

# Chapter 01 正式候選圖技術審查 r02

## 審查範圍與重新綁定

- 最終正文：`.work/chapter-01/draft-r03.md`
- 最終正文技術證據：`.work/chapter-01/reviews/body-technical-r03.md`
- 圖規格：`.work/chapter-01/figures/story-spec-r01.md`、`technical-spec-r01.md`
- 圖稿與 render：`.work/chapter-01/figures/story-r02.mmd`、`story-r02.svg`、`technical-r02.mmd`、`technical-r02.svg`
- 圖說、替代文字與產製紀錄：`.work/chapter-01/figures/metadata-r02.md`
- 前輪圖技術證據：`.work/chapter-01/reviews/figure-technical-r01.md`
- 排除範圍：未讀取、未引用、未比較 `/home/felix/work/webrtc_story`

正文 SHA-256 已重算一致。兩份 spec 與 metadata 的 `Content-SHA256` 均已同步為本輪最終正文 hash；圖的 Mermaid source 與 SVG render 內容未改。

## 七檔正式 mapping 與 artifact set

依主代理指定的未來正式路徑逐檔重算：

| 候選來源 | 未來正式路徑 | SHA-256 |
|---|---|---|
| `.work/chapter-01/figures/story-spec-r01.md` | `book/figures/story/chapter-01-file-versus-conversation-spec.md` | `c9c239fd4ae2f4283f6a84db8fdef9e4223d7509418f7c726095869cee059f70` |
| `.work/chapter-01/figures/story-r02.mmd` | `book/figures/story/chapter-01-file-versus-conversation.mmd` | `5e35b08a3c5bd7d35944941e6c343b59945ce29261bfa8cb16ed6e5a5371f135` |
| `.work/chapter-01/figures/story-r02.svg` | `book/figures/story/chapter-01-file-versus-conversation.svg` | `5c2ad02ef4ca59be6c068b5ef51a7104e028248cc7700bf4dff361b324d47b15` |
| `.work/chapter-01/figures/technical-spec-r01.md` | `book/figures/technical/chapter-01-browser-concept-overview-spec.md` | `a1980390d0c67afe58dbcdca671c8f4fc8d4120bec4d1d3ef6d49804df5c338f` |
| `.work/chapter-01/figures/technical-r02.mmd` | `book/figures/technical/chapter-01-browser-concept-overview.mmd` | `9572797ad38aef609716d4e628a0945b71ce2fb237e0201be68518e3697b1320` |
| `.work/chapter-01/figures/technical-r02.svg` | `book/figures/technical/chapter-01-browser-concept-overview.svg` | `18bd4873c80eae3d7889943bedd4b737a304c0fbfc3eaa218542db4a39e1e3c4` |
| `.work/chapter-01/figures/metadata-r02.md` | `book/assets/figures/chapter-01-figure-metadata.md` | `bec57047b99c74f76518773570a7accdf1a222848fa546c2d37866e5cb9d41a0` |

按正式路徑排序，使用 kit 的 compact JSON 正規化方式重算，artifact-set SHA-256 為 `19f5197167bbec5f7e19426441479143b723f051c1420ae81ee59284a152cb7c`，與本 Gate 綁定值一致。

## 最終正文引用核查

1. `draft-r03.md:106` 的生活圖引用從未來 `book/chapters/chapter-01.md` 正確解析至 `book/figures/story/chapter-01-file-versus-conversation.svg`，即七檔 mapping 中的生活圖 SVG。
2. `draft-r03.md:122` 的專業圖引用正確解析至 `book/figures/technical/chapter-01-browser-concept-overview.svg`，即 mapping 中的專業圖 SVG。
3. `draft-r03.md:106,108,122,124` 的兩組 alt／caption 與同步後 metadata 逐字一致，也和 MMD／SVG 的可見內容及語意說明一致；正文沒有引用錯圖或用 caption 改寫圖的技術含義。
4. `body-technical-r03.md` 已確認 r03 相對 r02 只新增上述 image link 與 caption，沒有改動其他技術、版本、來源或安全內容。

## 生活故事圖回歸

1. 上列仍只呈現被明確命名的完成檔案模式：準備完整影片、完成、一次性交付、小華觀看與回應，以及前段等待。
2. 下列四個事件仍依時間排列，框內文字箭頭依序交替表示小明／小華互相回應；事件間的 Mermaid 關係只供排版且不可見。
3. 圖內、caption、alt 與 SVG desc 都保留「文字箭頭只表示互動節奏，不表示資料實際路徑」的限制，未新增 direct/P2P、固定道路、封包或實際拓撲主張。
4. 可見內容沒有 server、protocol、IP、port、relay、安全機制或其他 Chapter 01 尚未教授的技術元件。

## 專業圖回歸

1. Browser A／小明端與 Browser B／小華端仍左右等權；中央上列「協調資訊」與下列「即時影音」在位置、點狀／實線字形、虛線／實線框及完整文字標籤上保持分離。
2. Browser 與中央標籤間仍只有不可見排版關係。可見 `←`／`→` 是框內文字而非真實連線，且底部警語明確排除直接傳送、實際拓撲、資料路徑與內部做法。
3. 協調資訊與即時影音沒有合流或語意互換；圖未把 signaling 畫成媒體，也未加入 STUN/TURN、NAT、DTLS/SRTP、codec、relay 或固定順序。
4. 最終正文的 caption／alt 只描述上述概念交換與限制，不新增實作、安全或路徑主張。

## SVG 語意回歸

1. 兩份 SVG hash 與 r01 已審 render 完全相同；逐項解析可見文字、edge、`<title>` 與 `<desc>`，未出現新標籤、錯誤方向、額外元件或隱含路徑。
2. 兩份 SVG 根元素仍以 `aria-labelledby`／`aria-describedby` 連到正確且唯一的 title／desc ID。
3. 生活圖 title／desc 正確說明兩種時間關係與箭頭限制；專業圖 title／desc 正確說明左右端點、分列兩種概念交換及禁止直接／拓撲／路徑推論，均與最終正文及 metadata 一致。

## 結論

七檔候選內容、正式 mapping、個別 hash 與 artifact-set hash 均已核對。圖的 MMD／SVG 技術內容未改，最終正文引用、caption 與 alt 正確綁定同一正式資產；箭頭邊界、兩流分離、術語與未教先用限制均維持通過狀態。

Result: GATE PASS
