---
name: word-generator
description: 按 book plan 彙整 manifest 完整且正文、圖、Lab hash 相符的正式章節，產出 Markdown、DOCX、PDF 或 EPUB。當使用者要求預覽、彙整或出版書稿時使用；不得只依 debug log 判斷收錄資格。
---

# Word Generator

1. 先執行 `python3 scripts/validate_kit.py`；驗證失敗時停止出版並列出問題。
2. 讀取 `book/plan.md`、`book/chapters/` 與 `book/manifests/`，只收錄正文、圖、Lab hash 相符且全部必要 Gate 為 `pass`／核准 `not_applicable` 的章節。
3. 依 plan 順序建立「收錄章節」與「跳過章節及原因」清單。
4. 組裝正文、章末來源、圖 caption／alt text、Lab 連結與授權資訊，預設輸出 `dist/book.md`。
5. DOCX、PDF 或 EPUB 使用環境中可用的專用文件 skill 或工具，分別輸出 `dist/book.docx`、`dist/book.pdf`、`dist/book.epub`。
6. 缺少轉檔工具時只產出完整 Markdown，清楚列出未完成格式；不得假裝已建立檔案。
7. 不修改原始章節、manifest 或 Gate evidence 來掩蓋缺漏。
