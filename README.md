# PyBench

PyBench 2.0 is a Python benchmark inspired by Geekbench.

The purpose is to optimize modern CPUs for Python and make sure new versions of Python are getting faster.

It can also be used as a syntetic CPU benchmark to run on computers and servers.


## Install and run

```
pip install -r requirements.txt
python3 pybench.py
```

## Benchmark times

- Python 3.12 on Apple M1: 65.637987s
- Python 3.11 on Intel Core (Skylake, IBRS, 3792 MHz): 86.659294s
- Python 3.13 on Intel Xeon (2.20 GHz): 146.932857s
- Python 3.11 on Qualcomm Snapdragon 765G: 252.073677s

Less is always better!
