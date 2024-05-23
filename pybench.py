import string
from bz2 import BZ2Compressor
from datetime import datetime
from lzma import LZMACompressor
from random import random
from time import time


def progress_bar(iterable, total=None, start_time=None):
    total = total or len(iterable)
    bar_width = 40
    start_time = start_time or time()

    def show_progress(iteration):
        progress = int(bar_width * iteration / total)
        elapsed_time = time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        elapsed_str = "{:01}:{:02}:{:02}".format(
            int(hours), int(minutes), int(seconds)
        )

        bar = "=" * progress + " " * (bar_width - progress)
        percent_complete = (iteration / total) * 100
        output = f"\r[{bar}] {percent_complete:.1f}% Elapsed: {elapsed_str}"
        print(output, end='', flush=True)

    for i, item in enumerate(iterable, 1):
        yield item
        show_progress(i)

    print()  # newline after progress bar completion


def pi_wallis(n):
    pi = 2.
    for i in progress_bar(range(1, n)):
        left = (2. * i) / (2. * i - 1.)
        right = (2. * i) / (2. * i + 1.)
        pi = pi * left * right


def fibonacci_recursive(n):
    def fibonacci(n):
        if n <= 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    for i in progress_bar(range(1, n)):
        fibonacci(i)


def fibonacci_iterative(n):
    first, second = 0, 1
    for _ in progress_bar(range(2, n)):
        first, second = second, first + second


def multiply_matrices(size):
    A = [[random() for _ in range(size)] for _ in range(size)]
    B = [[random() for _ in range(size)] for _ in range(size)]
    C = [[0 for _ in range(size)] for _ in range(size)]

    for i in progress_bar(range(size)):
        for j in range(size):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(size))


def compress(n, algo_class, algo_args=[]):
    algo = algo_class(*algo_args)
    data = string.printable.encode()
    for i in progress_bar(range(n)):
        algo.compress(data * n)
    algo.flush()


def benchmarks():
    print('Compress using BZ2 algorithm:')
    compress(n=2**10, algo_class=BZ2Compressor, algo_args=[1])

    print('Compress using LZMA algorithm:')
    compress(n=2**11 + 2**10, algo_class=LZMACompressor)

    print('Calculate Pi using Wallis product:')
    pi_wallis(2**21 + 2**20)

    print('Calculate Fibonacci numbers recursively:')
    fibonacci_recursive(2**5 + 2**2 + 2 + 1)

    print('Calculate Fibonacci numbers iteratively:')
    fibonacci_iterative(2**19 + 2**18)

    print('Multiply matrices:')
    multiply_matrices(2**9)


def main():
    start = datetime.now()
    benchmarks()
    end = datetime.now()
    result = end - start
    print('Benchmark time:', result.total_seconds(), 'seconds')


if __name__ == "__main__":
    main()
