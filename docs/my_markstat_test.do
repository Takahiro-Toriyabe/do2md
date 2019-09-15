clear all

/*md
% Quantiles in Stata and R
% Takahiro Toriyabe
% `s c(current_date)`

Stata and R compute percentiles differently. Let us load the `auto`
dataset and compute the 75th percentile of `price` using Stata's `centile`
md*/

sysuse auto, clear
centile price, centile(75)

/*md
We find that the 75-th percentile is `s r(c_1)`.

For a discussion of these methods see
Hyndman, R. J. and Fan, Y. (1996) Sample quantiles in statistical packages, 
*American Statistician* 50:361-365.
md*/

clear all
