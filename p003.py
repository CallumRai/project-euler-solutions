def is_prime(num):
    divisors = []

    for i in range(2, int(num/2)+1):
        if num % i == 0:
            divisors.append(i)

    if len(divisors) == 0:
        return True

    return False


def prime_factors(num):
    vals = []

    for i in range(2, int(num/2)+1):
        if num % i == 0:
            if is_prime(i):
                vals.append(i)
                num = num/i

                if num == 1:
                    break

    return vals


print(max(prime_factors(600851475143)))