#!/usr/bin/env bash
# 下載 Noto Sans CJK TC 靜態 OTF（Regular + Bold），供 RenderCV/Typst 渲染繁體中文。
# 建議執行一次後把字型 commit 進 repo，之後 clone 就不必再下載。
set -euo pipefail
cd "$(dirname "$0")"
BASE="https://github.com/notofonts/noto-cjk/raw/main/Sans/OTF/TraditionalChinese"
for w in Regular Bold; do
  f="NotoSansCJKtc-$w.otf"
  if [ ! -s "$f" ]; then
    echo "downloading $f ..."
    curl -sSL -o "$f" "$BASE/$f"
  fi
done
ls -la *.otf
