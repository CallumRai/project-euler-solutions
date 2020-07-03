from math import floor


def short_divis(num, den):
    num = str(float(num)) + ('0' * 10000)
    result = ''
    remainder = 0

    for i in range(10000):
        try:
            c = int(str(int(remainder)) + str(int(num[i])))
        except ValueError:
            result += '.'

        whole = int(floor(c / den))
        result += str(whole)

        remainder = c % den

    return result


repeat_dict = {}
for i in range(2, 1001):
    num = short_divis(1, i)

    for j in range(1, 5000):
        pattern = num[-j:]
        try:
            if j > 1 and int(pattern) == 0:
                repeat_dict[i] = 0
                break
        except ValueError:
            repeat_dict[i] = 0
            break

        if num[-2 * j:-j] == pattern:
            repeat_dict[i] = j
            break

print(max(repeat_dict, key=repeat_dict.get))
