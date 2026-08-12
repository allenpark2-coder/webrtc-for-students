Gate: body_technical
Round: 2
Content-SHA256: e23c8195813023bfcc71383930a025bea2f132bfbdf4248f1346d0cfeb5a8cf6
Result: GATE PASS

# Chapter 03 Body Technical Review — Round 02

## 審查邊界

- 已獨立重算 `.work/chapter-03/draft-r02.md`，SHA-256 與頁首綁定值相同。
- 已逐行核對 r01→r02 diff、`body-technical-r01.md` 的 blocking 與非阻擋建議，並回歸 scope、source audit、規範基線、roadmap、讀者既有概念及 r01 已通過技術項。
- 本輪沒有修改受審正文或其他專案真實來源；未讀取或引用排除專案。兩個未來 SVG 仍只審正文的 alt、caption 與圖稿約束文字。

## r01 blocking 回歸：完整解決

r01 的唯一技術阻擋是把任意 NAT 外側觀察值定義成 public IP address。r02 已把兩個維度完整分開，且沒有留下互相矛盾的舊句：

1. `draft-r02.md:42-44` 現依 RFC 2663 §2.7，把 public IP address 限定為 public/global address realm 中、由 IANA 或相當 Internet address registry 分配而具全域唯一性的位址；另把 outside observed address 定義為觀察位置相關的輔助說法。文字明示外側值可能仍是 RFC 1918 private-use 或其他非全域唯一位址，只有另有 public/global realm 證據時才能再標為 public。
2. 同段保留 IANA registry 支持的負向判斷：非 RFC 1918 仍可能是 loopback、link-local、documentation、shared 等 special-purpose；registry 中的 prefix 也不保證特定 local/global context 的 routability。因此「非 private」不能推成 public 或可達。
3. `draft-r02.md:72-81` 的 public IP 候選小卡同步改為 registry allocation／global uniqueness 維度，來源同時列 RFC 2663 §2.7 與 IANA registry；真正作用、常見誤解與適用範圍都把 outside observation 分開。
4. 生活故事圖文字 `:158-164` 明示 outside observed address 不因位於圖外側就成為 public IP；專業圖文字 `:168-174` 改用符號 `E` 表示 outside observed address，禁止把 `E` 自動標為 public，只有額外的 global-uniqueness evidence 才能另標 public/global realm。原本會誤導的符號 `P` 已完全移除。
5. 流程 `:183-186` 先記錄 outside observation，再以獨立 registry/global-uniqueness evidence 判斷 public/global realm；即使已確定 global uniqueness，仍不能代替 route、policy、listener 或 reachability evidence。
6. 第 1 題及解析 `:514-516` 同時納入「非 RFC 1918」與「某層外側觀察值」兩個反例，正確要求額外證據，且沒有再把 outside observation 當 public 定義。
7. 章末 RFC 2663 採用範圍 `:545` 與 IANA registry 採用範圍 `:552` 和正文一致。全文搜尋 public/global/outside/外側觀察後，未發現舊的「public = 任意外側觀察值」殘留。

這組修訂符合 RFC 2663 的有限 IPv4 taxonomy，也正確涵蓋 double NAT 或 CGN subscriber-side 外側值可能仍非 public/global 的情況；同時保留「global uniqueness 不等於實際可達」的重要邊界。

## r01 非阻擋改善回歸

- `draft-r02.md:54` 已移除容易和 best-effort 混淆的「盡力偵測」，改為 RFC 9293 支持的 loss/error detection、sequence、retransmission 與 reliable in-order byte-stream service，並明示無法維持時 connection 仍可能失敗。
- `draft-r02.md:555-556` 已加入 Linux `network_namespaces(7)` 及 iproute2 `ip-link(8)`、`ip-address(8)`、`ip-route(8)`，採用範圍只到 namespace 隔離／lifetime、loopback 啟用及 address/route 檢查；沒有拿這些工具輸出證明 NAT、firewall 或 Internet 行為。

## 程式與執行 evidence

- r02 的 Python 程式區塊重新抽取後 SHA-256 為 `e9b0e0723bc8bfbeac48bb20ce3b0699a6feceb08454d9a20a6f00bfdc6c1c7e`，與正文宣告及 r01 實際執行版本完全相同；r01→r02 diff 沒有改動任何環境命令、listener/client 命令、故障、復原或 cleanup 命令。
- 因 artifact 完全相同，本輪引用 `body-technical-r01.md` 的實際執行 evidence：Ubuntu 22.04.5 LTS/x86_64、Python 3.10.12、util-linux 2.37.2、iproute2 5.15.0；新 namespace 僅有啟用的 loopback 且 route 為空；TCP/UDP baseline、逐一停止、另一 transport 持續成功、逐一復原均符合 exit/marker/log 預期；cleanup 後 source、兩份 log、暫存目錄、四個已知 PID 與 probe process 均不存在。
- 結論仍正確限制在該 namespace、tuple、transport、listener 與時間窗；UDP send success 不等於接收，停止 listener 不模擬 NAT/firewall，也不支持一般速度、可靠性、Internet 或 WebRTC 結論。

## 其餘技術回歸

- RFC 1918、2663、4787+6888/7857、8085、9293 的 status、updates/obsoletes 與採用邊界未被改壞；NIST SP 800-41 Rev. 1 與 IANA registry 的日期及有限用途一致。
- NAT、NAPT、mapping、firewall 仍分層；具體 mapping 例明確限單播 UDP、內外均為 IPv4 的 Traditional NAT 情境，不建立 TCP-through-NAT、IPv6 NAT 或完整 firewall behavior 教學。
- UDP/TCP 只比較 datagram 與 reliable in-order byte-stream service semantics，不排名速度；message boundary、loss/duplication/reordering、application congestion responsibility、TCP failure與應用處理／安全界線均保留。
- 兩張未來圖的文字仍分開 mapping/policy 與 UDP/TCP，沒有加入 Chapter 04+ API、ICE/STUN/TURN、signaling、DTLS/SRTP、RTP/RTCP、codec 或其他後章依賴。
- Namespace 安全前提、停止條件、固定 target/port、marker、PID 身分、timebox、逐一故障／復原、紙上替代、精確 cleanup 與 evidence 上限均未變。

GATE PASS
