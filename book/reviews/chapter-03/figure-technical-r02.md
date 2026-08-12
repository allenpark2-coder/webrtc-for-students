Gate: figure_technical
Round: 2
Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6
Artifact-Set-SHA256: 302b6630def6f8370f2c1967ce17da5c219212db1e06e868af13c9ae1ca976fb
Result: GATE PASS

# Chapter 03 Figure Technical Gate — Round 02

## 審查識別

- 已重算正文 SHA-256、新版 metadata/MMD/SVG 與兩份未修改 r01 spec；以 future-formal-path mapping 依 validator 相同算法計算七檔 artifact set，結果與 header 及委派值相符。
- 本輪 mapping：`metadata-r02.md`、`story-r02.mmd/.svg`、`technical-r02.mmd/.svg` 分別對應既定正式 metadata/story/technical 路徑；兩份 `*-spec-r01.md` 沿用既定正式 spec 路徑。
- 已完整核對 r01→r02 MMD/metadata diff、兩份 r02 SVG、核准 spec、正文凍結 caption/alt、body technical r02、figure-spec technical r01 與 figure-technical r01。
- 已實際以原始解析度查看 `story-r02.png`（1,984 × 743）及 `technical-r02.png`（1,984 × 964）。未修改任何候選 artifact、正文或 spec，未讀取或引用排除專案。

## r01 blocking 1：跨 panel 可見箭頭已解決

- `story-r02.mmd:61-62` 已把 `A --> B`、`B --> LIMIT` 改為 `A ~~~ B`、`B ~~~ LIMIT`，並在 `linkStyle 11,12,13` 固定 `stroke-width:0px`。
- Story SVG 的 `L_A_B_0`、`L_B_LIMIT_0` 與 UDP/TCP layout edge `L_UOUT_TSTATE_0` 都是 `edge-thickness-invisible`、`stroke-width:0px`、無 `marker-end`；原尺寸 PNG 中 A、B、全圖 boundary 之間沒有可見線或箭頭。
- A 區內的 mapping→policy、allow/block 箭頭仍維持；B 區 UDP 與 TCP 各自只在泳道內左至右。圖不再把 NAT/firewall 故事、transport comparison 與 boundary note串成 wire flow 或處理時序。
- Technical 也把 A/B、B/scope、UDP/TCP lane 間排版關係設成 invisible；SVG 對應 edges 全部 `stroke-width:0px`、無 marker。

## r01 blocking 2：Mapping、policy、allow 與 listener evidence 已解決

- NAT、NAPT 平行卡現在各以 `形成 mapping record` 箭頭進入同一 mapping table 內的 `分層界線`；該界線可見且完整列出 `mapping record ≠ policy evidence`、`mapping ≠ allow`、`allow ≠ listener exists`、`下一項仍須獨立判斷 policy`。
- 分層界線至 firewall policy 只存在不可見 layout constraint：Technical SVG `L_BOUND_POLICY_0` 為 `edge-thickness-invisible`、`stroke-width:0px`、無 marker；不再有 r01 的 `mapping evidence` 箭頭視覺流入 policy。
- Firewall 仍是獨立 diamond；allow 使用尖頭箭頭前往 outside observation，block 使用無箭頭終止線前往 `policy evidence`。Outside node 另顯示 `目的 listener 仍須另證`。
- 全圖底部再次保留相同三條 evidence 界線，並把 mapping table 限在 IPv4/unicast/one-UDP-tuple Traditional NAT 教學表示。實際 PNG 可清楚看到分層框與全圖界線，不需靠 metadata 或 alt 才能取得結論上限。

## r01 blocking 3：UDP/TCP 固定限制已解決

- UDP lane 在 loss/reordering 與 datagram boundary 之外，新增可見限制：`不內建 delivery、duplicate protection 或 ordering 保證`，以及 application 仍有 congestion responsibility。文字存在於 MMD、SVG 與實際 PNG。
- TCP lane 保留 establishment、reliable in-order byte stream 與不保留 message boundary，並新增可見限制：connection 仍可能 failure；不保證 immediate arrival、application processed 或 identity/confidentiality security。
- B 區標題與全圖 scope 均明示只比較 transport service semantics、不排名速度；TCP lane 標題仍明示不連上方 NAT 例，且實際 PNG 沒有任何跨 panel 線。

## 其餘技術回歸

- Technical 仍由同一 host 分叉成兩條平行案例：address-only NAT 保留 `E:49152`，NAPT 改為 `E:62000`；兩者均為 UDP、destination unchanged，未被畫成 NAT→NAPT 串聯或所有 NAT 都改 port。
- `E` 仍只等於 outside observed address；public/global realm 需要另外的 registry allocation + global uniqueness evidence，且仍不保證 route、policy、listener 或 reachability。條件證據留在獨立虛線 observation 區，沒有連到 NAT mapping 成為自動屬性。
- Story 的總機/mapping 與警衛/policy 仍為不同形狀、動詞和 evidence；allow 後保留 `目的 listener？`，block 不連向小華。
- UDP 的 loss/reordering 仍標為「可能」；TCP 沒有 packet boundary、永不失敗或速度優劣暗示。圖中沒有 Chapter 04+ 的正向概念、WebRTC path、ICE/STUN/TURN、signaling、安全媒體、codec、stats 或 gateway 偷渡。

## Frozen text、SVG 語意與 metadata

- 兩份 MMD `accDescr`、兩份 SVG `<desc>` 與 metadata 內兩段 alt 都逐字等於正文凍結 alt；metadata 兩段 caption 也逐字等於正文 caption。
- Story SVG 根為 `id="ch03-story"`、`role="img"`，`aria-labelledby="ch03-story-title ch03-story-desc"`；technical 對應為 `ch03-tech`、`ch03-tech-title ch03-tech-desc`。Title 是核准短名稱，沒有新增技術主張。
- Metadata r02 正確記錄兩份 spec 未變、r01 修訂依據、新版 renderer/尺寸、PNG 只作 preview，以及正式 artifact set 綁定兩份 spec、新 MMD/SVG 與 metadata；沒有把本 Gate 冒充 accessibility Gate。

GATE PASS
