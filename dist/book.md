# Chapter 01：為什麼視訊通話不是「把影片寄過去」

## 1\. 今天遇到什麼問題？

小明按下視訊通話按鈕時，畫面不一定立刻出現。有時他先看到自己，過一會兒才看到小華；有時影像出現了，聲音卻沒有；還有時兩邊原本聊得很順，幾分鐘後畫面忽然停住。

如果視訊通話只是「把影片寄過去」，事情似乎不該這麼麻煩。小明先錄完一段影片，等檔案準備好，再交給小華。小華收到完整檔案後按下播放，就能從頭看到尾。這和傳送一張照片很像：內容先完成，接著才傳送，收完之後再觀看。

可是通話時，小華不想等小明講完十分鐘、收完一個完整檔案，才回答第一句話。她會在聽見問題後立刻回應；小明也會看著她的表情改變說法。新的聲音與畫面一直在產生，雙方也一直在接收和回應。等待如果太久，兩個人就會搶話、停頓，甚至以為對方沒有聽見。

因此，視訊通話的核心不是「把一份完成的影片交出去」，而是讓雙方能在內容持續產生時，持續交換資訊並互相回應。這件事至少留下六個待解問題：當下的聲音與畫面從哪裡來？雙方怎麼交換準備通話所需的協調資訊？資料怎麼找到能到達對方的方式？通話內容與協調資訊怎麼受到保護？正在產生的聲音與畫面怎麼持續送出？網路情況改變時，互動品質怎麼盡量維持？

這六問現在只是全書地圖，不是六個已經解開的答案。它們也不一定照順序發生；真實通話中，多件事可能交錯或同時進行。本章的任務，是先看清問題的形狀。

## 2\. 生活故事

小明準備和小華討論隔天的科展報告。他想到一個簡單方法：「我先把想說的話錄成影片，再把影片寄給你。」

第一段影片錄了三分鐘。小明錄完、檢查完，再交給小華。小華看完後才發現，她在第一分鐘就有問題：「你說的測量結果，是星期一還是星期二的？」於是她再錄一段影片回覆。等小明收到，兩人已經花了不少時間，卻還停在第一個問題。

「如果我在你說到第一分鐘時就能問呢？」小華說。

兩人改成持續對話。小明說到日期時，小華立刻追問；小明聽見後馬上修正。小華拿起一張圖，小明也能當場指出哪個數字需要重算。這次，資訊不是先做成一份完整作品才交付，而是在產生的同時不斷往返。

不過，他們很快又遇到新問題。小明的畫面出現了，不代表小華的聲音一定已經送達；小華看得到小明，也不代表小明看得到小華。兩人還得先知道彼此都準備好了、設法讓資料到達、避免內容被不相干的人看見，並在網路忽快忽慢時繼續交談。

這個「寄送完成影片」與「持續對話」的比喻，在一個範圍內成立：前者凸顯內容先完成再傳送，後者凸顯雙方邊產生、邊交換、邊回應，等待時間也會影響互動。

但比喻從這裡開始失真。真正的即時通訊不是小明和小華親手逐句搬運資訊，也不是沿著一條永遠不變的道路前進。瀏覽器會同時處理多種工作、狀態與回饋；故事中的「直接說話」也不能用來推論資料實際怎麼走。故事幫我們提出問題，不能代替真正的技術說明。

## 3\. 如果你是工程師，你會怎麼解？

先別急著想某個產品名稱，也別猜要按哪個按鈕。假設你只能寫下一份「通話必須做到什麼」的清單，你會列哪些項目？

你可以先問：

1.  **怎麼取得此刻的內容？** 雙方都要能取得當下的聲音；需要畫面時，也要取得當下的影像。
2.  **怎麼確認雙方能合作？** 兩邊必須交換建立通話所需的協調資訊，而不是各自準備後就期待事情自動完成。
3.  **怎麼讓資料到達？** 裝置可能位於不同環境，資料需要找到可用的到達方式。
4.  **怎麼保護通話？** 建立通話所需的資訊，以及真正交換的聲音與畫面，都不能被當成毫無保護的公開內容。
5.  **怎麼持續交換？** 內容尚未全部產生，系統就要讓已產生的部分持續前進，讓另一端能及時接收。
6.  **情況變差時怎麼辦？** 可用條件可能隨時間改變，系統要盡量維持能互動的結果，而不是只在最理想的一刻成功。

這份清單刻意不回答「內部到底怎麼做」。它的價值是讓我們不會把某一個成功現象誤認成全部成功。例如，看到小華的畫面，只能證明「目前有一項可見現象」；它不能單獨證明小華聽得到小明、小明聽得到小華、兩邊畫面都正常、所有協調都正確，或品質接下來都不會改變。

工程師面對複雜系統時，常先把「想要的結果」和「支持結果的證據」分開。前者說明目標，後者幫助判斷哪些部分真的成立。本章不要求你解開六問，只要求你不要漏問。

## 4\. 正式技術名稱

第一個名稱是**即時通訊（Real-Time Communication）**。在本書中，它指資訊產生後，在足以支援人類互動的時間內持續交換。重點是「持續」與「能互相回應」，不是保證完全沒有等待、永遠不失敗或品質固定不變。

第二個名稱是**網頁即時通訊（Web Real-Time Communication, WebRTC）**。WebRTC 提供一組標準化的瀏覽器能力與處理模型，讓瀏覽器及相容的一端能建立即時的聲音、畫面或資料通訊。本章只看全貌，不拆解內部做法。

WebRTC 不是一部萬能機器，也不是一種影片檔格式。它不代表只要出現一個按鈕，所有準備、協調、到達方式、安全與品質問題就會自動消失；它也不保證資料一定以某一種固定方式在兩部裝置之間移動。

第三個名稱是 **peer**，本書譯為**對等端**。Peer 是參與一次即時通訊的一端。在本章故事中，小明端和小華端各代表一個瀏覽器／peer 角色。

Peer 描述的是一次通訊中的角色，不等於一個人，也不等於一台永遠固定不變的機器。名稱裡的「對等」更不保證資料一定直接在兩部裝置之間傳送；真正的到達方式要在後續章節用證據判斷。

本章採用的 WebRTC 技術定位來自 W3C 於 2025 年 3 月 13 日發布的 WebRTC Recommendation。全書問題地圖也參考 2021 年 1 月發布的 RFC 8825；它的狀態是 Proposed Standard，屬於 Internet Standards Track。它是一份 applicability statement 與規範 roadmap，本身不另行定義 protocol。

## 5\. 專有名詞小卡

以下三張都是本章提出的候選小卡；在本章所有審查完成前，它們還不會進入全書正式詞庫。

### 即時通訊

英文：Real-Time Communication  
中文：即時通訊  
一句話：資訊產生後，在足以支援互動的時間內持續交換  
生活比喻：小明說話時，小華不必等完整影片做完，就能聽見、理解並回應  
真正作用：描述一種重視持續交換與互動時間的通訊需求  
常見誤解：「即時」不代表完全零等待、永不失敗或品質永遠相同  
適用版本／範圍：本書的瀏覽器即時影音與資料通訊入門範圍  
首次出現章節：Chapter 01  
來源：<https://www.rfc-editor.org/rfc/rfc8825.html>

### WebRTC

英文：Web Real-Time Communication  
中文：網頁即時通訊  
一句話：讓瀏覽器與相容端點建立即時通訊所需的一組標準化能力與處理模型  
生活比喻：小明與小華要持續對話，需要一整套互相配合的準備與處理能力  
真正作用：支援瀏覽器建立即時聲音、畫面或資料通訊；本章只介紹整體定位  
常見誤解：WebRTC 不是單一設備、單一傳送規則、視訊檔格式，也不保證固定的資料到達方式  
適用版本／範圍：W3C WebRTC Recommendation，2025-03-13 版本；本書以瀏覽器情境為主  
首次出現章節：Chapter 01  
來源：<https://www.w3.org/TR/2025/REC-webrtc-20250313/>

### Peer

英文：Peer  
中文：對等端  
一句話：參與一次即時通訊的一端  
生活比喻：故事中的小明端與小華端各代表一個參與通話的角色  
真正作用：指出一次通訊中的參與端角色  
常見誤解：peer 不等於一個人或一台永久固定的機器，也不保證資料直接在兩台裝置之間傳送  
適用版本／範圍：本章用於描述瀏覽器／peer 角色；實際資料到達方式留待後章  
首次出現章節：Chapter 01  
來源：<https://www.w3.org/TR/2025/REC-webrtc-20250313/>

## 6\. 第一張圖：生活故事圖

本章的第一張圖要幫你比較兩條時間線。

![上下兩條由左向右的時間線比較兩種模式。上列「完整影片寄送」中，小明先準備完整影片，越過「影片完成」界線後才一次交付；小華前段等待，收到、觀看後才回應。下列「持續雙向互動」中，四個事件依時間向右排列，文字箭頭方向交替：小明向小華說明日期、小華向小明追問星期一或星期二、小明向小華修正為星期二、小華向小明指出數字要重算。圖下註明，文字箭頭只表示互相回應的節奏，不代表資料實際路徑。](../book/figures/story/chapter-01-file-versus-conversation.svg)

\*\*圖 1-1　完成檔案寄送與持續雙向互動的時間差。\*\*上列必須先準備並交付完整影片，小華之後才能觀看與回應；下列則在內容持續產生時交錯交換與回應。文字箭頭只表示故事中的互動節奏，不表示真實資料路徑。

第一條是「完整影片寄送」：小明先把內容全部準備完成，接著交出完整影片，小華收到後才開始觀看與回應。時間線上會有明顯的「準備完畢」界線。

第二條是「持續對話」：小明與小華產生的聲音、畫面和回應交錯出現。兩人不需要等一方完成整段內容，才開始另一方的回應。

讀圖時只要抓住一件事：**完成檔案的傳送以內容先完成為前提；即時互動則在內容持續產生時就持續交換。**

這張生活圖不表示真正的技術架構，也不表示資料沿固定道路移動。圖中的人、片段與時間線只是用來比較互動節奏；不能拿來判斷通話內部使用了哪些元件，或資料實際經過哪裡。

## 7\. 第二張圖：專業圖

第二張圖是全書的最小鳥瞰圖。左邊是 Browser A（小明端），右邊是 Browser B（小華端）。兩端之間只畫兩種概念性的交換：

![Browser A（小明端）位於左側，Browser B（小華端）位於右側，兩個端點框大小與樣式相同。中央上列是帶點狀線條字形的「左箭頭、協調資訊、右箭頭」，下列是帶實線字形的「左箭頭、即時影音、右箭頭」。主圖下方另有警語，說明雙向文字箭頭只表示雙方都需交換，不表示直接傳送或實際資料路徑；這是概念鳥瞰，實際拓撲、路徑與內部做法於後章拆解。](../book/figures/technical/chapter-01-browser-concept-overview.svg)

\*\*圖 1-2　WebRTC 通話的最小概念鳥瞰。\*\*Browser A（小明端）與 Browser B（小華端）之間分列協調資訊與即時影音兩種概念交換；中央文字箭頭只區分用途並提醒雙方都需交換，不表示直接傳送、實際拓撲、資料路徑或內部實作。

  - \*\*協調資訊：\*\*雙方為建立通話而需要交換的資訊。
  - \*\*即時影音：\*\*通話進行時持續交換的聲音與畫面。

兩種線都必須是雙向概念，提醒我們不能只檢查一邊。但箭頭不代表真正的連線方向、經過哪些設備或使用哪種傳送方式。圖中也會保留「細節於後章拆解」的標記。

這張圖的目的，是先把「建立通話所需的交換」和「通話中的聲音與畫面」分開看。它不是完整架構，更不能由兩個瀏覽器之間的一條線推論資料一定直接傳送。

## 8\. 流程、狀態或資料怎麼走？

現在把六個問題排成方便閱讀的提問地圖。請注意，這不是一條固定的單向流水線；通話期間，某些工作會同時進行，也可能因情況改變而再次處理。

### 提問一：如何取得當下內容？

雙方要先有「現在」的聲音與畫面可供交換。若只拿到小明之前錄好的影片，得到的是可播放內容，卻不是正在發生的互動。

### 提問二：如何交換協調資訊？

小明端準備好了，不代表小華端自動知道。雙方需要交換足以建立通話的協調資訊。本章只知道「需要交換」，不討論資訊格式與交換方法。

