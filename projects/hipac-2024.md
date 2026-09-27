# 2024 第三屆國網盃應用程式效能優化競賽（HiPAC 2024）冠軍 / HiPAC 2024 Champion

- 時間：2024（賽前約一年培訓）
- 主辦：國家實驗研究院國家高速網路與計算中心（NCHC）
- 隊名：我知你很急但你先別急（國立臺中教育大學資工系，6 人大學部團隊）
- 隊員：王品智、黃楷奇、陳幸妤、高健壹、黃俊傑、彭冠銘；指導老師黃國展主任、教練葉家郡
- 名次：冠軍（獎金 NT$100,000）；同屆亞軍清大、季軍明道／嘉中／建中聯隊
- 來源：決賽簡報（HiPAC-NTCU）、中教大新聞稿、NCHC 成果頁

## 賽題與做法
1. **叢集建置（Setup）**：針對 Infiniband 與 NVIDIA GPU 建置多節點環境
2. **監控（Monitoring）**：自製 exporter 降低監控成本，搭配 Prometheus / Grafana
3. **MPI 與 NUMA binding**：比較一般 MPI 與 NUMA 綁定後的效能差異
4. **HPL**：先以小記憶體占比測 NB，再逐步拉高 N 至記憶體約 83%
5. **HPCG**：賽前大量練習改變測資比例找規律（y < x 且 y < z），據此得最佳參數，並以腳本自動化測試
6. **電漿應用題 PIConGPU**：從原始碼建置，單節點與雙節點；A 參數約 2 小時全部達標，B 參數約 20 分鐘但不精確
7. **生醫應用題 NAMD 2.14**：自行編譯與官方執行檔比較；multicore、multicore-CUDA、雙節點 verbs-smp-CUDA；
   調整 `outputEnergies / outputTiming / dcdFreq / restartfreq`、`++ppn +pemap +comap +devices`，
   雙節點最佳 0.679 ns/day
8. **隱藏題**：密碼復原（md5 217/481、bcrypt 935/1494，總 1152/2500）、流體力學 PyFR

## 我的分工
- 負責**標準題型（HPL / HPCG benchmark）的參數優化**與**應用題型（PIConGPU、NAMD）**
- 備賽期間撰寫自動化腳本記錄並分析參數與效能的關聯（即上方 HPCG 的「找規律 → 最佳參數 → 腳本自動化測試」流程），並熟悉應用題型的安裝與執行方式
- 決賽運用賽前整理出的參數調校策略，協助團隊奪冠

## 技能對應
Slurm、Prometheus、Grafana、MPI、NUMA、Infiniband、CUDA、HPL/HPCG benchmark、從原始碼建置科學計算軟體

## 待補
- 決賽日期與總隊數
