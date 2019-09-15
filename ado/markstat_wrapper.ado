program define markstat_wrapper
	syntax anything, path_stmd(string)
	
	tempname adopath output_name
	local `adopath' "`c(sysdir_plus)'/m"
	local `output_name' = subinstr("`path_stmd'", ".stmd", "", .)

	shell python "``adopath''/do2stmd.py" "`anything'" "`path_stmd'"
	markstat using "``output_name''", nor

	shell pandoc "``output_name''.html" -o "``output_name''.md"
	shell sed -i -r "s/\ \{\.stata\}/Stata/" "``output_name''.md"
end
