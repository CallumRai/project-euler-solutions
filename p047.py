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


found = False
i = 646
x = 10000
primes = sieve(x)

while not found:
    numbers = list(range(i, i + 4))

    if ceil(numbers[-1] / 2) > x:
        x += 10000
        primes = sieve(x)

    primes = [i for i in primes if i <= ceil(numbers[-1] / 2)]

    factors = []
    for number in numbers:
        factor = 0
        for prime in primes:
            if number % prime == 0:
                factor += 1
            if factor > 4:
                factor = 5
                break

        factors.append(factor)

    if factors == [4] * 4:
        print(i)
        found = True
    else:
        for j in range(4):
            if factors[-(j + 1)] != 4:
                i += 4 - j
                break
