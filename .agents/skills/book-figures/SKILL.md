---
name: book-figures
description: 把通過正文與圖規格 Gate 的技術科普插圖轉成 Mermaid 草圖、正式插圖需求或圖片。當需要預覽專業圖、整理生圖 prompt 或生成正式圖時使用；輸出仍須技術與無障礙 Gate。
---

# Book Figures

1. 讀取核准正文、正文 technical review、story spec、technical spec 與 `bible/source-policy.md`。
2. 依規格選擇 Mermaid、SVG 或生圖 prompt；不把所有領域強迫畫成網路架構圖。
3. 預覽先寫入 `.work/chapter-NN/figures/`，檔名包含用途與輪次，例如 `technical-r01.mmd`。
4. 保留精確元件、關係、方向、狀態與資料意義；不得新增規格中沒有的技術主張。
5. 同時產出 caption、alt text、非顏色辨識方式、對比與灰階列印說明。
6. 未經使用者明確要求「開始生圖」，只產出 Mermaid 或 prompt，不呼叫生圖工具。
7. 使用生圖能力時，以核准規格為唯一內容依據，並把工具、日期、prompt、授權與修改登記到 attribution 草稿。
8. 規格正式路徑為 `book/figures/{story|technical}/chapter-NN-*`，生成資產為 `book/assets/figures/chapter-NN-*`；主代理計算完整圖 artifact set hash，生成或修改後重新執行 figure technical 與 accessibility Gate。
