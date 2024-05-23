# PyBench

PyBench 2.0 is a Python benchmark inspired by Geekbench.

The purpose is to optimize modern CPUs for Python and make sure new versions of Python are getting faster.

It can also be used as a syntetic CPU benchmark to run on computers and servers.


## Runtime

```
> python3 pybench.py
Compress using BZ2 algorithm:
[========================================] 100.0% Elapsed: 0:00:15
Compress using LZMA algorithm:
[========================================] 100.0% Elapsed: 0:00:15
Calculate Pi using Wallis product:
[========================================] 100.0% Elapsed: 0:00:14
Calculate Fibonacci numbers recursively:
[========================================] 100.0% Elapsed: 0:00:17
Calculate Fibonacci numbers iteratively:
[========================================] 100.0% Elapsed: 0:00:15
Multiply matrices:
[========================================] 100.0% Elapsed: 0:00:16
Benchmark time: 94.750028 seconds
```

## Benchmark times

- Python 3.12 on Apple M1 (power): 59.403723s
- Python 3.12 on Apple M1 (battery): 94.750028s
- Python 3.11 on Qualcomm Snapdragon 765G: 187.072155s
- Python 3.11 on Intel Core (Skylake, IBRS, 3792 MHz): 205.720891s
- Python 3.13 on Intel Xeon (2.20 GHz): 329.178737s

Less is always better!
