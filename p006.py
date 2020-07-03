nums = list(range(1, 101))
nums_squared = [i ** 2 for i in nums]

print(sum(nums_squared)-sum(nums)**2)
