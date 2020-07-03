from math import ceil, sqrt


def fact(no):
    if no == 0 or no == 1:
        return 1

    numbers = list(range(2, no + 1))

    i = 1
    for number in numbers:
        i = i * number

    return i


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


primes_dict = prime_dict(1000000)


def get_numbers(no):
    number = []
    for i in range(len(str(no))):
        number.append(int(str(no)[i]))

    return number


def get_rotations(no):
    numbers = get_numbers(no)

    rotations = []
    for k in range(len(numbers)):
        rotations.append(numbers[k:]+numbers[:k])

    rotation_nos = []
    for r_list in rotations:
        no_rot = ''
        for n in r_list:
            no_rot += str(n)

        rotation_nos.append(int(no_rot))

    return list(set(rotation_nos))

circular = []
for i in range(1000000):
    valid = True
    numbers = get_numbers(i)

    if i != 2:
        for j in [0, 2, 4, 6, 8]:
            if j in numbers:
                valid = False
                break

    if not valid:
        continue

    if primes_dict.get(i):
        rotations = get_rotations(i)
        for rotation in rotations:
            if not primes_dict.get(rotation):
                valid = False
                if i == 193939:
                    print(rotation, valid)
                break
    else:
        continue

    if valid:
        circular.append(i)

print(len(circular))