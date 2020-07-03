def is_palindrome(num):
    num = str(num)
    if len(num) % 2 == 0:
        first = num[0:int(len(num) / 2)]
        last = num[int(len(num) / 2):]
    else:
        first = num[0:int(len(num) / 2)]
        last = num[int(len(num) / 2) + 1:]

    for i in range(len(last)):
        if last[-i - 1] == first[i]:
            continue

        return False

    return True


three_digit = list(range(100, 1000))
pal_products = []

for num1 in three_digit:
    for num2 in three_digit:
        if is_palindrome(num1 * num2):
            pal_products.append(num1 * num2)

print(max(pal_products))
