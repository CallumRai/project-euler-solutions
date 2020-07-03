from math import floor

unit_dict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
tens_dict = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
tens_ten_dict = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}


def get_letters_tens(number):
    ten = floor(number / 10)
    if ten == 0:
        ten_letters = 0
    elif ten == 1:
        return tens_dict.get(number)
    else:
        ten_letters = tens_ten_dict.get(ten)

    unit = number - ten * 10

    if unit == 0:
        return ten_letters

    unit_letter = unit_dict.get(unit)

    return ten_letters + unit_letter


def get_letters(number):
    if number < 10:
        return unit_dict.get(number)
    if 10 <= number <= 19:
        return tens_dict.get(number)
    if 20 <= number <= 99:
        return get_letters_tens(number)
    if number == 1000:
        return 11

    hundred = floor(number / 100)
    ten_unit = number - hundred * 100

    hundred_letters = unit_dict.get(hundred)
    ten_letters = get_letters_tens(ten_unit)

    if ten_letters == 0:
        return hundred_letters + ten_letters + 7

    return hundred_letters + ten_letters + 10


cumsum = 0
for i in range(1, 1001):
    cumsum += get_letters(i)

print(cumsum)
