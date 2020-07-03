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

def dec_bin(x):
    return int(bin(x)[2:])

palindrome = []
for i in range(1000000):
    bin_i = dec_bin(i)

    if is_palindrome(i) and is_palindrome(bin_i):
        palindrome.append(i)

print(sum(palindrome))