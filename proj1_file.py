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

#function for setting each user's p & q values to random prime nums with the specified range
def gen_rand_user_prime(user_dicts, minPrime, maxPrime):
    for i in user_dicts:
        i["p"] = generate_random_prime(minPrime, maxPrime)
        i["q"] = generate_random_prime(minPrime, maxPrime)

def calc_n_phi(user_dicts):
    for i in user_dicts:
        n = i["p"] * i["q"]
        i["n"] = n

        phi = (i["p"] - 1) * (i["q"] - 1)
        i["phi"] = phi

def compute_d(user_dicts, e_val):
    for i in user_dicts:
        d = pow(e_val, -1, i["phi"])
        i["d"] = d

def rsaAlgoKeys(user_dicts, e_val, minPrime, maxPrime):
    gen_rand_user_prime(user_dicts, minPrime, maxPrime)
    calc_n_phi(user_dicts)
    compute_d(users, e_val)

if __name__ == '__main__':
    # Testing prime num generation
    minPrimeRange = 2
    maxPrimeRange = 1000
    prime_number = generate_random_prime(minPrimeRange, maxPrimeRange)
    print("Prime Num Test:", prime_number)

    #storing users as dictionaries so process of storing/updating/adding values is simple and repeatable
    alice = {"Name": "Alice", "p": -1, "q": -1}
    mike = {"Name": "Mike", "p": -1, "q": -1}
    greg = {"Name": "Greg", "p": -1, "q": -1}
    users = [alice, mike, greg]
    #RSA Process Below, may consolidate into single function as needed
    gen_rand_user_prime(users, minPrimeRange, maxPrimeRange)
    calc_n_phi(users)
    standard_e_val = 65537 # picked because common public e values are 3, 5, 17, 257, or 65537
    compute_d(users, standard_e_val)

    print(users)

