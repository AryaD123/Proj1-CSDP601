# RSA Cryptography Algorithm
This project implements the RSA Cryptography Algorithm for secure communication. The program generates RSA keys for multiple users, encrypts and decrypts messages using these keys, and demonstrates the core principles of RSA.

## Overview
The RSA algorithm relies on the use of prime numbers to generate a public-private key pair, which is then used for secure message transmission. The program simulates this process for a group of users by:

- Generating random prime numbers.
- Computing public and private keys.
- Encrypting and decrypting messages.
## Features:
### Key Generation: 
- For each user, two random prime numbers are selected within a specified range to generate public and private keys.
### Message Encryption: 
- Converts a plaintext message into an encrypted form using the public key.
### Message Decryption: 
- Recovers the original message using the private key.
## Functions:
### gcd(a, b): 
- Calculates the greatest common divisor of two numbers.
###is_prime(n):
- Checks if a number is prime.
### generate_random_prime(start, end):
- Generates a random prime number within a specified range.
### gen_rand_user_prime:
- Assigns random prime numbers to users.
### calc_n_phi:
- Computes the RSA modulus n and phi.
### compute_d:
- Calculates the private key d.
### rsaAlgoKeys:
- Runs the process of generating keys for all users.
### input_reciever:
- Handles message input, encryption, and decryption.
