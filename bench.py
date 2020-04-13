from datetime import datetime

from tqdm import tqdm


def wallis(n):
    pi = 2.
    for i in tqdm(range(1, n)):
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
    for i in tqdm(range(1, n)):
        fib(i)


def fib_loop(n):
    f = 0
    s = 1
    for x in tqdm(range(2, n)):
        nxt = f + s
        f = s
        s = nxt
    print(len(str(s)), 'decimals')


def benchmnarks():
    print('calculating pi:')
    wallis(2**22)

    print('\ncalculating fib recursive:')
    fib_range(2**5 + 2**2 + 2)

    print('\ncalculating fib iterative:')
    fib_loop(2**20)


def main():
    start = datetime.now()
    benchmnarks()
    end = datetime.now()
    result = end - start
    print('\nbenchmark time:', result)


if __name__ == "__main__":
    main()
