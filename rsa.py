#!/bin/bash/python3
import sys


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factorize_rsa_number(n):
    p = 2
    while True:
        if n % p == 0 and is_prime(p):
            q = n // p
            if is_prime(q):
                return p, q
        p += 1


def factorize_file(filename):
    with open(filename, 'r') as file:
        number = int(file.readline().strip())
        p, q = factorize_rsa_number(number)
        print(f"{number}={p}*{q}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    factorize_file(filename)
