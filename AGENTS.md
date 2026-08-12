# Book Authoring Kit — Codex 專案指令

這是一套領域中立的技術科普書框架。Codex 主代理負責協調流程；五個 `.codex/agents/` 專職代理只處理各自角色範圍。

## 真實來源

- `bible/`：書籍設定、風格、人物、來源政策、累積術語與章節模板。
- `book/plan.md`：經使用者確認的全書 roadmap。
- `state/current/`：最新進度與讀者已學概念。
- `book/manifests/chapter-NN.json`：正式 Gate 狀態與正文／圖／Lab hash；這是出版資格的唯一真實來源。
- `debug_log.md`：主代理追加的人類可讀審查摘要，不取代 manifest。
- `.work/chapter-NN/`：尚未晉升的草稿、逐輪審查、圖與 Lab。

## 不可違反的規則

1. 寫作開始後，不得自行修改 `bible/book-config.md`、`style.md`、`characters.md`、`source-policy.md` 或 `chapter-template.md`；先在 `.work/proposals/` 提案並取得使用者同意。
2. `bible/glossary.md` 只能由主代理在對應章節所有 Gate 通過後追加核准術語。
3. 未審核內容全部留在 `.work/`；只有主代理能把內容晉升至 `book/`。
4. 寫作者不核准自己的內容；審查者不直接重寫受審內容。
5. 每個 Gate 最多三輪，使用 `r01`、`r02`、`r03` 獨立檔名。第三輪失敗時停止並請使用者決定。
6. 正文一旦在 Gate 後修改，舊 hash 與所有下游 Gate 立即失效，必須重新審查。
7. 不得使用 `state/current/known-concepts.md` 尚未收錄、且本章未先教會的概念。
8. Lab 不得在 production、未授權網路或唯一一份設備上執行；必須提供隔離、復原與 cleanup 步驟。
9. `debug_log.md` 只能由主代理追加，不得改寫既有紀錄。
10. 每完成一章，建立 `state/chapter-NN/` 快照，再以相對 symlink 原子更新 `state/current`。

## 六個角色

- Codex 主代理：orchestrator；控制 Gate、hash、manifest、晉升與 state。
- `editor`：目錄、學習目標、銜接、難度曲線與知識依賴。
- `storyteller`：使用 `$book-writer` 撰寫或修訂正文；主代理不與它同時寫同一草稿。
- `domain-expert`：分別審查正文、圖規格／正式圖與 Lab 技術內容。
- `diagram-designer`：生活故事圖、專業圖規格及無障礙需求。
- `lab-designer`：安全、可重現、可清理的最小 Lab 與故障實驗。

只有使用者要求規劃、撰寫、審查或產出書籍內容時才啟動專職代理。具依賴關係的 Gate 必須循序；只有不修改同一檔案的獨立工作才能平行。

## 新書規劃

1. 確認 `bible/book-config.md`、`characters.md` 與 `source-policy.md` 已填妥。
2. 委派 `editor` 產出 `.work/plan-draft.md`。
3. 檢查章節依賴、難度曲線、技術基線與排除範圍。
4. 使用者確認 `.work/plan-draft.md` 後，由主代理更新 `book/plan.md`。

## 逐章工作流

每章使用 `.work/chapter-NN/`，正文與審查依輪次命名，例如 `draft-r01.md`、`reviews/structure-r01.md`。

1. `editor` 產出 `scope.md`，列出目標、先備知識、新術語、圖與 Lab 是否適用。
2. 委派 `storyteller` 並明確要求使用 `$book-writer`，產出 `draft-rNN.md`。
3. 主代理計算該輪正文 SHA-256，再使用 `$book-linter` 產出綁定此 hash 的 structure review；失敗則回到步驟 2，修訂後必須使用新 hash。
4. `domain-expert` 對同一正文 hash 執行正文技術 Gate，包含來源、版本、比喻與程式碼。
5. `diagram-designer` 產出生活圖與專業圖規格；需要正式圖時再使用 `$book-figures`。不適用時在 scope 與 manifest 說明理由。
6. 主代理計算圖 artifact set hash；`domain-expert` 對正文與圖 hash 執行圖技術 Gate，主代理或 `editor` 執行可讀性、替代文字、對比與灰階列印 Gate。規格或圖檔一經修改，兩個 Gate 都失效。
7. `lab-designer` 產出 Lab、依賴鎖定、預期結果、故障、復原、cleanup 與執行證據。
8. 主代理計算 Lab artifact set hash；`domain-expert` 對正文與 Lab hash 執行 Lab 技術 Gate。不可實際執行時只能標記 `not_applicable`，並寫明限制與人工驗證。
9. `editor` 執行最終 Gate，確認銜接、知識依賴、學習目標與參考資料。
10. 全部 Gate 通過後，主代理把核准正文、圖、Lab 與 evidence 複製到正式路徑，建立 `book/manifests/chapter-NN.json`；此時仍是待驗證候選，不更新 glossary 或 state。
11. 執行 `python3 scripts/validate_kit.py`。失敗時撤回該章候選晉升並回到 `.work/` 修正；成功才視為正式晉升。
12. 主代理追加 glossary 與 debug log、建立 state 快照，原子更新 `state/current`，並再次執行驗證。

## Manifest 規則

正式 manifest 依 `templates/chapter-manifest.json`，必須包含：

- `content_file` 與其小寫 SHA-256。
- `artifacts.figures` 與 `artifacts.labs` 列出每個正式檔案及 SHA-256。圖使用 `book/figures/{story|technical}/chapter-NN-*` 或 `book/assets/figures/chapter-NN-*`；Lab 使用 `book/labs/chapter-NN/`。
- `structure`、`body_technical`、`figure_technical`、`figure_accessibility`、`lab_execution`、`lab_technical`、`editorial` 七個 Gate。
- 每個 Gate 的 `content_sha256` 必須等於正文 hash；圖與 Lab Gate 另須記錄對應的 `artifact_set_sha256`。
- `pass` Gate 必須指向 `book/reviews/chapter-NN/{gate-name}-rNN.md` 中存在的 evidence。
- `not_applicable` 只允許圖或 Lab Gate，且 `note` 不得為空。

每份通過的 evidence 開頭必須包含下列欄位；圖與 Lab Gate 再加入 `Artifact-Set-SHA256`：

```text
Gate: body_technical
Round: 1
Content-SHA256: <64 位小寫 SHA-256>
Result: GATE PASS
```

`$word-generator` 必須先執行 validator；不得只依賴 `debug_log.md` 判斷是否可出版。

## 完成檢查

- 章節包含固定 14 段與「本章參考資料」。
- manifest hash 與正式正文一致，所有必要 Gate 完成。
- 圖與 Lab 未引入正文 Gate 之後未審查的新技術主張。
- 新術語、來源、圖像授權、known concepts 與 state 已同步。
- Lab 有隔離、復原、cleanup、依賴版本與預期輸出。
- `state/current` 是指向最新快照的有效相對 symlink。
