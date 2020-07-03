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


primes = sorted(sieve(50000), reverse=True)
primes_1m = sieve(1000000)
found = False
i = 22

while not found:
    valid = False
    j = 0

    while not valid:
        if i + j > len(primes):
            break

        if sum(primes[j:i + j]) < 1000000:
            if sum(primes[j:i + j]) in primes_1m:
                recent_prime = sum(primes[j:i + j])
            print(i, primes[j:i + j])
            valid = True
            break
        else:
            j += 1

    if valid:
        i += 1
    else:
        print(i,recent_prime)
        found = True