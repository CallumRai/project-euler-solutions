from math import floor

all_coins = [200, 100, 50, 20, 10, 5, 2, 1]

a = 0


def update_a():
    global a
    a += 1
    return a


def recurse(coins, goal):
    if goal == 0:
        update_a()
    elif len(coins) != 1:
        max_coin = floor(goal / coins[0])

        for i in range(0, max_coin + 1):
            remaining = goal - coins[0] * i
            recurse(coins[1:], remaining)

    else:
        update_a()


recurse(all_coins, 200)
print(a)