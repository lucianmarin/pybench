# PyBench

PyBench 3.0 is a Python benchmark inspired by Geekbench.

The purpose is to optimize modern CPUs for Python and make sure new versions of Python are getting faster.

It can also be used as a syntetic CPU benchmark to run on computers and servers.

## Runtime

```
> python3 bench.py
Compress using LZW algorithm:
[========================================] 100.0% 0:00:08
Calculate Pi using Wallis product:
[========================================] 100.0% 0:00:09
Calculate Fibonacci numbers recursively:
[========================================] 100.0% 0:00:12
Calculate Fibonacci numbers iteratively:
[========================================] 100.0% 0:00:07
Multiply matrices:
[========================================] 100.0% 0:00:07
Benchmark time: 45.7459 seconds
```

## Benchmark times

- Python 3.14 on Apple M1 (power): 45.7459 seconds
- Python 3.14 on Apple M1 (battery): 72.7001 seconds
- Python 3.14 on Apple M4 (power): 28.7314 seconds
- Python 3.13 on Intel Xeon: 75.4398 seconds
- Python 3.13 on Samsung Exynos 1680: 84.6202 seconds

Less is always better!

Intel Xeon running at 4 GHz powers the server hosting [Subreply](https://subreply.com/) - a tiny, but mighty social network.
