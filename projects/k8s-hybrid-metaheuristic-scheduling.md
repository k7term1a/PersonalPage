# Kubernetes 混合式啟發式排程 / Hybrid Metaheuristic Scheduling for Kubernetes

- 時間：2024-11 ~ 2025-02
- 身分：大學專題（國立台中教育大學，ntcu114）
- Repo：https://github.com/k7term1a/ntcu114-yunikorn-core/tree/ntcu114-project

## 背景
Kubernetes 批次工作排程問題，以 Apache YuniKorn 排程器為實驗平台。

## 我做了什麼
- 結合蟻群演算法（ACO）與蚱蜢最佳化（Grasshopper Optimization, GOA）設計混合式排程策略
- 在 YuniKorn core 上實作並進行實驗評估

## 結果與數字
- GOA 使 ACO 收斂速度提升近 50%（TODO：量測指標是迭代次數還是 wall-clock？實驗規模、節點數、工作數？）
- ACO 提升了 GOA 排程的解品質（TODO：品質指標是 makespan / 資源利用率？提升多少？）

## 技術
Go（YuniKorn）, Kubernetes, ACO, Grasshopper Optimization, 排程模擬

## 關鍵字
Kubernetes scheduling, metaheuristics, YuniKorn, batch scheduling, resource management, Go

## 待補（面試會被問）
- 團隊人數與我的分工
- 與 YuniKorn 預設排程器的對照數據
