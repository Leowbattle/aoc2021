f = open("input")
nums = list(map(int, f.read().splitlines()))

numIncrease = sum(map(lambda x: x[1] > x[0], zip(nums, nums[1:])))
print(numIncrease)