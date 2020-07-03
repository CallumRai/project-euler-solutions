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

def is_pandigital(x):
    unique_nums = []
    for i in range(len(str(x))):
        unique_nums.append(int(str(x)[i]))

    remove = [0]
    for i in range(9 - len(str(x))):
        remove.append(9-i)

    for i in remove:
        try:
            unique_nums.remove(i)
        except ValueError:
            pass

    if len(set(unique_nums)) == len(str(x)):
        return True

    return False

primes = sorted(sieve(10000000),reverse=True)

for prime in primes:
    if is_pandigital(prime):
        print(prime)
        break