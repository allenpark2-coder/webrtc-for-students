# Chapter 03 Mermaid 圖稿 metadata r02

Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6

> 對應正文：`.work/chapter-03/draft-r02.md`
> 核准規格：`story-spec-r01.md`、`technical-spec-r01.md`，兩檔均未修改
> 規格 SHA-256：story `7738f94d687249b78c27217502203b48870e8dc3eaf696a96e6effdc429ce12d`；technical `22ea90d6ec97a766b65b8602608e52710a427bd5bd3e0673e310f0ed50b1b2ca`
> 修訂依據：`.work/chapter-03/reviews/figure-technical-r01.md`，GATE FAIL
> 本輪候選：`story-r02.mmd/.svg/.png` ＋ `technical-r02.mmd/.svg/.png` ＋本檔
> r01 全部保留；本輪沒有修改正文或 spec。
> 狀態：待 r02 figure technical 與 accessibility Gate；本檔不代替兩個 Gate。

## r02 修正摘要

### Story

- `A --> B` 改成 `A ~~~ B`，`B --> LIMIT` 改成 `B ~~~ LIMIT`；兩者是無方向且不可見的 Mermaid layout constraint。
- UDP 與 TCP 子泳道之間原有的 layout constraint 亦維持不可見。A、B 與全圖比喻邊界現在只靠標題、位置及外框建立閱讀層級，沒有跨 panel 流程箭頭。
- A 區內的 mapping／policy、allow／block 與 listener 關係未改；凍結 caption、alt 與可見文字未改。

### Technical mapping／policy

- NAT 與 NAPT 兩個平行案例各自只以 `形成 mapping record` 箭頭進入 mapping table 內的中介分層界線；中介界線到 firewall policy 只使用 `BOUND ~~~ POLICY` 不可見 layout constraint，不再有 mapping evidence 流入 policy 的可見箭頭。
- 中介界線與全圖底部均直接列出：`mapping record ≠ policy evidence`、`mapping ≠ allow`、`allow ≠ listener exists`；中介界線另明示下一項仍須獨立判斷 policy。
- Firewall 的 `允許` 尖頭箭頭仍指向 outside observation；`阻擋` 維持平頭終止線並停在 policy evidence 節點。Outside node 另明示目的 listener 仍須另證。
- `E = outside observed address`、public/global 的條件式另證與 reachability 限制完全保留。

### Technical transport service

- UDP 泳道新增可見限制：不內建 delivery、duplicate protection 或 ordering 保證，application 仍有 congestion responsibility。
- TCP 泳道新增可見限制：connection 可能 failure；不保證 immediate arrival、application processed 或 identity／confidentiality security。
- Reliable、in-order byte stream、不保留 message boundary、TCP 面板不連 NAT，以及 UDP／TCP 不排名速度均保留。
- A／B 及 B／全圖推論邊界只以不可見 layout constraint 排版，不形成跨 panel 技術流程。

## Renderer、尺寸與輸出

- Renderer：`@mermaid-js/mermaid-cli` 11.16.0，以固定版本 `npx --yes @mermaid-js/mermaid-cli@11.16.0` 執行。
- 未安裝 repo-local dependency，未修改 package manifest 或 lockfile。
- 白色背景、要求寬度 2,000 px；最終 PNG：
  - `story-r02.png`：1,984 × 743 px，寬高比 2.67，符合 `>= 1.5`。
  - `technical-r02.png`：1,984 × 964 px，寬高比 2.06，符合 `>= 1.6`。
- 兩份 source 的 theme 基準字級及全部 node class 字級下限均為 18 px。
- SVG 根 id 維持 `ch03-story` 與 `ch03-tech`，方便正式路徑使用且避免同頁衝突。

## 圖 3-1：總機與警衛是兩個工作

### Caption（正文凍結文字）

**圖 3-1　總機與警衛是兩個工作。**總機只代表 NAT／NAPT 的內外表示與暫時 mapping，警衛另依 firewall policy 決定是否放行；外側觀察位址不因位於圖的外側就成為 public IP address，UDP／TCP 運送帶也只比較 service semantics，不比較速度。

### Alt text（正文凍結文字）

生活故事圖：小明的內側聯絡表示先到總機，總機建立暫時對應，再到依 policy 判斷的警衛，最後指向小華所在的外側網路；下方分列保留一張張邊界但可能遺失或重排的 UDP 明信片，與建立狀態後可靠按序交付、但不保留表單邊界的 TCP 連續紙帶；文字明示 mapping 不等於放行、放行不等於 listener 存在，外側觀察位址不等於 public IP address 或永久身分。

