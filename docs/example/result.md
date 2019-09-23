```Stata
. clear all
```

% Quantiles in Stata and R % Takahiro Toriyabe % 23 Sep 2019

Stata and R compute percentiles differently. Let us load the `auto`
dataset and compute the 75th percentile of `price` using Stata's
`centile`

```Stata
. sysuse auto, clear
(1978 Automobile Data)

. centile price, centile(75)

                                                       -- Binom. Interp. --
    Variable │       Obs  Percentile    Centile        [95% Conf. Interval]
─────────────┼─────────────────────────────────────────────────────────────
       price │        74         75        6378        5798.432      9691.6
```

We find that the 75-th percentile is 6378.

For a discussion of these methods see Hyndman, R. J. and Fan, Y. (1996)
Sample quantiles in statistical packages, *American Statistician*
50:361-365.

```Stata
. clear all
```
