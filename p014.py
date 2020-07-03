def collatz(start):
    end = False
    seq = [start]

    while not end:
        if seq[-1] % 2 == 0:
            n = seq[-1] / 2
        else:
            n = 3 * seq[-1] + 1

        seq.append(n)

        if n == 1:
            end = True

    return len(seq)


max_size = 0
max_start = 0

for i in range(1,1000000):
    i_size = collatz(i)

    if i_size > max_size:
        max_size = i_size
        max_start = i

print(max_start)
