from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from multiprocessing import cpu_count
from lzma import LZMACompressor
from bz2 import BZ2Compressor

from tqdm import tqdm


def wallis(n):
    pi = 2.
    for i in tqdm(range(1, n)):
        left = (2. * i) / (2. * i - 1.)
        right = (2. * i) / (2. * i + 1.)
        pi = pi * left * right
    # print(len(str(pi)), 'decimals')


def fib_range(n):
    def fib(n):
        if n <= 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    # for i in tqdm(range(1, n)):
    #     fib(i)
    cpus = cpu_count()
    with ThreadPoolExecutor(max_workers=cpus) as executor:
        fibs = [executor.submit(fib, i) for i in range(1, n)]
        with tqdm(total=n) as pbar:
            for future in as_completed(fibs):
                pbar.update()


def fib_loop(n):
    f = 0
    s = 1
    for x in tqdm(range(2, n)):
        nxt = f + s
        f = s
        s = nxt
    # print(len(str(s)), 'decimals')


def compress(n, c_class, c_args=[]):
    c = c_class(*c_args)
    zero = b"0"
    for i in tqdm(range(n)):
        c.compress(zero * n)
    c.flush()


def benchmnarks():
    print('compressing bz2:')
    compress(n=2**15, c_class=BZ2Compressor, c_args=[1])

    print('compressing lzma:')
    compress(n=2**15, c_class=LZMACompressor)

    print('calculating pi:')
    wallis(2**25)

    print('calculating fib recursive:')
    fib_range(2**5 + 2**2 + 2)

    print('calculating fib iterative:')
    fib_loop(2**20)


def main():
    start = datetime.now()
    benchmnarks()
    end = datetime.now()
    result = end - start
    print('benchmark time:', result)


if __name__ == "__main__":
    main()
