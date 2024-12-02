f = open("2_2.txt", "r")
def checks(nums):
    sortedForward = all([nums[i] < nums[i + 1] for i in range(len(nums) - 1)])
    sortedBackward = all([nums[i] > nums[i + 1] for i in range(len(nums) - 1)])
    maxDiff = all([abs(nums[i] - nums[i + 1]) <= 3 for i in range(len(nums) - 1)])
    return (sortedForward | sortedBackward) & maxDiff

def isSafe(text):
    nums = [int(num) for num in text.split()]
    if checks(nums):
        return True
    else: 
        for index in range(len(nums)):
            numst = nums.copy()
            del numst[index]
            if checks(numst):
                return True
    return False

print(sum(isSafe(line) for line in f.readlines()))