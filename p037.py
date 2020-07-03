from math import ceil, sqrt


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


def get_truncs(x):
    truncs = []
    for i in range(len(str(x))):
        truncs.append(str(x)[i:])
        truncs.append(str(x)[:i])

    truncs = list(set(truncs))
    truncs.remove('')

    truncs_int = []
    for trunc in truncs:
        truncs_int.append(int(trunc))

    return truncs_int


primes_dict = prime_dict(1000000)
found = 0
x = 11
all = False
trunc_primes = []


while not all:
    print(x)
    truncs = get_truncs(x)
    trunc_prime = True

    for trunc in truncs:
        if primes_dict.get(trunc) is not True:
            trunc_prime = False
            break

    if trunc_prime:
        trunc_primes.append(x)
        found += 1

    x += 1

    if found == 11:
        break

print(sum(trunc_primes))