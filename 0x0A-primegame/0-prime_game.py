#!/usr/bin/python3
"""
This module contains prime game as explained in README.md
"""


def primeNumbers(n):
    """this function returns prime numbers between 1 and n
    using sieve of Eratosthenes algorithm
    """
    primeNos = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primeNos.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primeNos


def isWinner(x, nums):
    """this functions determines the winner of the game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for n in range(x):
        primeNos = primeNumbers(nums[n])
        if len(primeNos) % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
