from itertools import permutations, combinations
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
i = 1000

while not found:
    numbers = []
    for j in range(len(str(i))):
        numbers.append(str(i)[j])

    i += 1

    perms = list(permutations(numbers))

    perm_no = []
    for perm in perms:
        x = ''
        for j in range(len(perm)):
            x += str(perm[j])

        perm_no.append(int(x))

    primes = sieve(max(perm_no) + 1)

    valid_perm = []
    for perm in perm_no:
        if perm >= 1000 and perm in primes:
            valid_perm.append(perm)

    if len(valid_perm) < 3:
        continue

    combs = list(set(list(combinations(valid_perm, r=3))))

    for comb in combs:
        if comb[2] - comb[1] == comb[1] - comb[0] and comb[2] - comb[1] != 0 and comb[0] != 1487:
            found = True
            found_comb = comb

    if found:
        x = ''
        for j in found_comb:
            x += str(j)

        print(x)