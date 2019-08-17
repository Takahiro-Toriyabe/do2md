# markstat-wrapper
Wrapper of markstat in Stata to facilitate dynamic document

## Prerequisite

1. Install [Pandoc](https://github.com/jgm/pandoc)
2. Install `markstat` and `whereis` into Stata
3. Use `whereis` to set the path of the Pandoc and LaTeX (See [Germán's web page](https://data.princeton.edu/stata/markdown/gettingStarted) for detail)
4. If you make pdf file, copy [stata.sty](https://github.com/Takahiro-Toriyabe/markstat-wrapper/blob/master/docs/stata.sty) to the appropriate place (and run `mktexlsr` on your terminal to update style-file list in case of TeX Live)

```Stata
ssc install markstat
ssc install whereis
whereis pandoc "[PATH]/pandoc.exe"
whereis pdflatex "[PATH]/pdflatex.exe"
whereis R "[PATH]/R.exe" /* If you use R */
```
