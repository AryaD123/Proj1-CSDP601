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

def gen_rand_user_prime(user_dicts, minPrime, maxPrime):
    for i in user_dicts:
        i["p"] = generate_random_prime(minPrime, maxPrime)
        i["q"] = generate_random_prime(minPrime, maxPrime)

if __name__ == '__main__':
    # Testing prime num generation
    minPrimeRange = 2
    maxPrimeRange = 100
    prime_number = generate_random_prime(minPrimeRange, maxPrimeRange)
    print(prime_number)

    alice = {"p": -1, "q": -1}
    mike = {"p": -1, "q": -1}
    greg = {"p": -1, "q": -1}
    users = [alice, mike, greg]
    gen_rand_user_prime(users, minPrimeRange, maxPrimeRange)
    print(users)

