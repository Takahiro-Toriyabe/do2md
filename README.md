# markstat-wrapper
Wrapper of markstat in Stata to facilitate dynamic document

## Prerequisite

1. Install [Pandoc](https://github.com/jgm/pandoc)
2. Install `markstat` and `whereis` into Stata
3. Use `whereis` to set the path of the Pandoc and LaTeX (See [Germán's web page](https://data.princeton.edu/stata/markdown/gettingStarted) for detail)
4. If you make pdf file, copy [stata.sty](https://github.com/Takahiro-Toriyabe/markstat-wrapper/blob/master/docs/stata.sty) to the appropriate place (and run `mktexlsr` on your terminal to update style-file list in case of TeX Live)
5. If your OS is Windows, you may need to install gnu-sed
6. Copy and paste [markstat_wrapper.ado](https://github.com/Takahiro-Toriyabe/markstat-wrapper/blob/master/ado/markstat_wrapper.ado) and [do2stmd.py](https://github.com/Takahiro-Toriyabe/markstat-wrapper/blob/master/python/do2stmd.py) to `[adoPATH]/m/` (`[adoPATH]` may be "C:/ado/plus/")

```Stata
ssc install markstat
ssc install whereis
whereis pandoc "[PATH]/pandoc.exe"
whereis pdflatex "[PATH]/pdflatex.exe"
whereis R "[PATH]/R.exe" /* If you use R */
```

## Usage

- Source do-file for markstat-wrapper is basically the same as usual do-file
- Markdown part should start with `/*md` and end with `md*/`
```Stata
Stata command
/*md
Markdown line 1
Markdown line 2
md*/
Stata command
```
- DO NOT write anything in the line with `/*md` or `md*/`. For example, the following does not work
```Stata
Stata command
/*md Markdown line 1
Markdown line 2
md*/
Stata command
```
- See [src.do](https://github.com/Takahiro-Toriyabe/markstat-wrapper/blob/master/docs/example/src.do) for an example of the source file
- Syntax of Stata command `markstat_wrapper` is `markstat_wrapper src_file, output(output_file)`
  - src_file: Source file (.do)
  - output_file: output file name (.md)
- For example,
  ```Stata
  markstat_wrapper markstat_wrapper "src.do", output("result.md")
  ```
