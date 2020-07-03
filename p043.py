from itertools import permutations
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


numbers = sorted(permutations(list(range(10))), reverse=True)
primes = sieve(18)

pan_numbers = []
for x in numbers:
    if x[0] == 0:
        continue

    no = ''
    for i in x:
        no += str(i)

    pan_numbers.append(int(no))

cumsum = 0
for x in pan_numbers:
    valid = True
    for i in range(7):
        if 4+i > len(str(x))-1:
            if int(str(x)[1 + i:][0:3]) % primes[i] != 0:
                valid = False
                break
        else:
            if int(str(x)[1 + i:4 + i]) % primes[i] != 0:
                valid = False
                break

    if valid:
        cumsum += x

print(cumsum)
