Gate: figure_accessibility
Round: 2
Content-SHA256: 0a9673a4bbf89a6b51b8da3a1c65d2328f0c6e9a0a90f4d6a3741a84a7933d16
Artifact-Set-SHA256: 19f5197167bbec5f7e19426441479143b723f051c1420ae81ee59284a152cb7c
Result: GATE PASS

# Chapter 01 正式候選圖無障礙審查 r02

## 重發原因

正文 r03 新增兩個正式 SVG 引用與 caption，正文 hash 因此改變；圖規格及 metadata 的 `Content-SHA256` 同步更新，使 artifact set hash 改變。Mermaid 與 SVG 視覺內容未改。本 Gate 以最終正文與最終正式路徑 hash 重發。

## 通過證據

- 兩個正文 image link 的 alt text 與 `metadata-r02.md` 完全一致，caption 亦一致。
- 固定 renderer 11.16.0 的兩張 SVG 均有 `<title>`、`<desc>`、`aria-labelledby`；正文另提供 Markdown alt text。
- 色值對比仍為：文字最低 16.12:1、外框／線條最低 9.37:1，高於 4.5:1／3:1 門檻。
- 圖面為白／近黑／灰階，另以 A/B、位置、形狀、線型、`→`／`←` 與完整標籤辨識，無資訊只靠顏色。
- PNG 預覽目視結果未變：無裁切或文字重疊；生活圖與專業圖的警語均在主圖之外清楚可讀。
- 正式 artifact set 的七個檔案與對應路徑已列於 r01；本輪 hash 已按更新後實際檔案重算。

## 結論

最終正文、圖規格、Mermaid、SVG 與 metadata 的無障礙資訊一致，且以相同正文／artifact set hash 綁定。

Result: GATE PASS
