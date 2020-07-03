def is_prime(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True


found = False
num = 2
primes = []

while not found:
    if is_prime(num):
        primes.append(num)

    num += 1

    if len(primes) == 10001:
        found = True

print(max(primes))
