Gate: body_technical
Round: 2
Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69
Result: GATE PASS

# Chapter 02 正文技術審查 r02

## 審查範圍

- 受審正文：`.work/chapter-02/draft-r03.md`；重算 SHA-256 與本 Gate 綁定值一致。
- 回歸依據：`scope-r02.md`、`structure-r03.md`、`body-technical-r01.md`、更新後全部 `bible/*.md`（含 `spec-baseline.md`）、`book/plan.md` Chapter 02／03 與 `state/current/`。
- 本輪集中驗證 r01 四組必改、NIST LAN／WAN、IANA live registry、兩個未來正式圖路徑與完整 Lab；未修改受審檔，也未讀取排除專案。

## r01 必改逐項回歸

### 1. HTTP connection 的 client／server 角色：已解決

位置：`draft-r03.md:19,31,43,303,309-311,346`。

- RFC 9110 §3.3 直接定義：建立該 HTTP connection 的參與者是 client，接受該 connection 的參與者是 server；角色只針對特定 connection，同一程式可在不同 connection 中扮演不同角色。
- 正文現在每次提出角色交換都限定為「本章 localhost HTTP connection」，並明說不得外推為所有通訊方式的廣義角色定義；來源採用範圍和 RFC 原文邊界一致。
- RFC Editor 將 RFC 9110 列為 STD 97／Internet Standard。章末來源的 status、章節定位與限定用途正確。

### 2. IP address 的 IPv4／IPv6 共同模型與 IPv6 邊界：已解決

位置：`draft-r03.md:20,45,85-93,159-165,303,315-317,339,341-343`。

- RFC 791 的 IPv4 header 與 RFC 8200 的 IPv6 header 都具有 source／destination address 欄位；正文只把這個交集用作版本共同模型，沒有再把 RFC 8200 的 IPv6 專屬 address 定義外推為所有 IP 版本。
- RFC 4291 §2.1 支援 IPv6 位址配給介面，以及單一介面可有多個 IPv6 位址。RFC Editor 記錄為 Draft Standard、Obsoletes RFC 3513、Updated by RFC 5952／6052／7136／7346／7371／8064，與正文一致。
- RFC 4862 明確定義 IPv6 SLAAC 位址的 preferred／valid lifetime；valid lifetime 到期後位址失效。RFC Editor 記錄為 Draft Standard、Obsoletes RFC 2462、Updated by RFC 7527／9762，與正文一致。正文只把它用作 IPv6 自動設定位址的生命週期例子，並明說不能外推為所有 IP 位址採相同變化機制。
- 「IP address 不是人的永久身份」因此是由明示的限定例子反駁永久身份推論，不是宣稱全部位址都由 SLAAC 或同一機制更換。

### 3. 實跑環境與官方背景：已解決

位置：`draft-r03.md:198,206,213-223,349`。

- 正文透明區分本輪唯一實跑環境 Ubuntu 22.04.5 LTS／Python 3.10.12，和 Ubuntu 24.04 官方 `python3` 套件的 Python 3.12.3 family 背景；沒有宣稱後者已執行或把 3.10.12 冒充 Noble 預設。
- 新增的 `cat /etc/os-release` 與 `python3 --version` 讓讀者先記錄自己的環境；遇到命令、輸出或 cleanup 差異即停止的邊界可重現且安全。
- 本輪逐字執行結果見下節。實際輸出為 `Ubuntu 22.04.5 LTS (Jammy Jellyfish)` 與 `Python 3.10.12`，和正文聲明完全一致。

### 4. RFC 1122／RFC 9293 與 BCP 165 關係：已解決

位置：`draft-r03.md:53,339-346`。

- RFC Editor 目前列 RFC 1122 為 STD 3／Internet Standard、`Updates RFC 793`，並列九份 `Updated by`，含 RFC 9293。RFC 9293 取代 RFC 1122 中的 TCP requirements；正文已逐項記錄，且只採 Internet host 分層／互連背景，不採、不教該 TCP requirements，未提前越入 Chapter 03。
- RFC 6335 是 Best Current Practice、BCP 165 的一部分，並 Updates RFC 2780／2782／3828／4340／4960／5595。現行 BCP 165 同時包含 RFC 6335 與 RFC 7605；RFC 7605 補充但不 Updates RFC 6335。正文已正確拆開這些關係，沒有再把 RFC 6335 單獨等同整個現行 BCP 165。

## 指定新增來源與圖引用

