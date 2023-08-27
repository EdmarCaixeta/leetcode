from typing import List


def runningSum(nums: List[int]) -> List[int]:
    result = []
    carrySum = 0
    for item in nums:
        carrySum += item
        result.append(carrySum)
    return result
print(runningSum([1,2,3,4]))