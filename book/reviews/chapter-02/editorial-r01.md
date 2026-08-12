Gate: editorial
Round: 1
Content-SHA256: a3fc4b1eb2913194eac7f5a2c80045675c8c5b30305c598b200207fd49adde69
Result: GATE PASS

# Chapter 02 最終編輯審查

## 審查範圍與候選鏈

- 受審正文為 `.work/chapter-02/draft-r03.md`，重算 SHA-256 與頁首綁定值一致。
- `structure-r03`、`body-technical-r02` 均通過且綁定同一正文 hash。
- `figure-technical-r02`、`figure-accessibility-r02` 均通過，並共同綁定圖候選集 `c6a76a305a02b8c6c12f1bcc2c2bc5975101169b3272c7cf1242b41f974c8a1d`；重算七個映射檔所得 artifact-set hash 相同。
- 本審查另核對 `scope-r02.md`、正式計畫 Chapter 01–03、Chapter 01 最新讀者狀態、全部 bible、兩張圖的規格／metadata／MMD／SVG 與實際 PNG 預覽。正式 Lab 為不適用，本章只有章內 localhost 安全觀察。

## 學習目標、難度與知識依賴

- 正文完成 Chapter 02 的全部目標：辨認特定 HTTP localhost 連線中的 client/server 角色；用版本中立的最小共同模型區分 IP address 與 port；以相對範圍理解 LAN/WAN；把 packet 理解為有限資料單位；最後以受限證據回答「誰、在哪裡、從哪個入口送出什麼」。
- Chapter 01 已知的「證據範圍必須配合結論」被自然延伸到位址、入口與封包觀察；沒有假定讀者已懂 Chapter 03 或更後面的網路機制。
- 難度由生活故事、正式名稱、術語卡、兩張圖、資料流、最小觀察與理解題逐步增加。命令均可直接照錄，且另提供紙上替代路徑，因此未要求讀者具備 Linux 管理經驗。
- 本章沒有把 client/server 寫成永久機器類型，沒有把 IP address 當人或裝置的永久身分，沒有把 port 當實體洞口，也沒有宣稱 packet 保證送達、順序、唯一性或時效性。
- LAN/WAN 依相對有限範圍與通常更大地理範圍／更多獨立使用者說明，保留「沒有單一距離門檻」的界線，沒有以管理邊界取代正式分類。

## 固定結構與七個首次術語

- 正文含依序且僅一次出現的固定 14 段，並另有「本章參考資料」。五題理解題與五組解析一一對應。
- 七張術語小卡完整且唯一：用戶端、伺服器、網際網路協定位址、連接埠、區域網路、廣域網路、封包。每張均具正式名稱、白話解釋、生活比喻、成立處、失真處、技術邊界、本章位置、後續用途與快速檢核。
- 正文把 client/server 明確限制在本章的 HTTP localhost connection 情境，並說明同一程式可在不同連線交換角色；IPv4／IPv6、IPv6 多位址與 SLAAC 位址生命週期的適用範圍也有明確界線。
- 章內重複屬教學鷹架：同一組概念依故事、正式命名、卡片、圖、資料流、觀察與理解題重新組織，而非新增未審查主張。

## 故事、比喻與人物一致性

- 小明／小華延續 bible 的固定人物；未增加新的具名常駐角色。
- 「地址／辦公室入口／文件」比喻分別承接 IP address、port 與 packet，並在正文與小卡中說明比喻會失真的地方：位址不等於身分、入口不是實體洞、資料單位不附帶傳送保證。
- 故事中的 client/server 角色交換綁定不同連線，沒有暗示角色是設備永久屬性；LAN/WAN 案例也明示情境邊界不能取代真實網路分類。

## 圖引用與教學功能

- 正文兩個引用會由未來正式路徑 `book/chapters/chapter-02.md` 正確解析至 story 與 technical SVG；alt text 與 caption 和通過 Gate 的 metadata、圖規格及 SVG 內容一致。
- 生活圖支援「同一程式可在不同連線交換角色」、位址與入口分工，以及 LAN/WAN 的相對範圍；專業圖則把 IP address、port、packet 與網路範圍拆成可逐項辨識的結構。
- 實際預覽與 SVG 語意顯示關係不只靠顏色表達；technical r03 已以連接結構避免把封包卡內部誤讀成兩條未標方向的資料路徑。兩張圖沒有引入正文尚未教會的技術機制。

## 章內觀察、安全閉環與正式 Lab 判定

- 正式累積 Lab 依 roadmap 自 Chapter 04 開始，因此 Chapter 02 不需 Lab artifact；本章 localhost 觀察是章內最小證據活動，不應被誤列為正式 Lab。
- 活動限制在單一自有電腦、`127.0.0.1`、一般使用者與指定非特權連接埠；明確禁止掃描、區網／公網、production、他人設備與管理員權限操作。
- 故障是把服務由 A 入口移至 B；正文分別給出基線、成功預期、故障證據、停止條件、替代連接埠、恢復至 A、cleanup 與 cleanup 驗證，形成完整且可回復的安全閉環。
- 執行環境聲明誠實區分已執行的 Ubuntu 22.04.5／Python 3.10.12 與僅作官方套件背景的 Ubuntu 24.04／Python 3.12.3 family；工具行為不同時要求停止，不把未執行平台宣稱為已驗證。

## 來源與 Chapter 03 銜接

- 本章參考資料列出 11 筆第一手來源，具版本／status／updates 或範圍說明與查核日期；其支援範圍與 `spec-baseline.md`、`source-policy.md` 一致。
- RFC 1122 的 TCP requirements 僅出現在來源範圍排除說明，未被當成本章教學概念；RFC 6335 與現行 BCP 165／RFC 7605 的關係亦有交代。
- 結尾只提出「不同位址可見性」與「網路規則可能允許或阻擋」作為問題，沒有提前教 Chapter 03 才首次出現的 private/public IP、NAT、mapping、firewall、UDP 或 TCP，也未提前使用後章 signaling、ICE、STUN/TURN、媒體安全或 codec 概念。
- Chapter 03 可直接承接本章已建立的 address、port、packet 與證據邊界，進一步解釋跨網路路徑為何會受轉換與規則影響；銜接清楚且沒有向後依賴。

## 晉升判斷

Chapter 02 的學習目標、固定結構、術語首次教學、圖文映射、來源、安全觀察與章際依賴一致；未發現需退回 storyteller、domain-expert 或 diagram-designer 的編輯阻擋項。此候選可交由主代理建立正式 manifest 候選並執行 `scripts/validate_kit.py`；本 Gate 本身不代表已完成正式晉升、glossary 或 state 更新。
