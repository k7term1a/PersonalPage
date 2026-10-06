# 國網中心 LLM 團隊實習 / NCHC LLM Model Team Intern

- 時間：2025-03 ~ 至今
- 單位：國家高速網路與計算中心（NCHC）
- 來源：本人 HackMD 筆記（私人，2025-03 ~ 2026-02），只讀取未修改

## 1. 文獻 survey（LLM 資料、訓練與安全）
每篇整理成筆記並彙整於「論文筆記統整」（公開：https://hackmd.io/@kaichi）。
- 資料：OpenCSG Chinese Corpus、Datasets for LLMs: A Comprehensive Survey、FineWeb2、From Quantity to Quality（自導式指令資料篩選）、MAGPIE（對齊資料合成）
- 評測：Advancing the Evaluation of Traditional Chinese LMs（繁中 benchmark）
- 持續學習與遺忘：LAMOL、Forgetting-aware Pruning
- 安全與隱私：Safety-Tuned LLaMAs、VaultGemma、差分隱私（DP-SGD）研究
- 模型：MediaTek Breeze 2、NVIDIA Nemotron Nano 2
- 其他：LLM-based Data Science Agent survey、LAMBDA、MLOps survey（團隊 survey 中負責「雲端基礎設施」章節，與揚洲、健壹合寫）

## 2. 資料集備份 CI/CD（GitLab CI）
- 在國網 VM 自架 gitlab-runner，以 `.gitlab-ci.yml` 的 tag 指定 runner；解決 runner 使用者權限問題（共享群組）
- 流程分四個 stage：parse（解析 Notion 表格欄位）→ check（比對 Notion 紀錄與已備份清單）→ backup（下載 Hugging Face 資料集並推送備份）→ update（回寫 Notion 表格）
- 以容器執行腳本環境；支援 Notion table 與 database 兩種 API
- 筆記：「gitlab-ci」「測試 ci 流程」

## 3. 繁中教育語料分類器 PoC（類 FineWeb-Edu）
- 參考 FineWeb-Edu 流程：以 `Llama3-70B` 提示詞標記樣本是否適合教育主題 → 訓練分類器
- 資料：`jed351/Traditional-Chinese-Common-Crawl-Filtered`（768 GB，受限 100 GB 配額先取 30 GB，其中 3 GB 作分類器訓練樣本），下載時過濾過短／過長樣本並 hash 去重
- 分類器 backbone：`EmbeddingGemma-300m`，加分類頭；抽樣 10,000 筆標記資料檢視三類分布
- 結果：三分類正確率約 70%（參考作品 FineWeb-Edu-zhtw-Classifier 為 0.809）
- 筆記：「類 fineweb 實作」

## 4. 模型合併（model merging）PoC
- 研讀權重空間理論、Model Soup、任務向量；以 `mergekit` 做參數空間（PS）合併
- 以 TW-MGSM（繁中數學）與 TMMLU+ 評估合併前後模型
- 待補：最佳結果數字

## 5. 差分隱私（differential privacy）
- 研讀 DP 概念與 DP-SGD，並延伸閱讀 VaultGemma

## 6. 評測與資料合成相關實驗
- 答案萃取：比較「無限制」與「限制格式」回覆對 TMMLU+、MMLU-Pro、Penguins in Table 分數的影響（Llama 4）
- 觀察 Qwen、DeepSeek 對閩南語題目的回答；觀察 Gemma 3、Llama 4 的 embedding 數值偏差
- 以 `distilabel` 產生合成資料，記錄 cache、batch size 與生成數等參數影響；多輪對話生成格式實驗

## 7. 影像／影片辨識與 MCP（2026，國網指派）
- **Dify Agent + MCP 影片辨識**：使用者在 Dify 上傳影片並以自然語言要求分類，ReAct Agent 節點透過自架 MCP server 呼叫 K600（Kinetics-600）動作辨識推論服務；Agent 使用國網自架 OpenAI 相容 LLM 端點。處理過 Dify 相對 URL、簽名參數被覆蓋、Docker 連 host、zombie container 等問題（筆記「K600 影片辨識 MCP」）
- **K600 端到端延遲優化**：拆解延遲（錄製分段窗約 20 s 為主宰項、輪詢 2.5 s、前處理 p50 2.3 s、推論 p50 1.1 s），將錄製窗由 20 s 縮至 5 s：
  - e2e p50 **26.3 s → 10.8 s（−59%）**，p90 28.3 s → 12.7 s
  - 前處理 p50 2.39 s → 1.62 s
  - 準確度：top-5 一致率 100%、top-1 一致率 87.5%（140/160），top-1 信心 p50 46.8% → 48.7%
  - 筆記「K600 辨識系統減少延遲」
- **影片模型實驗**：VideoMAE v2 / K710 多片段推論與分類頭（Linear / MLP、+LayerNorm）比較，v2 MLP + LN top-1 54.5% → 56.5%；推論改為只解碼需要的幀、batch 合併 forward、ThreadPool 並行前處理
- **研究規劃與 survey**：DINOv3 與 Video Swin Transformer 在 K400 的訓練差異比較；規劃 Video Swin → MLP Projector → Gemma-4-E4B 的影片 VLM 兩階段訓練（模態對齊、指令微調）；MCP 技術報告；影像辨識服務 survey；Gemma 4 家族介紹
- **資料記錄改版 survey**（2026-09）：評估可在 GitLab CI / Pages / Package Registry + MinIO 上運作、無需常駐服務的資料集紀錄方案（HF Hub datasets、Croissant、Datasheets/Data Cards 等）

## 8. 語料蒐集流程
- 見 hf-extractor-lambda.md；並整理「繁體中文資料集彙整」（CC、維基、政府文件、新聞等來源）

## 環境
- 國網 VM：NVIDIA driver、CUDA 12.8 / 11.8、Environment Modules 建置（筆記「nchc vm」）
- 資料生成 pipeline（`NCHC_data_pipeline.sh`）相依性除錯：逐版測試 pydantic、openai 等套件找出可用版本範圍（筆記「NCHC shell 腳本套件版本問題」）

## 待補
- 模型合併的分數變化（筆記只有截圖）
- CI/CD 實際備份的資料集數量與容量
- LAMBDA 語料流程處理的資料集數量

## 關鍵字
LLM research, literature survey, data curation, FineWeb-Edu, classifier, model merging, mergekit, differential privacy, GitLab CI/CD, gitlab-runner, Hugging Face, Notion API, distilabel, evaluation, TMMLU+