### 提問三：如何找到能到達的方式？

兩端可能位於不同環境。系統需要找出資料能否到達，以及目前可採用什麼方式。這個問題不能靠故事中兩人「面對面」的畫面回答。

### 提問四：如何保護交換內容？

通話不是公開廣播。建立通話所需的資訊，以及雙方交換的聲音與畫面，都有安全需求。本章不把「保護」綁定為某一種特定做法，也不聲稱只靠一個圖示就能證明安全。

### 提問五：如何持續送出正在產生的內容？

新的內容會一小段一小段持續出現。接收的一端也要持續處理，而不是等待一個永遠還沒錄完的完整檔案。

### 提問六：如何面對條件改變？

網路情況、裝置負擔或使用者操作都可能改變可見結果。系統要盡量維持互動；工程師則需要觀察改變前、改變中與恢復後的證據。

這六問共同描述了「視訊通話為什麼比寄影片複雜」。任何一問都不是完整通話的同義詞，任何單一成功現象也不能替其餘五問作證。

## 9\. 最小實作或最小可觀察練習

本章還沒有教授足以安全寫出 WebRTC 程式的內容，因此**沒有正式 Lab，也不寫程式**。我們先練習一件更基礎的工程能力：把「我覺得通了」改寫成可逐項觀察的結果。

請準備下面的觀察表。若沒有安全的自有測試環境，直接使用表後的紙上情境，學習成果完全相同。

| 觀察項目          | 正常時          | 自己 mute 後    | unmute 恢復後   |
| ------------- | ------------ | ------------ | ------------ |
| 小明是否聽見小華      | 有／無／未知       | 有／無／未知       | 有／無／未知       |
| 小華是否聽見小明      | 有／無／未知       | 有／無／未知       | 有／無／未知       |
| 小明是否看見小華      | 有／無／未觀察      | 有／無／未觀察      | 有／無／未觀察      |
| 小華是否看見小明      | 有／無／未觀察      | 有／無／未觀察      | 有／無／未觀察      |
| 小明端的 mute 指示  | 開／關／未知       | 開／關／未知       | 開／關／未知       |
| 從操作到對端察覺是否需等待 | 幾乎立即／有等待／未觀察 | 幾乎立即／有等待／未觀察 | 幾乎立即／有等待／未觀察 |
| 品質是否有明顯變化     | 無／有／未觀察      | 無／有／未觀察      | 無／有／未觀察      |
| 是否恢復到原本可互動狀態  | 尚未測試         | 尚未恢復         | 是／否／未知       |

紙上情境如下：正常時，小明與小華都聽得到對方，也都看得到對方。小明按下自己畫面上的 mute 按鈕後，小明端顯示已 mute；小華不再聽到小明，但小明仍聽得到小華，原本可見的雙方畫面也仍存在。小明按下 unmute 後，小華再次聽到小明的測試短句。請把這些現象填入表格，沒有提供的資訊一律寫「未知」，不要猜。

「未知」不是失敗答案。它是在提醒你：沒有觀察，就沒有足夠證據下結論。

## 10\. 動手做

這是可選的章內觀察，不是正式 Lab。只有符合下列條件才操作：兩部裝置都由你擁有或控制；兩個測試帳號都是自己的；通話不是課堂、家庭、工作或其他正在使用的會議；沒有其他參與者；不開啟錄影或錄音。若任一條不成立，改做上一節的紙上情境。

為避免刺耳回授，兩部裝置不要把喇叭和麥克風靠在一起；優先使用耳機，或把音量維持在舒適的低音量。

1.  在兩部自有裝置上建立一場只含兩個自有測試帳號的通話。
2.  確認兩端介面都顯示自己未 mute。
3.  小明說一句不含個資的測試短句，例如「測試一、二、三」；小華確認是否聽見。
4.  小華也說一句測試短句；小明確認是否聽見。
5.  若兩端原本就有畫面，只記錄「有」或「無」，不要截圖或保存內容。
6.  把結果填入觀察表的「正常時」欄。沒有親自觀察的項目寫「未觀察」或「未知」。

預期的正常基準是：兩端都顯示未 mute，兩端都能聽見對方；若選擇觀察畫面，則分別記錄兩個方向是否看得見。這個基準是等等判斷故障與恢復的比較點。

遇到以下任一情況就立即停止：出現非測試參與者、產品開始錄製、要求付費、帳號或裝置不是自己控制，或發生刺耳回授、身體不適、裝置明顯過熱。停止後結束通話；不要為了完成表格而降低安全條件。

## 11\. 故意把它弄壞

接下來只製造一個很小、可復原的故障：**小明按下產品原本就有的 mute 按鈕，暫停自己的麥克風聲音。**

不要關閉網路，不要修改瀏覽器或裝置的權限，不要改動系統聲音設定，不要關閉攝影機，也不要操作小華端。一次只改一件事，才知道觀察到的變化和哪個操作有關。

操作後記錄：

1.  小明端是否明確顯示自己已 mute。
2.  小華是否不再聽到小明的測試短句。
3.  小明是否仍聽得到小華。
4.  原本存在的畫面是否仍然可見；若未觀察，就填「未觀察」。
5.  從按下按鈕到小華察覺之間，是否有明顯等待。

預期證據是「小明端顯示已 mute，而且小華不再聽到小明」。這些證據只支持一個有限結論：小明的聲音輸出因使用者操作而暫停。它不能證明 WebRTC 內部哪個部分改變，也不能證明整場通話、所有方向的聲音、所有畫面或所有安全需求同時成功或失敗。

若按鈕的影響不清楚、產品出現錄製、非測試參與者加入，或發生任何前一節的停止條件，立即結束操作並改用紙上情境。

## 12\. 工程師 Debug

Debug 不是看到「沒聲音」就立刻猜內部原因，而是先縮小可以由證據支持的範圍。

第一步，看小明自己的介面。若顯示已 mute，表示有一項直接可見的使用者狀態。第二步，請小華確認她失去的是不是只有「從小明而來的聲音」。若小明仍聽得到小華，而原本的畫面也仍存在，就不能把現象說成「整場通話完全斷掉」。

第三步，恢復唯一改動：小明按下 unmute。小明先確認自己的介面回到未靜音，再說同一句測試短句；小華確認是否重新聽見。把結果記入「unmute 恢復後」欄。

如果聲音恢復，我們可以說：「移除小明端的 mute 狀態後，小華再次聽見小明，觀察結果回到正常基準。」仍然不能由此推論通話內部每個部分都已被檢查。

如果聲音沒有恢復，不要任意修改尚未學過的設定。把結果標為「未恢復／原因未知」，接著安全結束測試。誠實保留未知，比一次改動很多項目後猜測原因更有價值。

最後完成 cleanup：正常結束通話，關閉使用中的測試分頁或應用，必要時登出臨時測試帳號；確認麥克風與攝影機的使用指示已熄滅。不要留下錄製檔、截圖、通話連結或個資。恢復驗證只記兩件事：unmute 後聲音是否回來，以及通話結束後裝置是否不再被使用。

這次練習呈現了一個重要原則：症狀的範圍、證據的範圍和結論的範圍要一致。小華聽不到小明，不等於所有問題都壞了；一個方向恢復，也不等於所有問題都已驗證。

## 13\. 本章一句話

視訊通話是持續的雙向互動，必須同時面對多類問題，不能只當成寄送一份已完成的影片。

## 14\. 五題理解題

### 第 1 題

為什麼「先錄完影片再寄送」不適合描述一場自然對話？

\*\*答案解析：\*\*因為自然對話需要雙方在內容持續產生時就接收並回應；若等一方完成整段影片，另一方才能回答，等待會破壞互動。差異不只是影片長短，而是「先完成再傳送」和「邊產生邊交換」兩種模式。

### 第 2 題

不使用後章技術名稱，列出本章的六類待解問題。

\*\*答案解析：\*\*取得當下的聲音與畫面、交換建立通話所需的協調資訊、找到資料能到達的方式、保護協調資訊與通話內容、持續傳送正在產生的影音，以及在條件改變時盡量維持互動品質。六項可能交錯發生，不是固定的單一路線。

### 第 3 題

小明端和小華端都是 peer。這能不能證明資料一定直接在兩部裝置之間傳送？為什麼？

\*\*答案解析：\*\*不能。Peer 只描述參與一次即時通訊的一端角色，沒有指定資料實際採用哪種到達方式。要判斷資料怎麼走，需要後續章節的知識與證據，不能從名稱或故事畫面推論。

### 第 4 題

小明看得到小華的畫面。為什麼這還不足以宣稱「通話全部成功」？

\*\*答案解析：\*\*因為這只是一個方向的一項可見現象。它沒有證明小華也看得到小明、雙方都聽得到彼此、協調資訊都正確、內容受到適當保護，或品質接下來都能維持。結論不能超過實際觀察到的證據。

### 第 5 題

小明按下 mute 後，小明端顯示已 mute，而且小華不再聽到小明；unmute 後聲音恢復。這些證據能證明什麼？又不能證明什麼？

\*\*答案解析：\*\*它們支持「小明的聲音輸出因使用者操作而暫停，移除該操作後可見結果回到基準」。它們不能證明 WebRTC 內部是哪個部分改變，也不能證明所有聲音、畫面、協調、安全與品質都正常。這正是讓證據範圍與結論範圍一致。

