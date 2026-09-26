# AWS Summit Taipei 2026 AI Hackathon 航運物流組 第一名 / AWS Summit Taipei 2026 AI Everywhere Hackathon, 1st Place (Shipping & Logistics Track)

- 時間：2026-07-15 ~ 07-16，台北國際會議中心（TICC）
- 主辦：AWS；五家企業出題，航運物流組由陽明海運出題「物流業的效率瓶頸」
- 隊名：ICTALAB（中興大學資工系 工商暨交通數據分析實驗室，5 人：2 博士 + 3 碩士）
- 名次：航運物流組第一名（完賽證明編號 28）
- 來源：決賽簡報《Oil! 船隻能效營運管理決策平台》

## 作品
船隊能效營運決策平台：Speed Loss 儀表板（15 艘船隊狀態、維護甘特圖、單船日誌與歸因）、
維護決策（清潔動作效益試算、建議日期、帶入市場油價）、預警訂閱、AI 顧問（RAG + LLM Wiki，回答附來源）。部署於 AWS。

## 模型
- 資料清洗：Noon Reports 21,282 筆 → 去重 / 衝突群組 → 8,057 筆正式訓練資料；多燃料依低位熱值換算 VLSFO 等效 DailyFOC
- 特徵：46 個（RPM²/³、STW²/³、速度反應效率、SOG−STW 差異、低速穩定化）
- 比較 direct / stacked / aux ME / aux physics 四種策略：**CatBoost direct 最佳，MAE 2.39 MT、WAPE 3.34%、R² 0.9836**
- SHAP：RPM 家族合計 44.4% 重要性；明確標註 SHAP 是解釋不是因果

## 我的分工
- 資料清洗（Noon Reports 去重、衝突群組處理、多燃料換算）與油耗模型（特徵設計、CatBoost 策略比較、SHAP）
- 注意：比賽以 AWS 免費額度為前提，平台前後端大量使用 AI 輔助開發（vibe coding）；
  履歷上只主張資料處理與建模能力，不主張前端／雲端架構

## 待補
- 用到的 AWS 服務清單
- 決賽隊數
