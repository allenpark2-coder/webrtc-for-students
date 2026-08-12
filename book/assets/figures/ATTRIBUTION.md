# Figure Attribution

每張正式圖片、圖示、字型或第三方資產都新增一筆：

```markdown
## chapter-NN-figure-name

- 檔案：
- 用途／caption：
- 作者或生成工具：
- 來源 URL：
- 建立／下載日期：
- 授權：
- 修改內容：
- 對應規格／prompt：
```

## chapter-01-file-versus-conversation

- 檔案：`book/figures/story/chapter-01-file-versus-conversation.mmd`、`.svg`
- 用途／caption：圖 1-1，完成檔案寄送與持續雙向互動的時間差。
- 作者或生成工具：本專案自行撰寫 Mermaid；`@mermaid-js/mermaid-cli` 11.16.0 渲染 SVG
- 來源 URL：不適用；內容依 Chapter 01 核准正文與圖規格
- 建立／下載日期：2026-08-12
- 授權：本專案自行撰寫；最終書稿授權於出版前確認
- 修改內容：r02 修正雙向互動方向、灰階樣式與 SVG `accTitle`／`accDescr`
- 對應規格／prompt：`book/figures/story/chapter-01-file-versus-conversation-spec.md`；未使用生圖 prompt

## chapter-01-browser-concept-overview

- 檔案：`book/figures/technical/chapter-01-browser-concept-overview.mmd`、`.svg`
- 用途／caption：圖 1-2，WebRTC 通話的最小概念鳥瞰。
- 作者或生成工具：本專案自行撰寫 Mermaid；`@mermaid-js/mermaid-cli` 11.16.0 渲染 SVG
- 來源 URL：<https://www.w3.org/TR/2025/REC-webrtc-20250313/>
- 建立／下載日期：2026-08-12
- 授權：本專案自行撰寫；最終書稿授權於出版前確認
- 修改內容：r02 改為左右等權端點、上下兩類概念交換、底部警語與 SVG `accTitle`／`accDescr`
- 對應規格／prompt：`book/figures/technical/chapter-01-browser-concept-overview-spec.md`；未使用生圖 prompt

## chapter-02-address-and-range

- 檔案：`book/figures/story/chapter-02-address-and-range.mmd`、`.svg`
- 用途／caption：圖 2-1，小明以地址、入口與範圍理解位置與服務入口。
- 作者或生成工具：本專案自行撰寫 Mermaid；`@mermaid-js/mermaid-cli` 11.16.0 渲染 SVG
- 來源 URL：<https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- 建立／下載日期：2026-08-12
- 授權：本專案自行撰寫；最終書稿授權於出版前確認
- 修改內容：r02 改為橫式三區版面，補強非顏色辨識、灰階樣式與 SVG 無障礙標記
- 對應規格／prompt：`book/figures/story/chapter-02-address-and-range-spec.md`；未使用生圖 prompt

## chapter-02-ip-port-packet

- 檔案：`book/figures/technical/chapter-02-ip-port-packet.mmd`、`.svg`
- 用途／caption：圖 2-2，localhost HTTP connection 中的角色、IP、port 與版本中立 packet 分層。
- 作者或生成工具：本專案自行撰寫 Mermaid；`@mermaid-js/mermaid-cli` 11.16.0 渲染 SVG
- 來源 URL：<https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3>、<https://www.rfc-editor.org/info/rfc791>、<https://www.rfc-editor.org/info/rfc8200>、<https://www.rfc-editor.org/rfc/rfc6335.html#section-6>
- 建立／下載日期：2026-08-12
- 授權：本專案自行撰寫；最終書稿授權於出版前確認
- 修改內容：r03 將 packet 欄位間關係改為無方向版面分隔，移除可能被誤讀為處理流程的箭頭
- 對應規格／prompt：`book/figures/technical/chapter-02-ip-port-packet-spec.md`；未使用生圖 prompt

## chapter-03-switchboard-guard

- 檔案：`book/figures/story/chapter-03-switchboard-guard.mmd`、`.svg`
- 用途／caption：圖 3-1，總機與警衛是兩個工作。
- 作者或生成工具：本專案自行撰寫 Mermaid；`@mermaid-js/mermaid-cli` 11.16.0 渲染 SVG
- 來源 URL：<https://www.rfc-editor.org/info/rfc2663>、<https://csrc.nist.gov/pubs/sp/800/41/r1/final>、<https://www.rfc-editor.org/info/rfc8085>、<https://www.rfc-editor.org/info/rfc9293>
- 建立／下載日期：2026-08-12
- 授權：本專案自行撰寫；最終書稿授權於出版前確認
- 修改內容：r02 移除跨面板流程箭頭，維持 mapping／policy 與 UDP／TCP 語意分離
- 對應規格／prompt：`book/figures/story/chapter-03-switchboard-guard-spec.md`；未使用生圖 prompt

## chapter-03-mapping-policy-transport

- 檔案：`book/figures/technical/chapter-03-mapping-policy-transport.mmd`、`.svg`
- 用途／caption：圖 3-2，Address 表示、mapping、policy 與 transport 語意分層。
- 作者或生成工具：本專案自行撰寫 Mermaid；`@mermaid-js/mermaid-cli` 11.16.0 渲染 SVG
- 來源 URL：<https://www.rfc-editor.org/info/rfc1918>、<https://www.rfc-editor.org/info/rfc2663>、<https://www.rfc-editor.org/info/rfc4787>、<https://www.rfc-editor.org/info/rfc8085>、<https://www.rfc-editor.org/info/rfc9293>
- 建立／下載日期：2026-08-12
- 授權：本專案自行撰寫；最終書稿授權於出版前確認
- 修改內容：r02 加強 mapping record、policy evidence、allow 與 listener 的分層，並補全 UDP／TCP 限制文字
- 對應規格／prompt：`book/figures/technical/chapter-03-mapping-policy-transport-spec.md`；未使用生圖 prompt
