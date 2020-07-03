from math import floor


def fact(no):
    numbers = list(range(2, no + 1))

    i = 1
    for number in numbers:
        i = i * number

    return i


digits = list(range(10))
number = []
order = 1000000

order -= 1
for i in range(10):
    ix = floor(order / fact(9 - i))

    digit = digits[ix]
    digits.remove(digit)
    order -= floor(order / fact(9 - i)) * fact(9 - i)
    number.append(digit)

lex_number = ''

for num in number:
    lex_number += str(num)

print(lex_number)
