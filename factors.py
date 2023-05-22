#!/bin/bash/python3
import sys


def factorize_number(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors


def factorize_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize_number(number)
            for factor_pair in factors:
                p, q = factor_pair
                print(f"{number}={p}*{q}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    factorize_file(filename)