- **LAN／WAN：充分。**NIST SP 800-82 Rev. 3 glossary 把 LAN 描述為涵蓋相對有限區域的網路；WAN 則通常涵蓋較大地理區域、服務比 LAN 更多的獨立使用者。`draft-r03.md:49,109-133,147,347` 保留「相對／通常」，明說沒有單一公里數門檻，也不再採 r01 未受支撐的「管理範圍」作正式定義。
- **IANA 日期：正確。**2026-08-12 直接讀取官方 registry XML，根層 `<updated>` 為 `2026-08-11`；同一 registry 說明 Dynamic／Private Ports 為 49152–65535，並按 transport protocol 區分。`draft-r03.md:348` 的日期與 49152／49153 選擇正確，且正文沒有把登錄誤寫為服務可信、可達或正在執行。
- **未來正式圖路徑：可接受。**`draft-r03.md:145,159` 的兩個引用從未來正式正文 `book/chapters/chapter-02.md` 分別解析到 `book/figures/story/chapter-02-address-and-range.svg` 與 `book/figures/technical/chapter-02-ip-port-packet.svg`。這兩個 SVG 尚未存在，因此本 Gate 不把它們當作已完成 artifact 或已渲染證據；後續仍須經圖規格、artifact technical 與 accessibility Gate。
- **alt／caption 技術邊界：可供後續圖稿遵循。**生活圖只表達 LAN／WAN 的相對差異、connection-specific HTTP 角色與無固定距離門檻；技術圖只拆分 IP address／port／packet，並明示 packet 不等於送達、圖上路徑不等於實際路徑。它們未新增 NAT、routing algorithm、TCP／UDP、WebRTC 或其他後章機制。正式圖若偏離這些主張，必須由下游圖 Gate 攔截。

## 精確命令執行證據

執行於新建隔離暫存目錄，只綁定 `127.0.0.1`，使用一般使用者權限及固定 A=`49152`、B=`49153`。兩個 port 均可用，未啟用替代配對、未掃描，也未終止任何未知程序。

1. **環境與建立內容：通過。**逐字執行 `cat /etc/os-release`、`python3 --version`、`mkdir -p ch02-local-test` 與正文的 `Path.write_text(...)`；輸出 Ubuntu 22.04.5 LTS／Python 3.10.12，頁面含 `CH02-LOCAL-ONLY`。
2. **A baseline：通過。**逐字執行 `python3 -m http.server 49152 --bind 127.0.0.1 --directory ch02-local-test`；本機 HTTP request 取得正確自製頁面，server 留下 `127.0.0.1` 的 `GET / HTTP/1.1` 200 紀錄；以 `Ctrl+C` 正常停止自己啟動的 A。
3. **停止 A／啟動 B：通過。**逐字在 49153 啟動同一服務；A request 得到 `URLError`，B 取得正確識別字且 server 留下 200 紀錄，符合「目標服務從 A 移到 B」的有限結論；以 `Ctrl+C` 停止 B。
4. **恢復 A：通過。**逐字重啟 A；A 再次取得正確識別字，B 得到 `URLError`；server 留下 A 的 200 紀錄，證明唯一故障改動已復原；再以 `Ctrl+C` 停止 A。
5. **Cleanup：通過。**逐字執行正文 `Path.unlink(missing_ok=True)`／`rmdir()` 命令；`ch02-local-test` 不存在，A、B 均無回應，之後移除本 Gate 自建的空暫存目錄。沒有測試程序殘留。
6. **人工瀏覽器限制：透明。**本輪環境沒有可用的圖形瀏覽器／DevTools，因此以 Python 標準庫本機 HTTP client 驗證 response body、失敗／成功切換及 server terminal evidence；未聲稱取得位址列或 Network 面板證據。讀者流程中的瀏覽器四項 baseline 仍需在人工執行時觀察，但此限制不阻擋精確命令、拓撲、故障、恢復與 cleanup 的技術可行性。

## 其他回歸

- 安全與停止規則完整：localhost-only、禁止 `0.0.0.0`／LAN／public／production／他人設備／管理員權限／掃描，port 占用使用固定替代配對或停止，不終止未知程序；故障只移動自建服務，復原與 cleanup 目標明確。
- 證據結論上限正確：成功、失敗與復原只判斷「這個自建測試服務」當時是否在指定 port 回應，不推論整台主機、整個網路、WebRTC 或未教傳輸規則。
- Chapter 03+ 邊界維持：private/public IP、NAT、mapping、firewall、UDP、TCP 等沒有被正式命名或解釋；HTTP、localhost、`http.server` 與 Network 面板被限定為本機觀察工具／情境。
- IP／port／packet、LAN／WAN 與門牌／入口／文件比喻都附有反例邊界；沒有把 port 畫成實體洞、把 IP 當永久身份、把 packet 當送達保證或把示意道路當實際拓撲。

## 結論

r01 四組必改均已以第一手來源、明確適用範圍及相符實跑證據完整解決；新增 NIST／IANA 主張、未來圖路徑與 alt／caption 也未越過正文及後章邊界。正文技術 Gate 通過。
