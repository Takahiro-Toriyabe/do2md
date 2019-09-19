capture program drop markstat_wrapper
program define markstat_wrapper
	syntax anything, output(string)

	tempname path_do2stmd path_temp dir_temp
	
	* Path to do2stmd.py
	local `path_do2stmd' = subinstr("`c(sysdir_plus)'/m/do2stmd.py", "\", "/", .)
	local `path_do2stmd' = subinstr("``path_do2stmd''", "//", "/", .)
	
	* Path to intermediate file directory
	local `path_temp' = subinstr(subinstr("`c(tmpdir)'/", "\", "/", .), "//", "/", .)

	capture mkdir "``path_temp''`dir_temp'"
	while _rc != 0 {
		tempname dir_temp
		capture mkdir "``path_temp''`dir_temp'"
	}

	* Make stmd file from do-file
	shell python "``path_do2stmd''" `anything' "``path_temp''`dir_temp'/tmp.stmd"

	* Use marksstat
	markstat using "``path_temp''`dir_temp'/tmp", nor

	* Make markdown file from html file
	shell pandoc "``path_temp''`dir_temp'/tmp.html" -o "``path_temp''`dir_temp'/tmp.md"
	shell sed -r "s/\ \{\.stata\}/Stata/" "``path_temp''`dir_temp'/tmp.md" > "`output'"
end