## 本章參考資料

  - [WebRTC: Real-Time Communication in Browsers](https://www.w3.org/TR/2025/REC-webrtc-20250313/) — W3C Recommendation，2025-03-13；查核日期 2026-08-12；支援 WebRTC 是瀏覽器即時通訊的一組標準化能力與處理模型，以及 peer 角色的整體定位。
  - [RFC 8825: Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/rfc/rfc8825.html) — Proposed Standard（Internet Standards Track），2021-01；查核日期 2026-08-12；支援瀏覽器即時通訊的整體問題、互動需求與多項機制共同作用，並說明它是 applicability statement／規範 roadmap，本身不另行定義 protocol。

# Chapter 02：Client、Server、IP、Port、LAN 與 WAN

## 1\. 今天遇到什麼問題？

上一章留下了一個問題：兩個 peer 都準備交換資訊時，資料究竟要送到哪裡？只知道「送給小華」還不夠，因為網路不會把人的姓名直接當成目的地。

今天，小明用瀏覽器向校內服務取得一個簡單頁面。他已經找到提供服務的裝置，卻仍然打不開頁面。奇怪的是，同一台裝置上的另一項服務可以正常使用。這表示「找到裝置」和「找到裝置上的特定服務」是兩個不同問題。

要描述最小的通訊情境，我們至少要回答五件事：這次是誰要求服務、誰提供服務、資料要去的網路位置、該位置上的哪個服務入口，以及資料會在什麼範圍的網路中前進。網路處理資料時，也不會把一整部影片或整份網站視為不可分割的一塊，而是處理有邊界的資料單位。

本章會建立「角色、位址、服務入口、網路範圍、資料單位」的心智模型。不過，看到一個頁面成功或失敗，仍只能支持同樣範圍的結論。這正是上一章學過的證據紀律：一項現象不能替整個網路或整套 WebRTC 作證。

## 2\. 生活故事

小明要把一份校務文件交到行政大樓。他只在信封上寫「行政大樓」，文件送到大樓後，工作人員卻不知道該交給註冊組、出納組，還是設備組。

小華提醒他：「你需要兩項資訊。大樓地址告訴你要到哪個位置，辦公室入口則告訴你要找哪項服務。」小明補上「註冊組服務入口」，文件才有明確的概念目的地。

這次故事先幫我們建立「提出要求」與「提供結果」的直覺；正式角色只限稍後的 localhost HTTP connection。假設小華開啟小明在自己電腦上建立的測試頁面，小華的程式建立這條 connection，小明的程式接受它。換一條 connection，同一程式也可能交換角色。小明和小華不是天生固定的兩種角色，而且本章不把這項 HTTP 定義泛化到所有通訊方式。

如果文件只在一棟建築等相對有限的區域內傳遞，可以先建立局部範圍的尺度直覺。若要送往更大的地理範圍，並連接更多獨立使用者，則能建立廣域互連的尺度直覺。差異不能只用公尺數決定：來源沒有給出一條適用所有情境的距離門檻，故事中的校園線或行政線也不能代替真實網路分類。

「地址＋辦公室入口」的比喻成立在這裡：地址幫助我們區分網路位置，入口幫助我們區分同一位置上的不同服務；一次一份、有邊界的文件，也能幫助理解網路會處理有限的資料單位。

但比喻從這裡開始失真。網路位址不是人的姓名或永久門牌；在 IPv6 範圍，位址配給介面，單一介面可有多個位址，而使用自動設定的位址還有生命週期。這些限定例子都不能外推為所有位址使用相同機制。服務入口不是摸得到的洞，也不是應用程式本身。資料單位更不等於有簽收保證的信件：它可能沒到、較晚到、順序改變或重複。真實資料路徑也不必等於地圖上最短的道路。本章故事只建立直覺，不解釋資料實際如何選路。

## 3\. 如果你是工程師，你會怎麼解？

面對「裝置找到了，服務卻找不到」時，先別把整個網路判定為故障。你可以把問題拆成四組。

第一組是**互動角色**。先把問題限定在本章的 localhost HTTP 情境，再指定正在觀察哪一條 connection：哪一方建立它？哪一方接受它？如果換了另一條 connection，同一程式的角色可能交換；這不是所有通訊方式的通用定義。

第二組是**位置與入口**。用一個欄位描述網路位置，再用另一個欄位描述該位置上的服務入口。只有位置，可能到達裝置卻找錯服務；只有入口數字，也無法單獨指出全球哪個位置。

第三組是**網路範圍**。比較兩個環境時，可先區分相對有限的區域，以及通常較大地理範圍、服務更多獨立使用者的互連情境；不要自行畫出一條公尺門檻。

第四組是**資料單位與證據**。資料被分成可處理的有限單位，不代表每個單位都一定準時、依序且只出現一次。觀察某一個服務入口失敗，也不能直接推論整台裝置、整個局部網路、整個跨範圍網路或 WebRTC 都失效。

這樣拆分後，我們得到的不是所有網路問題的答案，而是一份可檢查的最小清單：角色是否判斷正確？位置是否正確？入口是否正確？服務是否正在該入口等待？觀察到的證據究竟能支持多大的結論？

## 4\. 正式技術名稱

先看互動角色，而且嚴格限定在本章的 localhost HTTP 情境。依 RFC 9110 §3.3，建立一條 HTTP connection 的參與者是**用戶端（client）**；接受該 connection 的參與者是**伺服器（server）**。角色依這一條 connection 判定，不是兩種永久固定的機器。同一程式可在不同 HTTP connection 中交換角色；本章不把這項定義泛化為所有通訊方式。

接著是位置與入口。\*\*網際網路協定位址（Internet Protocol address, IP address）\*\*的最小共同模型是：RFC 791 的 IPv4 header 與 RFC 8200 的 IPv6 header 都有來源與目的位址，讓封包帶著來源與目的資訊；這不表示兩個版本的格式或全部行為相同。另在 IPv6 範圍，RFC 4291 §2.1 說位址配給介面而非整個節點，且單一介面可有多個 IPv6 位址；RFC 4862 所述的 IPv6 自動設定位址具有生命週期。這個生命週期只是 IPv6 自動設定的例子，不能外推成所有 IP address 都以相同機制改變。IP address 因而不能當成人、帳號或裝置的永久身份。

\*\*連接埠（port）\*\*是在特定傳輸脈絡中，以數字區分同一 IP address 上不同服務端點的識別欄位。Port number 不能離開 IP address 單獨指出完整目的地；相同號碼在不同傳輸脈絡中也不能直接視為同一入口。IANA 的登錄資料依傳輸欄位分開記錄，但「有登錄」不表示服務正在執行、值得信任或一定可以取得。

再看網路範圍。依 NIST SP 800-82 Rev. 3，\*\*區域網路（Local Area Network, LAN）\*\*是在相對有限區域內的一組電腦與其他裝置，例如一棟建築內；\*\*廣域網路（Wide Area Network, WAN）\*\*通常跨較大地理範圍、服務較多獨立使用者，也可互連較小網路。來源沒有提供單一距離門檻，所以故事邊界不能當成分類公式；Internet 是熟悉的廣域互連例子，但 WAN 不等於 Internet。

最後是**封包（packet）**：網路層處理的一個有格式、有限大小的資料單位，包含處理所需的標頭資訊與所攜帶的內容。形成 packet 只代表資料成為網路可處理的單位，不承諾它一定送達、維持順序、只出現一次或準時抵達。

本章的角色定義來自 RFC 9110／STD 97 §3.3；IPv4／IPv6 共同模型來自 RFC 791／STD 5 與 RFC 8200／STD 86。RFC 1122／STD 3 只提供 Internet host 通訊分層與互連背景；它 Updates RFC 793，而 RFC 9293 已取代其中的 TCP requirements，本章不採用也不教那些 requirements。RFC 6335 是 BCP 165 的一部分；現行 BCP 165 也包含提供補充建議、但不更新 RFC 6335 的 RFC 7605。

## 5\. 專有名詞小卡

以下七張是本章唯一的新術語候選；在本章全部 Gate 通過前，不會寫入正式詞庫。

### 用戶端

英文：client  
中文：用戶端  
一句話：在本章 localhost HTTP 情境中，建立一條 connection 的參與者  
生活比喻：這次走到服務窗口提出要求的小明  
真正作用：依這一條 HTTP connection 判定角色；例如瀏覽器建立通往同一台電腦測試服務的 connection 時，瀏覽器是該 connection 的 client  
常見誤解：client 不是永久機器類型；同一程式可在不同 HTTP connection 中交換角色，本章也不把定義泛化到所有通訊方式  
適用版本／範圍：僅限本章 localhost HTTP connection 與 RFC 9110 §3.3  
首次出現章節：Chapter 02  
來源：<https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3>

### 伺服器

英文：server  
中文：伺服器  
一句話：在本章 localhost HTTP 情境中，接受一條 connection 的參與者  
生活比喻：這次等待校務文件並提供結果的服務窗口  
真正作用：依這一條 HTTP connection 判定角色；例如本機測試程式接受瀏覽器建立的 connection 時，它是該 connection 的 server  
常見誤解：server 不等於整台機器，也不一定在雲端、比較強或永久只提供服務；本章不把定義泛化到所有通訊方式  
適用版本／範圍：僅限本章 localhost HTTP connection 與 RFC 9110 §3.3；不引入系統內部服務管理  
首次出現章節：Chapter 02  
來源：<https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3>

### 網際網路協定位址

英文：Internet Protocol address（IP address）  
中文：網際網路協定位址  
一句話：IPv4 與 IPv6 封包中用來表示來源與目的網路位置的位址  
生活比喻：指出要前往哪棟大樓的地址  
真正作用：RFC 791 與 RFC 8200 共同支持 IPv4／IPv6 都有來源與目的位址；在 IPv6 範圍，位址配給介面，單一介面可有多個位址  
常見誤解：IP address 不是人、帳號、瀏覽器、房間、裝置序號或永久身份；位址生命週期的例子僅限 RFC 4862 的 IPv6 自動設定，不能外推到所有 IP 位址  
適用版本／範圍：共同模型只含 IPv4／IPv6 的來源與目的位址；介面多位址限 RFC 4291 §2.1，生命週期限 RFC 4862 的 IPv6 自動設定  
首次出現章節：Chapter 02  
來源：<https://www.rfc-editor.org/info/rfc791>、<https://www.rfc-editor.org/info/rfc8200>、<https://www.rfc-editor.org/rfc/rfc4291.html#section-2.1>、<https://www.rfc-editor.org/info/rfc4862>

### 連接埠

英文：port  
中文：連接埠  
一句話：在特定傳輸脈絡中，用來識別服務端點的數字欄位  
生活比喻：到達大樓後，還要前往正確辦公室入口  
真正作用：區分同一 IP address 上的不同服務；例如測試服務位於 port A 時，舊 port B 不會因此提供同一服務  
常見誤解：port 不是實體洞、不是應用程式本身、不是全球唯一房號，也不能離開 IP address 和傳輸脈絡單獨定位服務  
適用版本／範圍：依 RFC 6335 與 IANA registry 的服務名稱／port number 管理背景；不比較具體傳輸規則  
首次出現章節：Chapter 02  
來源：<https://www.rfc-editor.org/rfc/rfc6335.html#section-6>

### 區域網路

英文：Local Area Network（LAN）  
中文：區域網路  
一句話：位於相對有限區域內的一組電腦與其他裝置  
生活比喻：文件在一棟建築等相對有限區域內傳遞  
真正作用：描述相對有限的網路範圍，例如一棟建築內；真實分類仍須查看具體網路設計  
常見誤解：LAN 沒有本章自訂的單一距離門檻，也不表示任意兩台相近裝置一定互通；故事中的校園或行政線不是分類公式  
適用版本／範圍：採 NIST SP 800-82 Rev. 3 glossary 的相對有限區域定義  
首次出現章節：Chapter 02  
來源：<https://csrc.nist.gov/pubs/sp/800/82/r3/final>

### 廣域網路

英文：Wide Area Network（WAN）  
中文：廣域網路  
一句話：通常跨較大地理範圍並服務較多獨立使用者的網路  
生活比喻：文件跨到較大地理範圍，連接更多獨立使用者  
真正作用：描述通常較大的地理尺度與較多獨立使用者，也可把較小網路互連起來  
常見誤解：WAN 不是「超過某個距離」的同義詞，也不等於 Internet；故事邊界不能代替真實分類  
適用版本／範圍：採 NIST SP 800-82 Rev. 3 glossary；沒有單一距離門檻，不教授互連內部如何選路  
首次出現章節：Chapter 02  
來源：<https://csrc.nist.gov/pubs/sp/800/82/r3/final>

### 封包

英文：packet  
中文：封包  
一句話：網路層處理的一個有格式、有限大小資料單位  
生活比喻：一次一份、有邊界的寄件單位  
真正作用：把處理資訊與所攜內容組成網路可處理的單位，而不是把整份檔案視為不可分割的一塊；版本中立概念圖會分層呈現來源 IP、目的 IP、傳輸欄位與所攜內容  
常見誤解：packet 不是簽收保證；形成 packet 不保證送達、順序、只送一次或準時  
適用版本／範圍：本書採版本中立入門模型；RFC 8200 直接支援 IPv6 header 加所攜內容的 packet 定義  
首次出現章節：Chapter 02  
來源：<https://www.rfc-editor.org/rfc/rfc8200.html#section-3>

## 6\. 第一張圖：生活故事圖

![生活故事圖：左側是相對有限區域內的地址與服務入口，右側是通常較大地理範圍並連接更多獨立使用者的情境；小插格顯示同一程式在不同 localhost HTTP connection 中可交換 client 與 server 角色，角色標籤附著於 connection，且沒有單一距離門檻。](../book/figures/story/chapter-02-address-and-range.svg)

\*\*圖 2-1　地址、入口與網路範圍。\*\*相對有限區域與通常較大地理範圍只是尺度示例，並非距離公式；角色只對應圖中的 localhost HTTP connection。

圖的左半部是相對有限的校內範圍。小明把文件送往標有「大樓地址＋服務入口」的目的地；角色文字要寫成「這條 connection 的 client」與「這條 connection 的 server」，不能把 client 或 server 永久印在人物身上。

圖的右半部跨較大地理範圍，連接較多獨立使用者與網路。兩側範圍必須用邊界線型、文字標籤和位置共同區分，不能只靠顏色；圖例也要明說這是 NIST 定義的尺度示例，不是距離門檻。

旁邊另放一個角色交換小插格：小華的程式在另一條 localhost HTTP connection 中建立連線，小明的程式接受它。這個插格要讓讀者看見角色貼在「這條 connection」上，而不是貼在人身上，也不把定義泛化到其他通訊方式。

生活圖的比喻仍有界線：大樓和辦公室只幫助理解位置與入口；文件箭頭不代表資料真實路徑，也不保證送達。圖中不能放真實 IP address、port number，或任何後章才會解釋的機制。

## 7\. 第二張圖：專業圖

![專業圖：裝置 A 與裝置 B 之間的要求與回應箭頭標示本次 HTTP connection 角色；來源與目的 IP、來源與目的 port 分列，packet 是獨立資料單位，近端 LAN 與跨網路 WAN 範圍另以文字和線型區分。](../book/figures/technical/chapter-02-ip-port-packet.svg)

\*\*圖 2-2　IP、port 與 packet 的分層概念。\*\*角色附著於本次 localhost HTTP connection；IP 與 port 分層，packet 箭頭不代表送達保證，實際路徑也不保證最短。

圖中兩端命名為「裝置 A」與「裝置 B」，不能直接命名為永久 client／server。角色標籤附著於本次 localhost HTTP connection 的箭頭，提醒角色依該 connection 判斷。

每一端把 IP 欄位和傳輸 port 欄位分成兩列。裝置 A 列出來源 IP、來源 port；裝置 B 列出目的 IP、目的 port，並在裝置 B 中另外畫出「特定服務」。Packet 畫成獨立資料單位，只標示來源 IP、目的 IP、分開的來源／目的 port 欄位，以及「所攜內容」。Port 不能被畫進 IP address，也不能把 packet 畫成保證送達的信件。

圖的近端範圍標示「LAN：相對有限區域」；跨越「網路互連位置（本章不展開）」後標示「WAN：通常較大地理範圍／更多獨立使用者」。若出現 router 字樣，只能作這個背景標籤的一部分，不能增加新的術語卡或解釋其內部行為。

圖例必須寫明：角色附著於本次 localhost HTTP connection；LAN／WAN 不只由距離決定；packet 箭頭只表示概念前進，不保證到達；實際路徑不保證最短。圖中不得提前加入 Chapter 03 或更後面的技術名稱。

## 8\. 流程、狀態或資料怎麼走？

以下八步是概念責任，不表示每個軟體都會以讀者看得見的固定順序執行，也不解釋路徑如何選擇。

1.  \*\*指定服務。\*\*先說清楚這次想取得什麼服務。
2.  \*\*形成角色。\*\*在本章 localhost HTTP 情境，建立這條 connection 的參與者是 client，接受它的參與者是 server。
3.  \*\*選定目的 IP address。\*\*用位址指出封包要前往的網路位置；位址不是對方的永久身份。
4.  \*\*指定目的 port。\*\*在對應傳輸脈絡中，指出該位置上的服務端點。只有 port number 不構成完整目的地。
5.  \*\*資料形成 packet。\*\*資料成為網路可處理的有限單位；這一步不提供送達承諾。
6.  \*\*在網路範圍中前進。\*\*資料可能留在 LAN，也可能經過網路互連進入 WAN 範圍；實際路徑不保證是地理或圖面上的最短線。
7.  \*\*到達目的網路位置。\*\*目的 IP address 讓網路層辨認要處理的位置。
8.  \*\*交給正在等待的服務。\*\*資料要交到目的 port 所對應、而且當時正在等待的服務。

最後一步尤其重要：IP address 正確，不代表該 port 上一定有目標服務。如果位址正確、入口卻錯了，觀察到的失敗只支持「這次沒有從該入口取得目標服務」；它不能直接證明整個網路、對方裝置或 WebRTC 故障。

## 9\. 最小實作或最小可觀察練習

本章的正式 Lab 為 **N/A**。這個章內練習只在單一電腦上觀察 localhost 與兩個 port，不建立可累積 Lab artifact，也不連到 LAN、WAN 或其他裝置。

固定拓撲與權限如下：

  - 一台自己控制的電腦、一個自己的瀏覽器、一般使用者權限。
  - 測試服務只能綁定本機 `127.0.0.1`，瀏覽器只開啟 `localhost`。
  - Port A 固定為 `49152`，port B 固定為 `49153`；兩者都是非特權 port。
  - 若 A 已被占用，只能改用事先指定的替代配對 A=`49154`、B=`49155`，並在紀錄中整組替換。替代配對也被占用就停止，不繼續猜號碼或掃描。
  - 禁止 `0.0.0.0`、區域網路位址、公網主機、production、他人設備、管理員權限與任何 port 掃描。

工具是 Python 3 標準庫。本輪唯一實際執行證據來自 Ubuntu 22.04.5 LTS／Python 3.10.12。Ubuntu 24.04 官方套件資料顯示預設 `python3` 屬 Python 3.12.3 family，但本輪未在 Ubuntu 24.04 執行，不能稱為已驗證環境。你必須先記錄自己的 `/etc/os-release` 與 `python3 --version`；若標準庫命令、輸出或 cleanup 行為不同，就停止並保留紀錄，不要假裝與實測基線等價。

下面命令中的 `http.server`、`127.0.0.1`、瀏覽器 URL 前綴及工具輸出只是完成本機觀察所需的工具細節，不是本章新增術語。若終端或瀏覽器 Network 面板出現尚未教過的欄位，一律標記「工具細節，後章再解釋」，不要用它解釋本章概念。

成功 baseline 只要求四項證據：瀏覽器位址列顯示 `localhost:49152`、頁面出現自製識別文字、server 終端出現這一筆本機要求紀錄，以及瀏覽器內建 Network 面板中自己的 `localhost` request 顯示成功。本章不正式教授 Network 面板的其他欄位。

## 10\. 動手做

在自己建立的空白練習目錄中操作。以下命令只在 Ubuntu 22.04.5 LTS／Python 3.10.12 實際執行過；Ubuntu 24.04／Python 3.12.3 family 只是官方套件背景，尚未實測。其他環境若無法以相同方式確認 localhost-only 綁定，改做紙上流程，不自行改成外部綁定。

### A. 建立自有測試內容

先建立只含本章自製內容的目錄與頁面：

``` bash
cat /etc/os-release
python3 --version
mkdir -p ch02-local-test
python3 -c 'from pathlib import Path; Path("ch02-local-test/index.html").write_text("<!doctype html><meta charset=utf-8><title>Chapter 02</title><h1>CH02-LOCAL-ONLY</h1><p>這是本專案自行產生的測試頁。</p>", encoding="utf-8")'
```

保留作業系統檔案與版本輸出的紀錄。本輪實測結果是 Ubuntu 22.04.5 LTS 與：

``` text
Python 3.10.12
```

### B. 建立 port A 的正常 baseline

在終端執行：

``` bash
python3 -m http.server 49152 --bind 127.0.0.1 --directory ch02-local-test
```

命令會保持執行；不要關閉這個終端。若它顯示 port 已被占用、嘗試使用非本機範圍，或要求提升權限，按 `Ctrl+C` 停止。Port 被占用時不終止不明程式、不掃描，僅依上一節規則改用固定替代配對。

在瀏覽器開啟：

``` text
http://localhost:49152/
```

預期頁面顯示 `CH02-LOCAL-ONLY`。終端應留下對應要求紀錄；Network 面板只保留自己的這一筆 localhost request。這些證據支持的結論只有：「這台電腦上的 port A 當時有目標測試服務回應。」

記錄後回到終端按 `Ctrl+C`，正常停止 A。這個停止動作也是下一節唯一故障的起點。

## 11\. 故意把它弄壞

故障仍限制在同一台電腦。不要改網路設定，不要連其他裝置，也不要同時改測試頁內容。

1.  確認 port A 的 baseline 已成功，而且 A 已用 `Ctrl+C` 正常停止。
2.  把同一個測試服務移到 port B：

<!-- end list -->

``` bash
python3 -m http.server 49153 --bind 127.0.0.1 --directory ch02-local-test
```

3.  保留瀏覽器的舊位址 `http://localhost:49152/` 並重新整理。預期是無法取得測試頁；實際錯誤文字可能因平台不同，不能要求只出現某一句。
4.  另開分頁至 `http://localhost:49153/`。預期出現相同的 `CH02-LOCAL-ONLY`，而 server 終端留下 B 的本機要求紀錄。
5.  在 Network 面板只比較這兩筆自己的 localhost request；其他工具欄位仍標記「後章再解釋」。

這次故障的證據組合是：A 沒有取得測試頁；server 明確顯示自己在 B 提供服務；B 取得相同識別文字；server 留下 B 的要求紀錄。結論上限是：「目標測試服務從 A 移到 B 後，A 不再提供它，B 提供它。」這不能證明所有其他服務、整個網路、WebRTC 或某種未教傳輸規則的狀態。

遇到以下任一情況就停止：命令綁定非 `127.0.0.1`、port 已被占用、要求管理員權限、出現未預期的非本機要求、需要掃描、可能影響既有服務，或無法辨認正在操作的是否為本章測試程式。不得終止不明程序。

## 12\. 工程師 Debug

先從可直接觀察的四個假設分流：

1.  瀏覽器中的地址名稱是否仍是 `localhost`？
2.  Port number 是 A 還是 B？
3.  目標測試服務是否正在那個 port 等待？
4.  頁面識別文字是否確實為 `CH02-LOCAL-ONLY`？

不要因 A 失敗就改系統網路、猜測後章機制或掃描其他入口。B 成功只能證明 B 當時有這個測試服務回應；A 同時失敗且目標 server 只在 B，才支持「目標服務不在 A」這個有限結論。

### 恢復 baseline

先在執行 B 的終端按 `Ctrl+C`。接著以原設定重新啟動 A：

``` bash
python3 -m http.server 49152 --bind 127.0.0.1 --directory ch02-local-test
```

重新開啟 `http://localhost:49152/`，確認頁面識別文字與 server 要求紀錄都回到 baseline。再確認 `http://localhost:49153/` 不再取得測試頁。這一步證明唯一改動已復原。

### Cleanup

1.  在 A 的終端按 `Ctrl+C`，正常停止測試 server。
2.  關閉 A、B 測試分頁與 Network 面板的錄製。
3.  只刪除本章自行建立的明確檔案與空目錄：

<!-- end list -->

``` bash
python3 -c 'from pathlib import Path; p=Path("ch02-local-test/index.html"); p.unlink(missing_ok=True); Path("ch02-local-test").rmdir()'
```

4.  再開啟 A 與 B，兩者都不應顯示 `CH02-LOCAL-ONLY`，server 終端也不應再產生新紀錄。

恢復驗證和 cleanup 驗證目的不同：前者證明服務已回到 A 的正常基準，後者證明練習服務沒有留下。若 cleanup 後任一 port 仍有回應，不要終止未知程序；停止操作，確認那不是本章測試服務，再交由電腦擁有者人工處理。

最後，把真實世界的問題留給下一章：localhost 讓位置與入口很單純，但裝置跨越不同網路時，位址可能有不同可見範圍，網路也可能依規則允許或阻擋資料。本章只提出問題，不先命名或解釋那些機制。

## 13\. 本章一句話

在本章 localhost HTTP connection 中，client 透過 IP address 找到網路位置、再以對應傳輸脈絡的 port 找到 server 服務，而 packet 只是在 LAN 或 WAN 中被處理的資料單位，不是送達保證。

## 14\. 五題理解題

### 第 1 題

在本章 localhost HTTP 情境，同一程式能不能在不同 connection 中交換 client 與 server 角色？

\*\*答案解析：\*\*可以。依 RFC 9110 §3.3，建立該 HTTP connection 的參與者是 client，接受它的是 server；同一程式可在不同 connection 中交換角色。這個答案只適用於本章 localhost HTTP 情境，不泛化到所有通訊方式。

### 第 2 題

已知某個人的 IP address，能不能斷言那是他的永久身份？

\*\*答案解析：\*\*不能。IPv4 與 IPv6 的共同模型只說封包有來源與目的位址；在 IPv6 範圍，RFC 4291 §2.1 說位址配給介面，且單一介面可有多個位址。RFC 4862 的 IPv6 自動設定位址生命週期也顯示，至少在這個限定範圍，位址不能當成永久身份；不能外推為所有 IP 位址都用相同機制變化。

### 第 3 題

只有一個 port number，能不能找到全球唯一的服務？

\*\*答案解析：\*\*不能。Port number 必須和 IP address 及對應的傳輸脈絡一起理解；同一數字也不代表服務必然正在執行。IANA 有登錄資料，更不等於該服務可信、可達或已啟動。

### 第 4 題

相隔多遠開始算 WAN？

\*\*答案解析：\*\*沒有單一距離答案。NIST SP 800-82 Rev. 3 把 LAN 描述為相對有限區域內的一組電腦與其他裝置，把 WAN 描述為通常跨較大地理範圍並服務更多獨立使用者。來源沒有提供放諸所有情境的距離門檻，故事中的校園線也不能取代真實分類。

### 第 5 題

Packet 已經送出，是否代表它一定依序、準時、只出現一次並成功到達？

\*\*答案解析：\*\*不是。Packet 只是網路處理的有格式、有限資料單位，本身不提供送達、順序、一次性或時效保證。如何因應這些情況要到後續章節才會拆解。

## 本章參考資料

  - [RFC 791 / STD 5: Internet Protocol](https://www.rfc-editor.org/info/rfc791) — Internet Standard，1981-09；replaces RFC 760，updated by RFC 1349、2474、6864；查核日期 2026-08-12；只支援 IPv4 header 的來源／目的位址與 datagram 背景，不採已更新欄位的舊細節。
  - [RFC 1122 / STD 3: Requirements for Internet Hosts — Communication Layers](https://www.rfc-editor.org/info/rfc1122/) — Internet Standard，1989-10；Updates RFC 793，updated by RFC 1349、4379、5884、6093、6298、6633、6864、8029、9293；查核日期 2026-08-12。RFC 9293 取代 RFC 1122 的 TCP requirements；本章只採 Internet host 通訊分層／互連背景，不採也不教該 requirements。
  - [RFC 8200 / STD 86: Internet Protocol, Version 6 (IPv6) Specification](https://www.rfc-editor.org/info/rfc8200/) — Internet Standard，2017-07；obsoletes RFC 2460，updated by RFC 9673；查核日期 2026-08-12；支援 IPv6 header 的來源／目的位址與 packet 定義，並與 RFC 791 構成最小共同模型。
  - [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/info/rfc4291) — Draft Standard，2006-02；obsoletes RFC 3513，updated by RFC 5952、6052、7136、7346、7371、8064；查核日期 2026-08-12；只使用 §2.1 的 IPv6 位址配給介面及單一介面可多位址主張。
  - [RFC 4862: IPv6 Stateless Address Autoconfiguration](https://www.rfc-editor.org/info/rfc4862) — Draft Standard，2007-09；obsoletes RFC 2462，updated by RFC 7527、9762；查核日期 2026-08-12；只用於 IPv6 自動設定位址的生命週期例子，不外推到所有 IP 位址。
  - [RFC 6335: IANA Procedures for the Management of the Service Name and Transport Protocol Port Number Registry](https://www.rfc-editor.org/info/rfc6335/) — Best Current Practice，2011-08；updates RFC 2780、2782、3828、4340、4960、5595；查核日期 2026-08-12；它是 BCP 165 的一部分，支援依傳輸脈絡分開的 port namespace、範圍與 registry 管理。
  - [BCP 165](https://www.rfc-editor.org/info/bcp165/) 與 [RFC 7605: Recommendations on Using Assigned Transport Port Numbers](https://www.rfc-editor.org/info/rfc7605) — 查核日期 2026-08-12；現行 BCP 165 包含 RFC 6335 與 RFC 7605，後者補充但不更新 RFC 6335；本章不藉此比較具體傳輸規則。
  - [RFC 9110 / STD 97: HTTP Semantics](https://www.rfc-editor.org/info/rfc9110) — Internet Standard，2022-06；查核日期 2026-08-12；只使用 §3.3 的 HTTP connection client／server 角色，並限定在本章 localhost HTTP 情境。
  - [NIST SP 800-82 Rev. 3: Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — NIST Special Publication，2023-09；supersedes Rev. 2；查核日期 2026-08-12；只使用 glossary 中 LAN 的相對有限區域與 WAN 通常較大地理範圍、較多獨立使用者定義；不自訂距離門檻。
  - [IANA Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) — Live registry，Last Updated 2026-08-11；查核日期 2026-08-12；支援 port number 依傳輸欄位分列及 49152–65535 為 Dynamic／Private Ports；登錄不代表服務正在執行、可信或可達。
  - [Ubuntu Packages: python3 (noble)](https://packages.ubuntu.com/noble/python3) — Ubuntu 24.04 LTS 官方套件資料；查核日期 2026-08-12；只支持其預設 Python 3 為 3.12.3 family 的背景。本輪未在 Ubuntu 24.04 執行；唯一實跑證據是 Ubuntu 22.04.5 LTS／Python 3.10.12。

# Chapter 03：NAT、Firewall、UDP 與 TCP

## 1\. 今天遇到什麼問題？

上一章，小明在同一台電腦上用 `localhost`、IP address 與 port 找到測試服務。可是他把同一套「地址＋入口」想法搬到不同網路後，原本的假設不一定還成立：內側使用的 IPv4 address，未必就是外側觀察到的 address；即使有一筆內外對應，也不代表資料一定獲准通過；即使 address 與 port 都正確，目的端也可能沒有用相符的傳輸方式等待資料。

因此，「同一個 LAN 可通，換到另一個網路不通」不是一個足以直接歸因的證據。可能要問的至少有四類：address 的可見範圍是否改變？是否存在仍有效的轉換對應？獨立的流量政策是否允許？目的端的 transport 與 listener 是否相符？這裡的 **listener** 只是「測試程式正在指定 transport 與 port 等待資料」的章內工具說法，不是新的核心術語。

本章還會比較兩種 transport service。比較重點不是頒發「誰一定比較快」的獎牌，而是它們向應用提供什麼語意：一種保留一份份資料的邊界，卻不承諾送達或順序；另一種建立連線狀態，把內容當連續 byte stream，提供可靠、按序的交付語意。實際等待時間與表現仍取決於應用、路徑、負載與實作，不能用名稱預先排名。

## 2\. 生活故事

小明從校內分機寄出資料，要送到小華所在的外部網路。資料先到「總機」。總機看到小明的內側聯絡表示，替這次傳送留下暫時的對應，讓外側看到另一個聯絡表示。若總機同時改了 address 與 port，稍後會有一個更精確的名稱；不能把所有總機工作都說成一定改 port。

資料接著遇到「警衛」。警衛不負責改寫聯絡表示，而是依 policy 判斷這次資料是否允許通過。總機有對應，警衛仍可能不放行；警衛放行，也不代表小華那一端剛好有人在正確 transport 與 port 等待。

小華又拿出兩種寄送服務。第一種像一張張明信片：每張的邊界保留，但服務本身不保證每張都抵達、不重複或照寄出順序抵達。第二種像先登記再傳送的連續紙帶：服務把內容視為連續字流，提供可靠、按序交付；途中資料仍可能遺失，服務可藉偵測與重送來維持這項語意，因而也可能需要等待。紙帶上哪裡算一張表單，仍要由使用它的應用自己約定。

這組比喻成立的範圍是：總機只代表內外聯絡表示與暫時對照，警衛只代表另依規則判斷；明信片代表保留每份寄送單位的邊界，連續紙帶代表先建立傳送狀態後，把內容按原順序當作連續字流交付。

比喻從這裡開始失真。總機的轉換工作與警衛的規則工作可能在同一台設備、不同設備，或只存在其中之一；畫成兩站只是為了分清責任，不是物理拓撲定律。真實對照可能依多項條件建立並有期限，本章不分類各種實作。第一種運送服務的應用可以自己加入確認、重送或排序；第二種服務的可靠按序交付也不等於永不失敗、立即抵達或對方應用已完成處理。「外線聯絡表示」更不等於具全域唯一性、全球可達或永久身分。

## 3\. 如果你是工程師，你會怎麼解？

遇到跨網路失敗時，先把猜測寫成可查核的四欄，而不是先把原因鎖定在某一個尚未查證的中間工作。

| 假設       | 要問的問題                                   | 最小 evidence               | 尚不能推出                |
| -------- | --------------------------------------- | ------------------------- | -------------------- |
| 內外表示     | 內側使用值與外側觀察值是否不同？                        | 兩側各自在同一次受控觀察記錄的 address   | 外側值具全域唯一性、一定可達、可信或永久 |
| 暫時對照     | 這次內側與外側表示之間是否有一筆仍有效的對照？                 | 同一運送方式、時間窗與受控資料的對照紀錄      | 規則一定放行，或目的端有人等待      |
| 規則判斷     | 對應方向與條件的資料是否允許通過？                       | 獨立的規則判斷紀錄                 | 位址轉換一定存在，或服務一定成功     |
| 運送方式／等待者 | 目的 address、port 與兩種運送方式是否相符，測試程式是否正在等待？ | 已知等待程式的紀錄、送出端結果、自製記號與結束狀態 | 整個網路或整套即時通訊故障        |

先用一列可讀的觀察記號，把這次來源與目的 address、port、運送方式寫在一起。例如「來源 `10.0.0.8:49152`，目的 `外側目的值:50000`，第一種運送方式」。這不是人的身分，也不是永久連線名稱；本章不延伸這種記錄的系統內部結構。

工程師的工作不是讓每個症狀只對應一個原因，而是找能排除假設的 evidence。只停止第二種方式的已知等待者、第一種仍成功，只支持第二種等待者不在原本可工作的狀態；只停止第一種方式的等待者後沒有接收紀錄，也只支持觀察窗內沒有取得該次資料的接收證據。正式名稱與更精確的服務語意，下一段才逐一建立。

## 4\. 正式技術名稱

本章先限定在 IPv4。第一個正式名稱是**私有 IP 位址（private IP address）**。RFC 1918／BCP 5 指定三段供 private internets 使用的 IPv4 address space：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`。它們可在彼此未協調的組織中重複使用；「私有」不等於加密、安全、匿名，也不表示一定存在位址轉換。

第二個名稱是**公用 IP 位址（public IP address）**。本章依 RFC 2663 §2.7，把它限定為公用／全域 address realm 中的 IP address；這種 realm 使用由 IANA 或相當的 Internet address registry 分配、具全域唯一性的 network address。這和「某個觀察點在轉換設備外側看見什麼」是不同維度。本章把後者稱作**外側觀察位址（outside observed address）**，它是觀察位置相關的輔助說法，不是第九張候選小卡：外側觀察位址可能仍是 RFC 1918 private-use 或其他非全域唯一位址，只有另有證據確定它位於 public/global realm 時，才可另標為 public IP address。

即使位址位於 public/global realm、具全域唯一性，也不保證當下有 route、policy 放行、目的 listener 存在或實際可達。IANA 的 IPv4 Special-Purpose Address Space registry 也顯示，RFC 1918 範圍之外仍有 loopback、link-local、documentation、shared 等其他特殊用途範圍，而且 registry 明示列入的 prefix 不保證在任一局部或全球情境可轉送。因此「不是 RFC 1918 private address」不能直接推成「public IP address」或「一定全球可達」。

第三個名稱是**網路位址轉換（Network Address Translation, NAT）**。在 RFC 2663 的 IPv4 入門模型中，它讓一個 address realm 的位址表示和另一個 realm 的位址表示互相對應。這裡的 realm 只需理解成「採用一組位址表示的範圍」。只翻譯 address 的情況仍屬 NAT。第四個名稱是**網路位址與連接埠轉換（Network Address Port Translation, NAPT）**：它是同時翻譯 IP address 與 transport port 的較精確子類。

第五個名稱是**對應（mapping）**：NAT／NAPT 為內外表示維持的狀態關聯。為避免把來源範圍用錯，本章的具體 mapping 範例只採 RFC 4787 所涵蓋的單播 transport、且內外都只談 IPv4 的 Traditional NAT 情境；該 transport 會在本段第七個名稱正式說明。本章也連同 RFC 6888、RFC 7857 對 RFC 4787 的更新邊界閱讀，不靠這些文件教授另一種運送方式在 NAT 中的行為，也不把任何一種 mapping、filtering、期限或 port 行為宣稱為所有 NAT 的唯一實作。

第六個名稱是**防火牆（firewall）**，它依 policy 允許或阻擋特定 traffic flow。NIST SP 800-41 Rev. 1 支持這個有限工作模型；NAT 文件則幫助我們分清 mapping 與 filtering 並非同一判斷。Firewall 可以和 NAT 共置、分開，或在沒有 NAT 的情境存在。Mapping evidence 與 policy evidence 必須分開取得。

第七個名稱是**使用者資料包協定（User Datagram Protocol, UDP）**。依 RFC 8085，它提供 minimal、unreliable datagram service：保留一份份 datagram 的 message 邊界，但不內建 delivery、duplicate protection、ordering 或 congestion control 保證。應用若使用 UDP，仍要為所需的可靠性與壅塞責任設計。UDP 沒有下一個名稱所具備的 transport connection establishment，不等於「沒有任何 state」，也不表示一定低延遲或一定較快。

第八個名稱是**傳輸控制協定（Transmission Control Protocol, TCP）**。依 RFC 9293／STD 7，它提供 connection-oriented、reliable、in-order byte-stream service。「Reliable、in-order」表示 TCP 以錯誤／遺失偵測、sequence 與 retransmission 等機制，向接收端應用提供可靠、按序的字流；若無法維持，connection 仍可能失敗。這不是封包永不遺失、系統永不失敗或資料立即抵達；「byte stream」則表示不保留應用原本每次送出資料的 message 邊界。TCP 也不因連線成功就提供應用身分、授權或機密性證明。

## 5\. 專有名詞小卡

以下恰八張是本章唯一的新術語候選；在本章全部 Gate 通過前，不會寫入正式詞庫。

### 候選小卡 1／8：Private IP address

英文：private IP address  
中文：私有 IP 位址  
一句話：RFC 1918 指定給 private internets 使用的三段 IPv4 address space  
生活比喻：組織內可自行協調、別的組織也可能重複使用的內線表示  
真正作用：在 IPv4 中提供 `10/8`、`172.16/12`、`192.168/16` 三段 private-use 範圍  
常見誤解：Private 不等於安全、加密、匿名、固定不可出網、LAN 同義詞，也不表示一定有 NAT  
適用版本／範圍：只限 RFC 1918 的 IPv4 private address space；不把同名分類直接套到 IPv6  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/info/rfc1918>

### 候選小卡 2／8：Public IP address

英文：public IP address  
中文：公用 IP 位址  
一句話：公用／全域 address realm 中，由 IANA 或相當 registry 分配而具全域唯一性的 IP address  
生活比喻：在共同登記制度下不和其他人重複的聯絡表示，但不保證道路暢通或有人接聽  
真正作用：描述 RFC 2663 §2.7 的 public/global realm 位址；和某個觀察點看到的外側位址是不同維度  
常見誤解：它不是「任意 NAT 外側觀察值」，也不是 RFC 1918 補集；具全域唯一性仍不保證 route、policy 放行、listener 存在或實際可達  
適用版本／範圍：RFC 2663 的 IPv4 public/global address realm 入門用法；是否為外側觀察值須另依觀察位置記錄  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/rfc/rfc2663.html#section-2.7>、<https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml>

### 候選小卡 3／8：NAT

英文：Network Address Translation（NAT）  
中文：網路位址轉換  
一句話：在不同 address realm 之間轉換或對應 IPv4 address 表示  
生活比喻：總機把內側聯絡表示對應成外側聯絡表示  
真正作用：本章只教 Traditional NAT 的 IPv4 入門模型；address-only translation 仍是 NAT  
常見誤解：NAT 不是 firewall、加密、身分驗證、路由器同義詞，也不保證端到端可達  
適用版本／範圍：RFC 2663 的 IPv4 術語與分類背景；Informational，不當作所有現代實作的強制行為  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/info/rfc2663>

### 候選小卡 4／8：NAPT

英文：Network Address Port Translation（NAPT）  
中文：網路位址與連接埠轉換  
一句話：Traditional NAT 中同時轉換 IPv4 address 與 TCP／UDP port 的子類  
生活比喻：總機不只換外線表示，也以不同入口數字區分多筆內側傳送  
真正作用：讓多個內側 session 可共用一個或一組外側 address 表示  
常見誤解：不能把所有 NAT 都說成一定改 port，也不能把 NAPT mapping 說成永久規則  
適用版本／範圍：RFC 2663 的 IPv4 Traditional NAT taxonomy；具體 mapping 範例限本章說明的單播 UDP、內外都只談 IPv4 的 Traditional NAT 情境  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/info/rfc2663>

### 候選小卡 5／8：Mapping

英文：mapping  
中文：對應  
一句話：NAT／NAPT 為這次內外位址表示維持的狀態關聯  
生活比喻：總機留下的一筆暫時內線／外線對照  
真正作用：讓受控 tuple 的內側表示與外側表示可以被關聯；實際 key、方向、refresh 與 lifetime 依規範範圍及實作而異  
常見誤解：Mapping 不是 DNS、route、firewall allow rule 或永久身分；存在 mapping 不代表回程 traffic 必然放行  
適用版本／範圍：具體行為範例只限 RFC 4787 及其 RFC 6888／7857 更新下的單播 UDP、內外都只談 IPv4 的 Traditional NAT 入門範圍  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/info/rfc4787>、<https://www.rfc-editor.org/info/rfc6888>、<https://www.rfc-editor.org/info/rfc7857>

### 候選小卡 6／8：Firewall

英文：firewall  
中文：防火牆  
一句話：依 policy 對特定 traffic flow 允許或阻擋的控制  
生活比喻：警衛依規則決定這次資料能否通過  
真正作用：在本章有限模型中，對流量作獨立於 address translation mapping 的 policy 判斷  
常見誤解：Firewall 不負責定義 private／public address；NAT mapping 存在也不代表 firewall 一定放行  
適用版本／範圍：NIST SP 800-41 Rev. 1 的一般入門模型；不宣稱所有產品位置、條件或部署相同  
首次出現章節：Chapter 03  
來源：<https://csrc.nist.gov/pubs/sp/800/41/r1/final>

### 候選小卡 7／8：UDP

英文：User Datagram Protocol（UDP）  
中文：使用者資料包協定  
一句話：提供不可靠 datagram service，保留每份 message 的邊界，但不保證送達、去重或順序  
生活比喻：一張張明信片各自有邊界，寄出卻不是簽收保證  
真正作用：以 datagram 為單位提供 minimal transport service；應用仍要承擔所需可靠性與壅塞責任  
常見誤解：UDP 不是「沒有任何 state」、一定即時、永不重送或一定比 TCP 快；本機 send success 也不等於 peer 收到  
適用版本／範圍：RFC 8085／BCP 145；本章不採 RFC 8899 更新所涉及的 datagram PLPMTUD 細節  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/info/rfc8085>

### 候選小卡 8／8：TCP

英文：Transmission Control Protocol（TCP）  
中文：傳輸控制協定  
一句話：提供建立連線狀態後的 reliable、in-order byte-stream service  
生活比喻：登記後傳送連續紙帶，接收者依序取得字流，但表單邊界需另約定  
真正作用：用偵測、sequence 與 retransmission 等機制提供可靠按序的 byte stream；不保留 application message 邊界  
常見誤解：TCP 不表示封包永不遺失、立即抵達、對方應用已處理、具身分安全，也不表示在所有情境一定比 UDP 慢  
適用版本／範圍：RFC 9293／STD 7 的 TCP service model 入門範圍  
首次出現章節：Chapter 03  
來源：<https://www.rfc-editor.org/info/rfc9293>

## 6\. 第一張圖：生活故事圖

![生活故事圖：小明的內側聯絡表示先到總機，總機建立暫時對應，再到依 policy 判斷的警衛，最後指向小華所在的外側網路；下方分列保留一張張邊界但可能遺失或重排的 UDP 明信片，與建立狀態後可靠按序交付、但不保留表單邊界的 TCP 連續紙帶；文字明示 mapping 不等於放行、放行不等於 listener 存在，外側觀察位址不等於 public IP address 或永久身分。](../book/figures/story/chapter-03-switchboard-guard.svg)

\*\*圖 3-1　總機與警衛是兩個工作。\*\*總機只代表 NAT／NAPT 的內外表示與暫時 mapping，警衛另依 firewall policy 決定是否放行；外側觀察位址不因位於圖的外側就成為 public IP address，UDP／TCP 運送帶也只比較 service semantics，不比較速度。

上列 alt text 與 caption 在圖 Gate 前視為凍結文字。未來 SVG 必須固定呈現小明、內側聯絡表示、總機、暫時對應表、警衛、外側網路與小華；總機使用「轉換／對應」，警衛使用「允許／阻擋」，不能合成「NAT 防火牆」。

兩條運送帶不能只靠顏色區分：UDP 使用一張張有外框的明信片，並以缺口與交換序號表示可能遺失／重排；TCP 使用相接紙帶、建立狀態標記與按序出口，並明寫不保留應用表單邊界。圖上不放速度獎牌，也不把外線號碼畫成 public/global realm、全球可達或永久身分；若要標 public，必須另有全域唯一性的證據。

## 7\. 第二張圖：專業圖

![專業圖：由左至右依序是 RFC 1918 private IPv4 host、獨立的 NAT 或 NAPT mapping table、獨立的 firewall policy boundary、outside network；表中以一筆 UDP 教學 tuple 分別示意 address-only NAT 與 address-plus-port NAPT，外側欄以 E 標示觀察位置相關的 outside observed address，並註明只有另有證據確定屬 public/global realm 才可另標 public IP address；下半部以分離時間線呈現 UDP datagram 邊界及可能遺失重排，與 TCP connection establishment 後的 reliable in-order byte stream，且不畫速度排名。](../book/figures/technical/chapter-03-mapping-policy-transport.svg)

\*\*圖 3-2　Address 表示、mapping、policy 與 transport 語意分層。\*\*Mapping table 只是一筆受控單播 UDP、內外都只談 IPv4 的 Traditional NAT 教學表示，不是產品表格格式；外側觀察位址 E 與 public/global realm 分開，firewall evidence 另列，TCP 時間線只教 transport service，不宣稱 TCP-through-NAT 行為。

上列 alt text 與 caption 在圖 Gate 前視為凍結文字。未來 SVG 的上半部必須把 private IPv4 host、mapping table、policy boundary 與 outside network 依序畫出；即使 NAT 與 firewall 放在同一 device 外框，也要有兩個獨立內框、不同線型與文字動詞。

Mapping table 可用符號值示意：內側 UDP tuple 的來源 `10.0.0.8:49152` 經 address-only NAT 後只改成「外側觀察位址 E:`49152`」；NAPT 例則改成「外側觀察位址 E:`62000`」。`E` 必須直接標「outside observed address／外側觀察位址：依觀察位置而定，不等於 public IP address」；只有另有 registry allocation／global uniqueness evidence 時，才可在 E 旁另標 public/global realm。目的欄保持不變，並註明 table layout 不等於任何產品實作。

圖的下半部以形狀、文字、編號與線型共同區分 UDP／TCP，不能只靠顏色。圖中不得加入任何 Chapter 04 以後才正式教學的名稱、元件或欄位。

## 8\. 流程、狀態或資料怎麼走？

以下流程是分層檢查順序，不表示每台設備都以可見的固定步驟執行，也不把圖上的順序當成物理拓撲定律。

1.  \*\*寫下內側 tuple。\*\*記錄這次來源與目的 address、port、transport；不要只記 port。
2.  \*\*確認 address 邊界。\*\*判斷來源是否落在 RFC 1918 的三段 private IPv4 space；把特定觀察點在轉換外側看見的值記作 outside observed address，不因它在外側或不屬 RFC 1918 就標成 public IP address。若另有 registry allocation／global uniqueness evidence，才可另判斷它是否屬 public/global realm；這仍不保證可達。
3.  \*\*查受控 mapping evidence。\*\*在單播 UDP、內外都只談 IPv4 的 Traditional NAT 範例中，記錄內側 tuple 與外側 tuple 的一筆對應及觀察時間。只改 address 是 NAT；同時改 address 與 port 才是本章所稱 NAPT。
4.  \*\*另查 policy evidence。\*\*確認對應方向與條件是否被 firewall policy 允許。Mapping record 不能代替這一步。
5.  \*\*形成外側 tuple。\*\*將 outside observed address／port／UDP 與目的表示列清楚；外側觀察位址仍不是 public IP address、永久身分或可達保證。若另證明它來自 public/global realm，全球唯一性仍不能代替 route、policy 與 listener evidence。
6.  \*\*確認目的 transport。\*\*同一 numeric port 的 TCP 與 UDP 是不同 transport 脈絡，不能因號碼相同就假定同一 listener 會接收。
7.  \*\*按 service semantics 讀證據。\*\*UDP client 的 send operation 成功，最多只表示本機程式把 datagram 交給本機 transport 處理；必須另有接收 log 或 application echo 才能說本次收到。TCP 則先建立 connection state，再傳遞 byte stream；一次 send 不保證對端只用一次 recv 取得同樣邊界。
8.  \*\*限制結論。\*\*成功或失敗都綁定該 tuple、transport、listener 與時間窗，不能擴張成 Internet、NAT、firewall 或 WebRTC 的整體結論。

## 9\. 最小實作或最小可觀察練習

本章正式 Lab 為 **N/A**。全書累積式 Lab 從 Chapter 04 開始；以下只是正文內的安全觀察，不建立 `book/labs/chapter-03/` artifact，也不模擬 NAT 或 firewall。

本輪採一次性的 rootless Linux user＋network namespace，而不是較早 scope 中的 container engine／base image 方案，因此沒有 Docker／OCI image digest 可鎖。`unshare --user --map-root-user --net` 會建立只供這個子 shell 使用的 user 與 network namespace；namespace 內顯示的 root 是映射後的 namespace 身分，不是 host root。只啟用新 namespace 自己的 loopback，不建立 veth、route、NAT 或 firewall rule，也不連 Internet、LAN、router、production 或他人設備。

本輪實測鎖定如下：

  - Host OS：Ubuntu 22.04.5 LTS，CPU architecture `x86_64`。
  - Python：CPython 3.10.12，只使用標準庫。
  - Namespace 工具：util-linux `unshare` 2.37.2；iproute2 `ip` 5.15.0。
  - 測試程式：本專案自寫單檔 `ch03_transport_probe.py`；UTF-8、LF、檔尾保留一個 newline；SHA-256 `e9b0e0723bc8bfbeac48bb20ce3b0699a6feceb08454d9a20a6f00bfdc6c1c7e`。
  - 唯一目的：namespace 內的 `127.0.0.1`；TCP 與 UDP 都使用同一個非特權 numeric port `49152`，以顯示兩種 transport 的 port number space 可各自有 listener。
  - 資源上限：兩個 listener、八次 client 呼叫（兩次初始 baseline、兩次另一 transport 連續性確認、兩次預期失敗、兩次恢復）；每次 client timeout 1.5 秒；總觀察 timebox 五分鐘；payload 只用本章自製 marker，不放秘密或真實資料。

成功 evidence 必須同時包含 client 的 `ECHO_OK`、對應 listener log 的相同 transport／marker，以及 client exit status `0`。UDP 的 `SEND_OK` 單獨不算接收成功。故障時只停止自己剛啟動且已記錄 PID 的一個 listener；另一 transport 必須仍成功，之後再重啟剛才停止的 listener並恢復 baseline。

若缺少 `unshare`／`ip`、user namespace 被系統政策停用、不能在新 network namespace 內只啟用 `lo`、版本／source hash 不符、namespace 出現非 loopback address 或 route、需要 `sudo`／host capability、出現非自製 marker，或無法精確辨認 PID，立即停止並改讀第 12 段的紙上 trace。不得修改 host network、firewall、router、route、DNS 或主介面求成功。

## 10\. 動手做

先在一般使用者 shell 記錄環境。若不是上述實測組合，可以閱讀與紙上推演，但不要把結果稱為本輪已驗證基線。

``` bash
uname -m
sed -n '1,12p' /etc/os-release
python3 --version
unshare --version
ip -Version
```

建立一個精確命名、用完可整組檢查的暫存目錄；若 `mktemp` 失敗就停止：

``` bash
CH03_WORKDIR=$(mktemp -d -p /tmp ch03-netns.XXXXXX)
printf 'workdir=%s\n' "$CH03_WORKDIR"
cd "$CH03_WORKDIR"
```

將下面程式區塊**逐字**存成 `ch03_transport_probe.py`，使用 UTF-8、LF 並保留最後一個 newline。它是同一個自寫 Python 單檔，依參數提供彼此獨立的 TCP／UDP echo listener 與 TCP／UDP client；不使用第三方套件。

``` python
#!/usr/bin/env python3
import argparse
import socket
import sys


def marker_text(data):
    return data.decode("utf-8", errors="backslashreplace")


def listen_tcp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host, port))
        listener.listen(4)
        print(f"READY transport=tcp host={host} port={port}", flush=True)
        while True:
            connection, address = listener.accept()
            with connection:
                chunks = []
                while True:
                    chunk = connection.recv(4096)
                    if not chunk:
                        break
                    chunks.append(chunk)
                payload = b"".join(chunks)
                print(
                    f"RECV transport=tcp bytes={len(payload)} "
                    f"marker={marker_text(payload)}",
                    flush=True,
                )
                connection.sendall(payload)


def listen_udp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener:
        listener.bind((host, port))
        print(f"READY transport=udp host={host} port={port}", flush=True)
        while True:
            payload, address = listener.recvfrom(4096)
            print(
                f"RECV transport=udp bytes={len(payload)} "
                f"marker={marker_text(payload)}",
                flush=True,
            )
            listener.sendto(payload, address)


def client_tcp(host, port, marker, timeout):
    payload = marker.encode("utf-8")
    try:
        with socket.create_connection((host, port), timeout=timeout) as connection:
            connection.sendall(payload)
            connection.shutdown(socket.SHUT_WR)
            chunks = []
            while sum(map(len, chunks)) < len(payload):
                chunk = connection.recv(4096)
                if not chunk:
                    break
                chunks.append(chunk)
    except OSError as error:
        print(f"NO_ECHO transport=tcp evidence={type(error).__name__}", file=sys.stderr)
        return 2
    echoed = b"".join(chunks)
    if echoed != payload:
        print("NO_ECHO transport=tcp evidence=payload_mismatch", file=sys.stderr)
        return 2
    print(f"ECHO_OK transport=tcp marker={marker}")
    return 0


def client_udp(host, port, marker, timeout):
    payload = marker.encode("utf-8")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(timeout)
        sent = client.sendto(payload, (host, port))
        print(f"SEND_OK transport=udp bytes={sent} marker={marker}")
        try:
            echoed, _ = client.recvfrom(4096)
        except (socket.timeout, OSError) as error:
            print(
                f"NO_ECHO transport=udp evidence={type(error).__name__}",
                file=sys.stderr,
            )
            return 2
    if echoed != payload:
        print("NO_ECHO transport=udp evidence=payload_mismatch", file=sys.stderr)
        return 2
    print(f"ECHO_OK transport=udp marker={marker}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("role", choices=("listen", "client"))
    parser.add_argument("transport", choices=("tcp", "udp"))
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=49152)
    parser.add_argument("--marker")
    parser.add_argument("--timeout", type=float, default=1.5)
    args = parser.parse_args()

    if args.role == "listen":
        if args.transport == "tcp":
            listen_tcp(args.host, args.port)
        else:
            listen_udp(args.host, args.port)
        return 0
    if not args.marker:
        parser.error("client role requires --marker")
    if args.transport == "tcp":
        return client_tcp(args.host, args.port, args.marker, args.timeout)
    return client_udp(args.host, args.port, args.marker, args.timeout)


if __name__ == "__main__":
    raise SystemExit(main())
```

先驗證 source hash。結果必須完全相同；不同就停止，不執行未知內容。

``` bash
sha256sum ch03_transport_probe.py
```

預期：

``` text
e9b0e0723bc8bfbeac48bb20ce3b0699a6feceb08454d9a20a6f00bfdc6c1c7e  ch03_transport_probe.py
```

接著從存放程式的目錄進入一次性 namespace：

``` bash
unshare --user --map-root-user --net bash
```

以下命令全部在這個新 shell 內執行。先只啟用它自己的 loopback，確認沒有其他 address／route；若看見非 loopback 項目就 `exit` 停止。

``` bash
ip link set lo up
ip -brief address
ip route show
```

啟動 TCP 與 UDP listener。兩者同時綁定 `127.0.0.1:49152` 是刻意的：numeric port 相同，但 transport 不同。PID 只取自剛才兩個背景命令。

``` bash
python3 ./ch03_transport_probe.py listen tcp --host 127.0.0.1 --port 49152 >ch03-tcp.log 2>&1 &
CH03_TCP_PID=$!
python3 ./ch03_transport_probe.py listen udp --host 127.0.0.1 --port 49152 >ch03-udp.log 2>&1 &
CH03_UDP_PID=$!
trap 'kill "$CH03_TCP_PID" "$CH03_UDP_PID" 2>/dev/null || true' EXIT
sleep 0.2
kill -0 "$CH03_TCP_PID" "$CH03_UDP_PID"
```

建立 baseline：

``` bash
python3 ./ch03_transport_probe.py client tcp --host 127.0.0.1 --port 49152 --marker CH03-TCP-BASE
CH03_TCP_BASE_EXIT=$?
python3 ./ch03_transport_probe.py client udp --host 127.0.0.1 --port 49152 --marker CH03-UDP-BASE
CH03_UDP_BASE_EXIT=$?
sed -n '1,20p' ch03-tcp.log
sed -n '1,20p' ch03-udp.log
printf 'tcp_exit=%s udp_exit=%s\n' "$CH03_TCP_BASE_EXIT" "$CH03_UDP_BASE_EXIT"
```

TCP 與 UDP 都應有相同 transport／marker 的 listener `RECV`、client `ECHO_OK` 與 exit `0`。UDP 還會先印 `SEND_OK`；它必須和後面的 `ECHO_OK` 分開理解。

## 11\. 故意把它弄壞

一次只停止一個已知 listener，不改 namespace、address、route、policy 或 source。實際錯誤類別可能因 OS 而異，所以只判斷「是否取得 application echo」與 exit status，不把某句錯誤文字當跨平台保證。

先停止自己記錄的 TCP listener，確認 UDP 仍成功，再觀察 TCP client 未取得 baseline echo：

``` bash
kill "$CH03_TCP_PID"
wait "$CH03_TCP_PID" 2>/dev/null || true
python3 ./ch03_transport_probe.py client udp --host 127.0.0.1 --port 49152 --marker CH03-UDP-WHILE-TCP-DOWN
CH03_UDP_WHILE_TCP_DOWN_EXIT=$?
python3 ./ch03_transport_probe.py client tcp --host 127.0.0.1 --port 49152 --marker CH03-TCP-DOWN
CH03_TCP_DOWN_EXIT=$?
printf 'udp_still_up=%s tcp_down=%s\n' "$CH03_UDP_WHILE_TCP_DOWN_EXIT" "$CH03_TCP_DOWN_EXIT"
```

預期 UDP 為 `0`，TCP 為 `2`。這只證明這次已知 TCP listener 未提供 baseline service，而相同 numeric port 的 UDP listener 仍獨立工作；它不證明 NAT、firewall 或網路故障。接著只恢復 TCP：

``` bash
python3 ./ch03_transport_probe.py listen tcp --host 127.0.0.1 --port 49152 >>ch03-tcp.log 2>&1 &
CH03_TCP_PID=$!
sleep 0.2
python3 ./ch03_transport_probe.py client tcp --host 127.0.0.1 --port 49152 --marker CH03-TCP-RESTORED
```

再停止自己記錄的 UDP listener，確認 TCP 仍成功，再觀察 UDP：

``` bash
kill "$CH03_UDP_PID"
wait "$CH03_UDP_PID" 2>/dev/null || true
python3 ./ch03_transport_probe.py client tcp --host 127.0.0.1 --port 49152 --marker CH03-TCP-WHILE-UDP-DOWN
CH03_TCP_WHILE_UDP_DOWN_EXIT=$?
python3 ./ch03_transport_probe.py client udp --host 127.0.0.1 --port 49152 --marker CH03-UDP-DOWN
CH03_UDP_DOWN_EXIT=$?
printf 'tcp_still_up=%s udp_down=%s\n' "$CH03_TCP_WHILE_UDP_DOWN_EXIT" "$CH03_UDP_DOWN_EXIT"
```

預期 TCP 為 `0`，UDP 為 `2`。特別看 UDP client：它可能先印 `SEND_OK transport=udp`，之後才印 `NO_ECHO`。這正好說明本機 `sendto()` 成功不等於 listener 收到，更不等於 peer 應用完成處理；本輪 Ubuntu 實測得到 `TimeoutError`，其他系統也可能出現不同 OS error，不能要求固定字串。

只恢復 UDP，重跑最後 baseline：

``` bash
python3 ./ch03_transport_probe.py listen udp --host 127.0.0.1 --port 49152 >>ch03-udp.log 2>&1 &
CH03_UDP_PID=$!
sleep 0.2
python3 ./ch03_transport_probe.py client udp --host 127.0.0.1 --port 49152 --marker CH03-UDP-RESTORED
```

這些故障都只是 listener state 的變化。禁止把停止 listener 稱作 NAT mapping 失效、firewall 阻擋、Internet loss 或效能測試；也禁止為了得到特定錯誤而修改 host 或 namespace firewall。

## 12\. 工程師 Debug

先對照 evidence 範圍：

| 現象                                              | 本章可支持                                                  | 本章不可支持                                                   |
| ----------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| TCP `ECHO_OK`，同 marker 出現在 TCP log              | 該 namespace、tuple、transport、時間窗內的 TCP echo baseline 成功 | TCP 封包永不遺失、應用已永久處理、Internet-wide reliability             |
| UDP `SEND_OK` 後 `ECHO_OK`，同 marker 出現在 UDP log  | 該次 datagram 在觀察窗內被 listener 收到並由測試程式 echo              | UDP 可靠、一定較快或 peer 必然收到下一筆                                |
| UDP `SEND_OK` 後 `NO_ECHO`，receiver log 無 marker | 觀察窗內沒有取得這次 datagram 的 application 接收／echo evidence     | 一定是 NAT、firewall、route、Internet 或 UDP connection failure |
| 只停 TCP，UDP 仍成功                                  | 這次 OS 實測中，同 numeric port 的 TCP／UDP listener 可獨立存在      | UDP 優於 TCP、整個 network 正常                                 |

若 baseline 不符，依序檢查 source hash、是否仍在一次性 namespace、`lo` 是否為 UP、目的是否仍是 `127.0.0.1`、numeric port 是否仍為 `49152`、transport／marker 是否相符，以及剛才記錄的 PID 是否仍存在。不要掃描其他 port，不要終止未知 process，更不要改 host network／firewall／router。

### 恢復與 cleanup

在 namespace 內，確認兩種 transport 已分別恢復過 baseline，然後只停止兩個已記錄 listener：

``` bash
kill "$CH03_TCP_PID" "$CH03_UDP_PID"
wait "$CH03_TCP_PID" 2>/dev/null || true
wait "$CH03_UDP_PID" 2>/dev/null || true
kill -0 "$CH03_TCP_PID" 2>/dev/null && printf 'STOP: TCP PID still exists\n'
kill -0 "$CH03_UDP_PID" 2>/dev/null && printf 'STOP: UDP PID still exists\n'
trap - EXIT
exit
```

`exit` 後一次性 network namespace 隨最後一個其中的 process 結束而消失；它沒有建立 host route、firewall rule、published port 或 router 設定。回到原 shell 後，先離開暫存目錄，再只刪除自己建立的三個明確檔案；不使用廣域 prune、glob 或模糊名稱：

``` bash
cd /tmp
python3 -c 'from pathlib import Path; import sys; base=Path(sys.argv[1]); [base.joinpath(name).unlink(missing_ok=True) for name in ("ch03_transport_probe.py", "ch03-tcp.log", "ch03-udp.log")]' "$CH03_WORKDIR"
rmdir "$CH03_WORKDIR"
```

確認這三個路徑與 `$CH03_WORKDIR` 都不存在；不要在 host 重新連 `127.0.0.1:49152` 作為 cleanup 證據，因為 host 上可能有不屬於本章的服務。`rmdir` 失敗時只列出該精確目錄內容並停止，不刪未知檔案。

### 無法使用 namespace 時的紙上替代

若不符合實測能力，閱讀下列預先產生的本專案 trace，不執行命令：

``` text
BASE TCP: listener RECV marker=CH03-TCP-BASE；client ECHO_OK；exit=0
BASE UDP: client SEND_OK；listener RECV marker=CH03-UDP-BASE；client ECHO_OK；exit=0
TCP DOWN: UDP 仍 ECHO_OK；TCP NO_ECHO；exit=2
TCP RESTORED: TCP ECHO_OK；exit=0
UDP DOWN: TCP 仍 ECHO_OK；UDP 先 SEND_OK、後 NO_ECHO；exit=2；listener 無該 marker
UDP RESTORED: UDP SEND_OK + listener RECV + client ECHO_OK；exit=0
```

紙上判讀的結論上限和實測相同：listener 可獨立停止／恢復；同 numeric port 可在 TCP、UDP transport 脈絡各自存在；UDP send success 不等於接收。這份 trace 仍不能證明 NAT、firewall、Internet 行為、可靠性排名或效能。

## 13\. 本章一句話

NAT／NAPT 的 mapping、firewall 的 policy，以及 UDP／TCP 的 service semantics 是不同層次，必須用各自對應且範圍相符的 evidence 判斷。

## 14\. 五題理解題

### 第 1 題

某個 IPv4 address 不在 RFC 1918 的三段 private range 中，或剛好是在某層轉換的外側觀察位址，能否直接斷言它屬於 public/global realm 且全球可達？

\*\*答案解析：\*\*不能。Outside observed address 只描述特定觀察位置，可能仍是 RFC 1918 private-use、shared 或其他位址；public IP address 則限 RFC 2663 §2.7 的 public/global address realm，需有 registry allocation／global uniqueness 的證據。IANA registry 還列出多種非 RFC 1918 的 special-purpose IPv4 range；即使已證明具全域唯一性，route、policy、listener 與實際可達性仍是不同條件。

### 第 2 題

只把內側 IPv4 address 換成外側 address，與同時把 address 和 UDP port 都換掉，分別如何稱呼？

\*\*答案解析：\*\*前者屬 NAT；後者是更精確的 NAPT 子類。不能反過來把所有 NAT 都說成一定改 port。本章具體 mapping 行為例只限單播 UDP、內外都只談 IPv4 的 Traditional NAT 來源範圍。

### 第 3 題

已看見一筆 NAT mapping，是否代表 firewall 一定允許外側資料通過？

\*\*答案解析：\*\*不是。Mapping 是內外表示的狀態對應；firewall policy 是獨立的允許／阻擋判斷。至少要分別取得 mapping record 與對應方向、條件的 policy evidence，還要另確認目的 transport／listener。

### 第 4 題

UDP 沒有 TCP 式 connection establishment，是否代表 UDP 一定比 TCP 快？

\*\*答案解析：\*\*不是。UDP 保留 datagram 邊界但不內建 delivery、duplicate protection 或 ordering 保證；TCP 提供 reliable、in-order byte stream，可能因建立狀態、等待或重送產生不同取捨。實際結果還受應用、路徑、負載與實作影響，不能抽象排名；本章也不做效能 benchmark。

### 第 5 題

停止已知 UDP listener 後，client 顯示 `SEND_OK`，但觀察窗內沒有 receiver marker 或 echo，能證明什麼？

\*\*答案解析：\*\*只能說本機 send operation 成功後，觀察窗內仍沒有取得這次測試 datagram 的 application 接收／echo evidence。它不能證明一定是 NAT、firewall、Internet、WebRTC 或 transport 普遍故障，也不能把 UDP 說成建立 connection 失敗。

## 本章參考資料

  - [RFC 1918 / BCP 5: Address Allocation for Private Internets](https://www.rfc-editor.org/info/rfc1918) — Best Current Practice，1996-02；obsoletes RFC 1597、1627，updated by RFC 6761；查核日期 2026-08-12；只支援三段 IPv4 private address space 與 private internet 範圍，RFC 6761 的 special-use domain name 程序更新不拿來定義 address，也不把 RFC 1918 的補集定義成全球可達 public address。
  - [RFC 2663: IP Network Address Translator (NAT) Terminology and Considerations](https://www.rfc-editor.org/info/rfc2663) 與 [官方 errata](https://www.rfc-editor.org/errata/rfc2663) — Informational，1999-08；RFC Editor 未列 updates／obsoletes 關係；查核日期 2026-08-12；採 IPv4 address realm、Traditional NAT、Basic NAT、NAPT 與 mapping 入門術語，並依 §2.7 把 public/global realm 限定為使用 IANA 或相當 registry 分配、具全域唯一性 network address 的 realm；外側觀察位址另依觀察位置記錄。Verified Errata 400 修正 TCP termination 文字，本章不採該舊細節，TCP 語意改以 RFC 9293 為主。
  - [RFC 4787 / BCP 127: Network Address Translation Behavioral Requirements for Unicast UDP](https://www.rfc-editor.org/info/rfc4787) — Best Current Practice，2007-01；updated by RFC 6888、7857；查核日期 2026-08-12；只採單播 UDP、內外都只談 IPv4 的 Traditional NAT 情境中 mapping 與 filtering 分開、state 具時間／實作邊界的入門主張，不支援 TCP NAT、IPv6 NAT 或完整 firewall 定義。
  - [RFC 6888 / BCP 127: Common Requirements for Carrier-Grade NATs](https://www.rfc-editor.org/info/rfc6888) — Best Current Practice，2013-04；updates RFC 4787；查核日期 2026-08-12；只記錄 RFC 4787 的現行更新背景，不把 carrier-grade resource、logging、port allocation 或 subscriber-scale 要求套到所有 NAT。
  - [RFC 7857 / BCP 127: Updates to Network Address Translation Behavioral Requirements](https://www.rfc-editor.org/info/rfc7857) — Best Current Practice，2016-04；updates RFC 4787、5382、5508；查核日期 2026-08-12；本章只採其對 RFC 4787 UDP NAT requirements 的更新範圍，不藉片段拼出 TCP-through-NAT 教學，也不展開其他 NAT 類型。
  - [RFC 8085 / BCP 145: UDP Usage Guidelines](https://www.rfc-editor.org/info/rfc8085) — Best Current Practice，2017-03；obsoletes RFC 5405，updated by RFC 8899；查核日期 2026-08-12；支援 UDP datagram service、可靠性／順序非保證與應用壅塞責任；RFC 8899 更新的 datagram PLPMTUD 細節不納入本章，也不支持「UDP 一定較快」。
  - [RFC 9293 / STD 7: Transmission Control Protocol](https://www.rfc-editor.org/info/rfc9293) — Internet Standard，2022-08；updates RFC 1011、1122、5961；obsoletes RFC 793、879、2873、6093、6429、6528、6691；RFC Editor 於查核日未列 updated by；查核日期 2026-08-12；只採 TCP connection-oriented、reliable in-order byte-stream 與 retransmission 入門語意，不把可靠等同永不失敗或應用已處理，也不比較普遍速度。
  - [NIST SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) — NIST Final Publication，2009-09；查核日期 2026-08-12；只支持 firewall 依組織 policy 控制不同 security posture 網路／host 間 traffic flow 的有限入門模型，不推論 NAT、特定產品位置或所有部署條件。
  - [IANA IPv4 Special-Purpose Address Space](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) — Live registry，Created 2009-08-19，Last Updated 2025-10-09；查核日期 2026-08-12；只支持「非 RFC 1918 不等於一定 globally reachable」，不把 registry 當作單一 address 可達性測試。
  - [Python 3.10.12 documentation](https://docs.python.org/release/3.10.12/) — CPython 3.10.12；查核日期 2026-08-12；本章自寫單檔只使用 `argparse`、`socket`、`sys` 標準庫；source hash 與實測 OS／architecture 另在正文鎖定。
  - [util-linux `unshare(1)` manual](https://man7.org/linux/man-pages/man1/unshare.1.html) — 本輪實測 util-linux 2.37.2；查核日期 2026-08-12；只支持建立一次性 user／network namespace 的工具行為。實作若缺少 rootless user namespace 能力即改用紙上 trace，不使用 `sudo` 或 host network 權限。
  - [Linux `network_namespaces(7)` manual](https://man7.org/linux/man-pages/man7/network_namespaces.7.html) — Linux manual pages；查核日期 2026-08-12；只支持 network namespace 隔離 network devices、IPv4／IPv6 protocol stacks、routing tables、firewall rules 與 port/socket 空間，以及最後一個 member process 結束後釋放實體裝置的工具邊界；本章實測只啟用新 namespace 的 loopback。
  - [iproute2 `ip-link(8)` manual](https://man7.org/linux/man-pages/man8/ip-link.8.html)、[`ip-address(8)`](https://man7.org/linux/man-pages/man8/ip-address.8.html) 與 [`ip-route(8)`](https://man7.org/linux/man-pages/man8/ip-route.8.html) — 本輪實測 iproute2 5.15.0；查核日期 2026-08-12；只支持 `ip link` 啟用 namespace loopback，以及以 `ip address`／`ip route` 檢查該 namespace 的 address 與 route；不拿命令輸出證明 NAT、firewall 或 Internet 行為。