## 圖 3-2：Address 表示、mapping、policy 與 transport 語意分層

### Caption（正文凍結文字）

**圖 3-2　Address 表示、mapping、policy 與 transport 語意分層。**Mapping table 只是一筆受控單播 UDP、內外都只談 IPv4 的 Traditional NAT 教學表示，不是產品表格格式；外側觀察位址 E 與 public/global realm 分開，firewall evidence 另列，TCP 時間線只教 transport service，不宣稱 TCP-through-NAT 行為。

### Alt text（正文凍結文字）

專業圖：由左至右依序是 RFC 1918 private IPv4 host、獨立的 NAT 或 NAPT mapping table、獨立的 firewall policy boundary、outside network；表中以一筆 UDP 教學 tuple 分別示意 address-only NAT 與 address-plus-port NAPT，外側欄以 E 標示觀察位置相關的 outside observed address，並註明只有另有證據確定屬 public/global realm 才可另標 public IP address；下半部以分離時間線呈現 UDP datagram 邊界及可能遺失重排，與 TCP connection establishment 後的 reliable in-order byte stream，且不畫速度排名。

## SVG accessibility

- `story-r02.mmd` 與 `technical-r02.mmd` 都使用 `accTitle`、`accDescr`；兩個 `accDescr` 逐字等於上方對應的正文凍結 alt text。
- Story SVG 根節點為 `role="img"`，以 `aria-labelledby="ch03-story-title ch03-story-desc"` 指向同檔 `<title>`／`<desc>`；technical SVG 對應使用 `ch03-tech-title`／`ch03-tech-desc`。
- Mermaid 原生輸出經與 r01 相同的固定機械式 accessibility 後處理，把預設 role／自動 id 改成規格指定的 image role 與穩定 id；沒有改動圖形、可見文字或凍結描述。
- 關鍵差異同時使用完整標籤、形狀、實線／虛線、箭頭／平頭終止與區塊位置，不只靠顏色。

## 原尺寸、單欄與灰階預覽

- 已實際查看兩張 PNG 原尺寸；Story 的 A／B／LIMIT 之間沒有可見線或箭頭，Technical 的 mapping boundary 與 policy 之間沒有可見線或箭頭。
- Technical 原圖可讀到三條 mapping/policy 邊界、UDP 的 delivery／duplicate／ordering／congestion 限制，以及 TCP 的 failure／immediate／processed／security 限制；沒有新增速度排名或 TCP-through-NAT 連線。
- 已以 FFmpeg 產生並人工查看 1,280 px 寬單欄代理：story 1,280 × 480，technical 1,280 × 622；新增限制與主要關係仍可辨，沒有裁切或重疊。
- 已人工查看兩張 1,280 px 灰階代理；mapping／policy、allow／block、outside evidence、UDP／TCP 與新增限制仍能依形狀、線型、位置和完整文字辨識。
- 本輪未使用整張 raster 的逐像素對比量測，因此不聲稱已量得正式出版頁的 WCAG contrast ratio；正式 accessibility Gate 仍須獨立判定。

## 來源與授權

- 候選由本專案依凍結正文、核准規格與 r01 technical Gate evidence 自行修訂；未使用第三方圖片、照片、圖示或模板，未呼叫 image generation。
- 技術來源範圍沿用正文與 spec 已核准的 RFC 1918、RFC 2663、RFC 4787、RFC 6888、RFC 7857、RFC 8085、RFC 9293、NIST SP 800-41 Rev. 1 與 IANA registry；本輪只恢復 spec 已核准的 visible boundary，不新增來源外主張。
- 最終 attribution 仍依 `bible/source-policy.md` 由主代理於晉升時登記。
- 未讀取、引用、複製或改編排除專案素材。

## 重現命令

MMD 到 PNG 使用以下固定命令；SVG 另加 `-I ch03-story` 或 `-I ch03-tech`，並依上方 accessibility 段落固定 role 與 title/desc id：

```bash
npx --yes @mermaid-js/mermaid-cli@11.16.0 \
  -i .work/chapter-03/figures/<stem>.mmd \
  -o .work/chapter-03/figures/<stem>.<ext> \
  -b white -w 2000
```

正式 r02 artifact set 應綁定兩份未修改 spec、兩張圖各自的 r02 MMD／SVG，以及本 metadata-r02；PNG 保留作 review preview。兩個 figure Gate 都必須綁定新 artifact-set hash。
