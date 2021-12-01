f = open("input")
nums = list(map(int, f.read().splitlines()))

sums = list(map(lambda x: sum(x), zip(nums, nums[1:], nums[2:])))
numIncrease = sum(map(lambda x: x[1] > x[0], zip(sums, sums[1:])))
print(numIncrease)