# PyBench

PyBench 2.0 is a Python benchmark inspired by Geekbench.

The purpose is to optimize modern CPUs for Python and make sure new versions of Python are getting faster.

It can also be used as a syntetic CPU benchmark to run on computers and servers.

## Runtime

```
> python3 pybench.py
Compress using BZ2 algorithm:
[========================================] 100.0% 0:00:15
Compress using LZMA algorithm:
[========================================] 100.0% 0:00:16
Calculate Pi using Wallis product:
[========================================] 100.0% 0:00:13
Calculate Fibonacci numbers recursively:
[========================================] 100.0% 0:00:17
Calculate Fibonacci numbers iteratively:
[========================================] 100.0% 0:00:15
Multiply matrices:
[========================================] 100.0% 0:00:16
Benchmark time: 93.9806 seconds
```

## Benchmark times

- Python 3.12 on Apple M1 (power): 59.4037s
- Python 3.12 on Apple M1 (battery): 93.9806s
- Python 3.11 on Qualcomm Snapdragon 765G: 187.0722s
- Python 3.11 on Intel Core (Skylake, IBRS, 3792 MHz): 205.7209s
- Python 3.13 on Intel Xeon (2.20 GHz): 329.1787s

Less is always better!

Intel Core running at near 4 GHz powers the server hosting [Subreply](https://subreply.com/) - a tiny, but mighty social network.
