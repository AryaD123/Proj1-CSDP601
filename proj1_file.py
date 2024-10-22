"""
Arya Das
CSDP 601 - Prof. Stone
Fall 2024 - UMES
Project 1
Description: Program for  implementing RSA Cryptography Algorithm
"""

import random
import math #using libraries to check if numbers are prime and to select random prime nums


# function for greatest common divisor
def gcd(a, b):
    temp = 0
    while(1):
        temp = a % b
        if (temp == 0):
            return b
        a = b
        b = temp

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

if __name__ == '__main__':
    minPrimeRange = 2
    maxPrimeRange = 100
    prime_number = generate_random_prime(minPrimeRange, maxPrimeRange)
    print(prime_number)

