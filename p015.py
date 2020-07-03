def fact(no):
    numbers = list(range(2, no + 1))

    i = 1
    for number in numbers:
        i = i * number

    return i


print(int(fact(40) / fact(20)**2))
