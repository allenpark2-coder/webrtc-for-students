---
name: book-linter
description: 檢查技術科普草稿的 14 段結構、繁體中文術語、候選小卡、固定人物、比喻邊界、來源與 Lab 安全欄位。當草稿完成或修訂後、送 domain-expert 前使用；不判斷技術主張是否正確。
---

# Book Linter

1. 讀取指定草稿、scope、全部 `bible/*.md`、`book/plan.md` 與 `state/current/known-concepts.md`。
2. 檢查 14 個標題依序完整、五題理解題確有五題，並存在「本章參考資料」。
3. 檢查術語格式、候選小卡欄位、未學概念、核准人物，以及每個比喻的成立與失真範圍。
4. 檢查版本／範圍、來源項目、圖是否說明適用性，以及 Lab 的隔離、復原與 cleanup 欄位是否存在。
5. 檢查文章是否先提問題再介紹技術，並避免以無關內容填滿不適用段落。
6. 對失敗項目提供標題或行號、問題及可操作修改方向。
7. 主代理提供本輪正文 SHA-256；每輪寫入新的 `.work/chapter-NN/reviews/structure-rNN.md`，使用 `Gate: structure`、`Round`、`Content-SHA256` 與 `Result: GATE PASS`／`GATE FAIL` 欄位。缺少 hash 時停止並回報。
8. 不修改草稿，不評論技術正確性，也不覆寫舊 review。
