# State 快照格式

每完成一章，建立新的 `state/chapter-NN/`，至少包含：

- `progress.md`：完成章節、manifest 與下一步。
- `known-concepts.md`：讀者已正式學過的概念。

主代理建立新快照後，使用相對 symlink 更新 `state/current`：

```bash
ln -sfn chapter-NN state/current.next
python3 -c 'import os; os.replace("state/current.next", "state/current")'
```

不要在已有 `chapter-00` 的專案內重跑初始化指令。建立新書請使用根目錄的 `scripts/init_book.py`。
