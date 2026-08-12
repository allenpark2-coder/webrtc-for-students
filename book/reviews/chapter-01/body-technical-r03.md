Gate: body_technical
Round: 3
Content-SHA256: 0a9673a4bbf89a6b51b8da3a1c65d2328f0c6e9a0a90f4d6a3741a84a7933d16
Result: GATE PASS

# Chapter 01 正文技術審查 r03

## 審查範圍

- 受審正文：`.work/chapter-01/draft-r03.md`
- 差異基準：`.work/chapter-01/draft-r02.md`
- 前置結構證據：`.work/chapter-01/reviews/structure-r03.md`
- 前輪正文技術證據：`.work/chapter-01/reviews/body-technical-r02.md`
- 圖規格：`.work/chapter-01/figures/story-spec-r01.md`、`technical-spec-r01.md`
- 圖稿與 render：`.work/chapter-01/figures/story-r02.mmd`、`story-r02.svg`、`technical-r02.mmd`、`technical-r02.svg`
- 圖說與替代文字：`.work/chapter-01/figures/metadata-r02.md`
- 正式候選圖技術證據：`.work/chapter-01/reviews/figure-technical-r01.md`
- 排除範圍：未讀取、未引用、未比較 `/home/felix/work/webrtc_story`

正文 SHA-256 已重算，與本 Gate 綁定值一致。

## r02 → r03 差異核查

逐行 diff 顯示，本輪只新增四個 Markdown 區塊：

1. 第 106 行：生活故事圖的 SVG image link 與完整 alt text。
2. 第 108 行：圖 1-1 caption。
3. 第 122 行：專業圖的 SVG image link 與完整 alt text。
4. 第 124 行：圖 1-2 caption。

除上述兩個 image link 與兩段 caption 外，正文內容逐字不變；沒有夾帶版本、來源、術語、觀察流程、安全條件或技術解釋的改寫。

## 圖 1-1 引用核查

1. **路徑正確。**第 106 行的 `../figures/story/chapter-01-file-versus-conversation.svg` 從未來正式正文 `book/chapters/chapter-01.md` 解析為 `book/figures/story/chapter-01-file-versus-conversation.svg`，與生活圖規格建議正式路徑一致。
2. **Alt 與 metadata 完全一致。**正文 alt 逐字等於 `metadata-r02.md` 的圖 1-1 alt，且與 MMD／SVG 實際內容相符：上列先準備、完成、交付、觀看與回應，下列四個事件方向交替，並保留文字箭頭不代表資料實際路徑的限制。
3. **Caption 與 metadata 完全一致。**第 108 行正確概括完成檔案模式與持續互動模式，沒有把生活故事提升為 WebRTC 實際拓撲、固定道路、direct/P2P 或封包流程。
4. **未新增錯誤技術主張。**Alt／caption 只描述圖面可見的時間關係與故事互動；沒有加入 server、protocol、IP、port、relay、安全機制或其他後章概念。

## 圖 1-2 引用核查

1. **路徑正確。**第 122 行的 `../figures/technical/chapter-01-browser-concept-overview.svg` 從未來正式正文解析為 `book/figures/technical/chapter-01-browser-concept-overview.svg`，與專業圖規格建議正式路徑一致。
2. **Alt 與 metadata 完全一致。**正文 alt 逐字等於 `metadata-r02.md` 的圖 1-2 alt，並正確描述實際 SVG：Browser A／B 左右等權；中央上列是點狀字形的協調資訊，下列是實線字形的即時影音；底部警語排除直接傳送、實際拓撲與資料路徑。
3. **Caption 與 metadata 完全一致。**第 124 行只區分協調資訊與即時影音兩種概念交換，明確限制文字箭頭只表示雙方都需交換，不主張 direct/P2P、實際路徑、內部實作或固定順序。
4. **兩流沒有混淆。**Alt／caption 保留協調資訊與即時影音的名稱、上下位置及用途差異；沒有把 signaling 當成媒體，也沒有加入 STUN/TURN、NAT、DTLS/SRTP、codec 或其他尚未教授的機制。

## 圖檔一致性回歸

1. 兩份 Mermaid source 與 SVG render 的內容 hash 均與已通過的正式候選圖技術 Gate 相同；本輪沒有修改實際圖面。
2. `story-r02.svg` 的 `<title>`／`<desc>` 與新增的生活圖 alt／caption 主張一致；`technical-r02.svg` 的 `<title>`／`<desc>` 與新增的專業圖 alt／caption 主張一致。
3. 兩份 SVG 的 `aria-labelledby`／`aria-describedby` 仍指向正確且唯一的 title／desc ID；沒有因正文引用新增矛盾的可存取名稱或說明。

## r02 已通過項回歸

1. **規範與來源未變。**WebRTC 仍以 W3C 2025-03-13 Recommendation 為定位；RFC 8825 仍正確列為 Proposed Standard、Internet Standards Track，並限定為 applicability statement／規範 roadmap，本身不另定 protocol。
2. **術語與比喻未變。**本章新增術語仍只有即時通訊、WebRTC、peer；完成影片／持續對話比喻仍明確排除實際路徑推論。
3. **證據邊界未變。**單向畫面與 mute/unmute 的觀察仍只支援有限產品層結論，不宣稱通話所有方向、內部機制、安全或品質均已驗證。
4. **安全與復原未變。**自有裝置／帳號、無第三人、不錄音錄影、耳機／低音量、停止條件、紙上替代、unmute 復原、cleanup 與裝置停止使用的驗證均完整保留。
5. **沒有未教先用。**新增內容只引用已通過技術審查的兩張 Chapter 01 概念圖，未引入後章 API、protocol、網路元件或工具。

## 結論

r03 新增的兩個實際 SVG 引用與 caption 均和核准規格、metadata 及實際圖面一致，正式相對路徑正確，也沒有新增或扭曲技術主張；r02 已通過的規範、來源、術語、比喻、證據與安全項目回歸無退步。

Result: GATE PASS
