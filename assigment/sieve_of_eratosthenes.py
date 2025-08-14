# sieve_of_eratosthenes.py
# Implementation of the Sieve of Eratosthenes algorithm to generate prime numbers

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    return [num for num, is_prime in enumerate(primes) if is_prime]

if __name__ == "__main__":
    limit = 50
    print(f"Prime numbers up to {limit}:")
    print(sieve_of_eratosthenes(limit))
