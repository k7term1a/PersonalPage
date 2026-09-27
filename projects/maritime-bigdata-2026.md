# 第六屆航港大數據創意應用競賽 學生組第一名 / 6th Maritime & Port Big Data Innovation Competition, 1st Place (Student Group)

- 時間：2026-03 報名 ~ 2026-08 決賽（決賽 8/10–8/12）
- 主辦：交通部航港局；須使用 iMarine 航港發展資料庫
- 名次：學生組第一名（獎金 NT$150,000）
- 隊名：SpaceY，作品《永續智能航港生態系》
- 決賽由隊長上台簡報（時間短），我與其他隊員在台下準備評審問答
- 我負責的兩個子系統（NCHU-ICTALab 組織下，commit 皆為我）：
  - https://github.com/NCHU-ICTALab/typhoon-evacuation-rl
  - https://github.com/NCHU-ICTALab/port-resilience-whatif
- 整體架構：獨立 Python 後端 + 無狀態 JSON 契約 + iMarine 前端 provider 播放（數位孿生）

## 子系統 1：颱風封港前船舶撤離排序（RL）
- 問題：封港倒數下，依船舶整備、港口入口與拖船容量產生派船／等待順序；操作人員可調「艘數 / 總噸位 GT / 風險點」三維偏好
- 方法：Soft Mixture-of-Experts PPO。四個 frozen experts（艘數、平衡、GT、風險）+ preference router + state router，
  vector critic 輸出三維 value；封港截止、入口容量、拖船容量以 action mask 硬限制
- 資料：iMarine 歷史出港快照（30 艘情境）+ 合成封港情境；24 個日期訓練，最後 5 個日期 held-out
- 結果（held-out，60 組配對情境）：
  - 四種偏好 weighted utility 均高於 FCFS：艘數 +1.40%、平衡 +2.65%、GT +2.10%、風險 +4.51%
  - 連續偏好 simplex 900 組配對：15/15 偏好點勝 FCFS，平均相對提升 +2.46%；每情境平均 3.23 個非支配候選
  - safety violations 0
- 誠實邊界：以 branch-and-bound oracle 證明 value-density 規則已距上限 1–3%，RL regret 11–16%；
  因此定位為「多偏好 Pareto 排程服務」而非「打敗規則」
- 工程：pytest 測試（env / mask / PPO / router / API）、HTTP API、前端

## 子系統 2：高雄港全災害產能衝擊 what-if（NSGA-II）
- 問題：港口設施受損／徵用下，72 小時內商船如何重分配、代價多大
- 方法：random-key NSGA-II（population 80、generation 80）產生 Pareto 候選；
  獨立 `validate_schedule` 重算硬限制；縮小實例以 CP-SAT 交叉驗證；FCFS、優先權規則、官方 VTS 規則仿真三種基準
- 結果（20 艘歷史案例，1068 泊位第 10–58 小時停用）：
  相較公開優先規則仿真，商船總等待 −5.25 h（−4.46%）、排程完成時間 −5.46 h（−10.82%）、硬限制違規 0
- 產出 `resilience.human_review.v1` 人工評估封包與確定性事件日誌供前端播放

## 技術
Python, PyTorch, PPO / Mixture-of-Experts, multi-objective RL, NSGA-II, CP-SAT (OR-Tools), SQLite, REST API, pytest

## 待補
- 隊伍人數與其他成員負責的部分（前端、其他子系統）
