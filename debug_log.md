# Debug Log

## 2026-08-12 — Phase 1 全書規劃

- editor 產出三輪獨立規劃草案；最新為 `.work/plan-draft-r03.md`。
- domain-expert 的第三輪審查結論為 `PLAN GATE PASS`，證據位於 `.work/reviews/plan-technical-r03.md`。
- 草案包含 6 Parts、18 Chapters、15 個 Lab 與三張需求／術語／Lab 對照表。
- 尚未取得使用者對全書設計的核准，因此未晉升 `book/plan.md`，也未開始正文、正式圖或 Lab 實作。

> 人類可讀、append-only 的技術審查摘要。只有主代理在章節正式晉升時追加；出版資格以 `book/manifests/` 為準。

<!--
## YYYY-MM-DD — Chapter NN — PASS

- Content SHA-256：
- 審查輪次：
- 主要修正：
- Manifest：book/manifests/chapter-NN.json
-->

## 2026-08-12 — Chapter 01 — PASS

- Content SHA-256：`0a9673a4bbf89a6b51b8da3a1c65d2328f0c6e9a0a90f4d6a3741a84a7933d16`
- 審查輪次：structure r03、body technical r03、figure technical r02、figure accessibility r02、editorial r01；Lab execution／technical 為有理由的 `not_applicable`。
- 主要修正：將 RFC 8825 更正為 Proposed Standard／Internet Standards Track；補上兩張核准 SVG 的正式引用、caption 與 alt text；Mermaid 使用 11.16.0 固定渲染，SVG 內建 title／desc／ARIA。
- Figure artifact-set SHA-256：`19f5197167bbec5f7e19426441479143b723f051c1420ae81ee59284a152cb7c`
- Manifest：`book/manifests/chapter-01.json`

## 2026-08-12 — Chapter 02 — PASS

- Content SHA-256：`a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69`
- 審查輪次：structure r03、body technical r02、figure technical r02、figure accessibility r02、editorial r01；Lab execution／technical 為有理由的 `not_applicable`。
- 主要修正：限制 client／server 定義於 localhost HTTP connection；以 IPv4／IPv6 第一手規範及 NIST 資料校準 IP、LAN／WAN 邊界；記錄實際 Ubuntu／Python 驗證環境；將 packet 圖的方向箭頭改為無方向分隔。
- Figure artifact-set SHA-256：`c6a76a305a02b8c6c12f1bcc2c2bc5975101169b3272c7cf1242b41f974c8a1d`
- Manifest：`book/manifests/chapter-02.json`

## 2026-08-12 — Chapter 03 — PASS

- Content SHA-256：`e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6`
- 審查輪次：structure r02、body technical r02、figure technical r02、figure accessibility r02、editorial r01；Lab execution／technical 為有理由的 `not_applicable`。
- 主要修正：將 public/global address realm 與觀察位置相關的 outside observed address 分離；修正核心術語首次教學順序；把 mapping record、firewall policy、allow 與 listener evidence 分層；補足 UDP／TCP 圖面限制。
- 章內觀察：一次性 rootless user/network namespace 中完成 TCP／UDP baseline、各自停用、另一 transport 持續成功、恢復與 cleanup；無 host 網路變更或殘留。
- Figure artifact-set SHA-256：`302b6630def6f8370f2c1967ce17da5c219212db1e06e868af13c9ae1ca976fb`
- Manifest：`book/manifests/chapter-03.json`
