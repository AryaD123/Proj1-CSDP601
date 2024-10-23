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

def input_reciever(user_dicts, e_val):
    print()
    for i in range(len(user_dicts)):
        print((i+1), ":", user_dicts[i]["Name"])
    chosen = int(input("Choose a user or type -1 to exit: ")) - 1
    if chosen < 0:
        return -1

    raw_msg = input("Enter a Message for user named " + user_dicts[chosen]["Name"] + ": ")
    #user_dicts[chosen]["Input"] = raw_msg
    raw_msg_split = []
    ascii_msg = []
    for j in raw_msg:
        raw_msg_split.append(j)
        ascii_msg.append(ord(j))
    print(raw_msg_split)
    print(ascii_msg)

    encrypted_split_msg = []
    for k in ascii_msg:
        C = (k ** e_val) % user_dicts[chosen]["n"]
        encrypted_split_msg.append(C)
        #print(k, chr(k), "encrypted: ", C, chr(C))
        print(f"Letter {chr(k)} (ascii {k}) ->encrypted-> {chr(C)} (Value {C})")

    print()
    decrypted_split_msg = []
    for l in encrypted_split_msg:
        M = (l ** user_dicts[chosen]["d"]) % user_dicts[chosen]["n"]
        decrypted_split_msg.append(M)
        #print(l, chr(l), "decrypted: ", M, chr(M))
        print(f"Letter {chr(l)} (ascii {l}) ->decrypted-> {chr(M)} (Value {M})")

    return 1


if __name__ == '__main__':
    print("Starting RSA Cryptography Algorithm...")
    #storing users as dictionaries so process of storing/updating/adding values is simple and repeatable
    alice = {"Name": "Alice", "p": -1, "q": -1}
    mike = {"Name": "Mike", "p": -1, "q": -1}
    greg = {"Name": "Greg", "p": -1, "q": -1}
    users = [alice, mike, greg]

    standard_e_val = 65537 # picked because common public e values are 3, 5, 17, 257, or 65537
    minPrimeRange = 2
    maxPrimeRange = 1000
    rsaAlgoKeys(users, standard_e_val, minPrimeRange, maxPrimeRange)

    #print(users)
    for i in users: print(i)
    encrypt_decrypt_message = 0
    while(encrypt_decrypt_message > -1):
        print()
        encrypt_decrypt_message = input_reciever(users, standard_e_val)
        for i in users: print(i)
        print()
    print("...Finished Running")
