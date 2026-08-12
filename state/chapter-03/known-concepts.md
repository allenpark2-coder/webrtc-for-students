# 讀者已學過的專有名詞清單

- 即時通訊、WebRTC、對等端（peer）。
- 用戶端（client）、伺服器（server）、網際網路協定位址（IP address）、連接埠（port）、區域網路（LAN）、廣域網路（WAN）、封包（packet）。
- 私有 IP 位址（private IP address）：RFC 1918 指定給 private internets 使用的三段 IPv4 address space。
- 公用 IP 位址（public IP address）：公用／全域 address realm 中，由 IANA 或相當 registry 分配而具全域唯一性的 IP address；不等於任意外側觀察值或可達保證。
- 網路位址轉換（NAT）：在不同 address realm 之間轉換或對應 IPv4 address 表示。
- 網路位址與連接埠轉換（NAPT）：Traditional NAT 中同時轉換 IPv4 address 與 TCP／UDP port 的子類。
- 對應（mapping）：NAT／NAPT 為這次內外位址表示維持的狀態關聯。
- 防火牆（firewall）：依 policy 對特定 traffic flow 允許或阻擋的控制。
- 使用者資料包協定（UDP）：保留 datagram 邊界，但不保證送達、去重或順序，應用仍有壅塞責任。
- 傳輸控制協定（TCP）：提供 connection-oriented、reliable、in-order byte-stream service，不保留應用 message 邊界。

讀者另已建立以下心智模型：NAT mapping 與 firewall policy 是不同證據層；外側觀察位址不等於 public/global 位址；mapping 不等於 allow，allow 不等於 listener 存在；UDP／TCP 應以 service semantics 與證據比較，不能抽象排名速度；單一 listener 的失敗不能證明 NAT、firewall 或整個網路故障。
