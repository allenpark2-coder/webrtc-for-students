---
name: book-writer
description: 依本專案的 scope、技術基線、來源政策與固定 14 段模板撰寫或修訂技術科普章節。當使用者要求寫第 N 章、建立草稿或修訂 Gate 退回稿時使用；由 storyteller 執行，不負責核准 Gate。
---

# Book Writer

1. 讀取指定 `.work/chapter-NN/scope.md`、全部 `bible/*.md`、`book/plan.md`、`state/current/known-concepts.md` 與既有 review。
2. 確認書籍設定、技術基線與目標章節已填妥；缺少實質資料時列出缺項並停止。
3. 使用 `## 1.` 至 `## 14.` 固定標題，再加入 `## 本章參考資料`。不適用項目保留段落並說明理由。
4. 使用已核准人物；每個比喻寫出成立範圍與失真處。只使用已學概念或在本章先教會的新概念。
5. 將新術語作為候選小卡放在正文，不修改 glossary。為技術主張提供版本、第一手來源與查核日期。
6. Lab 相關段落遵守隔離、授權、復原與 cleanup 規則；不得指向 production 或真實憑證。
7. 每輪寫入新的 `.work/chapter-NN/draft-rNN.md`，不得覆寫舊稿或直接寫入 `book/chapters/`。
8. 完成後交由主代理使用 `$book-linter`；不得自行宣告 Gate 通過。
