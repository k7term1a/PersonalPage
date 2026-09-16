# PersonalPage — 我的歷程資料庫 + 個人網頁

網頁：https://k7term1a.github.io/PersonalPage/

這個 repo 存的是履歷的**內容**（YAML + Markdown），不是履歷檔案。
每次 push 到 `main`，GitHub Actions 會自動：渲染中英 PDF → 產生個人網頁 → 部署到 GitHub Pages。

```
resume-en.yaml            英文主履歷（RenderCV 格式，唯一真相來源）
resume-zh.yaml            繁中主履歷
projects/*.md             證據庫：每個成就的完整背景、數字來源、待補事項
site/                     個人網頁產生器：build.py 讀兩份 YAML → index.html（中英切換、下載 PDF）
fonts/                    Noto Sans CJK TC（繁中 PDF 用）
.github/workflows/        CI：render PDF + build site + deploy Pages；tag v* 時發 Release
```

針對特定公司的客製版履歷**不放這裡**（`applications/` 已在 .gitignore），
由 Claude 的 `resume-build` skill 產生後放到另一個私人 repo。

## 本機預覽

```bash
pip install "rendercv[full]" jinja2 pyyaml
./fonts/get-fonts.sh
rendercv render resume-zh.yaml && rendercv render resume-en.yaml
python3 site/build.py && python3 -m http.server -d _site 8000
```

## 更新流程

1. 改 `resume-*.yaml`（兩種語言同步）；有新數字就在 `projects/` 補來源。
2. push 到 `main` → 幾分鐘後網頁與 PDF 更新。
3. 或在 Claude app 說「把 X 加進履歷」，skill 會開 `update/<日期>` 分支，你在 GitHub merge。

## 第一次啟用 Pages

Settings → Pages → Build and deployment → Source 選 **GitHub Actions**。
