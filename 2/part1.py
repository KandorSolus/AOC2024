f = open("2_1.txt", "r")
def isSafe(text):
    nums = [int(num) for num in text.split()]
    sortedForward = all([nums[i] < nums[i + 1] for i in range(len(nums) - 1)])
    sortedBackward = all([nums[i] > nums[i + 1] for i in range(len(nums) - 1)])
    maxDiff = all([abs(nums[i] - nums[i + 1]) <= 3 for i in range(len(nums) - 1)])
    return (sortedForward | sortedBackward) & maxDiff
print(sum(isSafe(line) for line in f.readlines()))