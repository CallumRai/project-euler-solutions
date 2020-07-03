from math import sqrt, ceil, floor, factorial


def is_prime(num):
    divisors = range(2, num)
    if num == 1:
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


def get_prime_factors(number):
    primes = sieve(ceil(number / 2))

    if is_prime(number):
        primes.append(number)

    prime_factors = []

    for prime in primes:
        if number % prime == 0:
            prime_factors.append(prime)

    factor_exp = []

    for factor in prime_factors:
        n = 1
        found_exp = False
        while not found_exp:
            if number % (factor ** (n + 1)) == 0:
                n += 1
            else:
                factor_exp.append(n)
                found_exp = True

    exponent_dict = {i: j for i, j in zip(prime_factors, factor_exp)}

    return exponent_dict

i = 5
found = False

while not found:
    if i == 5:
        dict1 = get_prime_factors(i)
        dict2 = get_prime_factors(i + 1)
    else:
        dict1 = dict2
        dict2 = get_prime_factors(i + 1)

    prime_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

    prime_dict[2] = prime_dict[2] - 1

    if prime_dict[2] == 0:
        del prime_dict[2]

    exponents = prime_dict.values()

    divisors = 1

    for exponent in exponents:
        divisors = divisors * (exponent + 1)

    if divisors > 500:
        print(int(i * (i + 1) / 2))
        found = True

    i += 1