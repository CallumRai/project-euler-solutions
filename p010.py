from math import sqrt, ceil, floor


def is_prime(num):
    divisors = range(2, num)
    if num == 1:
        return False

    for i in divisors:
        if num % i == 0:
            return False

    return True


def sieve(number):
    all_numbers = list(range(1, number - 1))
    default_state = [2] * len(all_numbers)
    numbers_dict = {i: j for i, j in zip(all_numbers, default_state)}
    cutoff = floor(sqrt(number))

    for num in all_numbers:
        if num > cutoff:
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


print(sum(sieve(2000000)))
