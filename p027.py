from math import sqrt, ceil


def is_prime(num):
    divisors = range(2, num)
    if num <= 1:
        return False

    for i in divisors:
        if num % i == 0:
            return False

    return True


def sieve(number):
    all_numbers = list(range(1, number))
    default_state = [2] * len(all_numbers)
    numbers_dict = {i: j for i, j in zip(all_numbers, default_state)}
    cutoff = ceil(sqrt(number))

    for num in all_numbers:
        if num > cutoff and num != 2:
            break

        if numbers_dict.get(num) != 2:
            continue

        if is_prime(num):
            numbers_dict[num] = 1

            num_not_prime = list(range(num * 2, number, num))

            for val in num_not_prime:
                numbers_dict[val] = 0

    for num in all_numbers:
        if num <= cutoff:
            continue

        if numbers_dict[num] == 0:
            continue

        numbers_dict[num] = 1

    prime = []

    for num in all_numbers:
        if numbers_dict[num] == 1:
            prime.append(num)

    return prime


def prime_dict(max):
    primes = sieve(max + 1)
    return_dict = {}

    for prime in primes:
        return_dict[prime] = True

    return return_dict

max_primes = 0
primes_dict = prime_dict(2001000)

for a in range(-1000, 1001):
    for b in range(-1000, 1001):

        def quad(n):
            return n ** 2 + a * n + b


        prime = True

        if primes_dict.get(quad(max_primes - 1)) or max_primes == 0:
            n = 0
            while prime:
                if primes_dict.get(quad(n)):
                    n += 1
                else:
                    prime = False
        else:
            continue

        if n > max_primes:
            max_primes = n
            max_ab = [a, b]

print(max_ab[0] * max_ab[1])