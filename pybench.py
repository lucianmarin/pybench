import string
from bz2 import BZ2Compressor
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from lzma import LZMACompressor
from multiprocessing import cpu_count
from random import random

from tqdm import tqdm


def pi_wallis(iterations):
    pi = 2.
    for i in tqdm(range(1, iterations)):
        left = (2. * i) / (2. * i - 1.)
        right = (2. * i) / (2. * i + 1.)
        pi = pi * left * right


def fibonacci_recursive(n):
    def fibonacci(n):
        if n <= 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    cpus = cpu_count()
    with ThreadPoolExecutor(max_workers=cpus) as executor:
        futures = [executor.submit(fibonacci, i) for i in range(1, n)]
        with tqdm(total=n) as pbar:
            for future in as_completed(futures):
                pbar.update()


def fibonacci_iterative(n):
    first, second = 0, 1
    for _ in tqdm(range(2, n)):
        first, second = second, first + second


def multiply_matrices(size):
    A = [[random() for _ in range(size)] for _ in range(size)]
    B = [[random() for _ in range(size)] for _ in range(size)]
    C = [[0 for _ in range(size)] for _ in range(size)]

    for i in tqdm(range(size)):
        for j in range(size):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(size))


def compress(n, c_class, c_args=[]):
    c = c_class(*c_args)
    zero = b"0"
    data = string.ascii_letters + string.digits + string.whitespace + string.punctuation
    for i in tqdm(range(n)):
        c.compress(data.encode() * n)
    c.flush()


def benchmnarks():
    print('Compress using BZ2:')
    compress(n=2**10, c_class=BZ2Compressor, c_args=[1])

    print('Compress using LZMA:')
    compress(n=2**11, c_class=LZMACompressor)

    print('Calculate Pi using Wallis product:')
    pi_wallis(2**26)

    print('\nCalculate Fibonacci numbers recursively:')
    fibonacci_recursive(2**5 + 2**3)

    print('\nCalculate Fibonacci numbers iteratively:')
    fibonacci_iterative(2**20)

    print('\nMultiply matrices:')
    multiply_matrices(2**9)


def main():
    start = datetime.now()
    benchmnarks()
    end = datetime.now()
    result = end - start
    print('\nBenchmark seconds:', result.total_seconds())


if __name__ == "__main__":
    main()
