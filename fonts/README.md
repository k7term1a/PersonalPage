# fonts/

RenderCV 會自動把 YAML 同層的 `fonts/` 加進字型搜尋路徑，所以繁中履歷只要在
`design.typography.font_family` 指定 `Noto Sans CJK TC` 即可。

第一次請執行 `./get-fonts.sh`（約 33 MB），然後把 `.otf` 一起 commit。
如果不想把字型放進 repo，Claude 的 `resume-build` skill 也會在缺字型時自動下載。
