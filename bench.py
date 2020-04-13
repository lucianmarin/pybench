from datetime import datetime
from statistics import mean

from memory_profiler import memory_usage
from progressbar import progressbar


def wallis(n):
    pi = 2.
    for i in progressbar(range(1, n)):
        left = (2. * i) / (2. * i - 1.)
        right = (2. * i) / (2. * i + 1.)
        pi = pi * left * right
    return pi


def fib_range(n):
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    for i in progressbar(range(1, n)):
        fib(i)


def fib_loop(n):
    f = 0
    s = 1
    for x in progressbar(range(2, n)):
        nxt = f + s
        f = s
        s = nxt
    print(len(str(s)), 'decimals')


def benchmnarks():
    print('calculating pi:')
    mem = memory_usage((wallis, [], {'n': 2**22}))
    print('mean mem:', mean(mem))

    print('\ncalculating fib recursive:')
    mem = memory_usage((fib_range, [], {'n': 2**5 + 2**2 + 2}))
    print('mean mem:', mean(mem))

    print('\ncalculating fib iterative:')
    mem = memory_usage((fib_loop, [], {'n': 2**20}))
    print('mean mem:', mean(mem))


def main():
    start = datetime.now()
    benchmnarks()
    end = datetime.now()
    result = end - start
    print('\nresult is', result)


if __name__ == "__main__":
    main()
