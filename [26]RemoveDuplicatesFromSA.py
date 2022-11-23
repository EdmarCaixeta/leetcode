from typing import List

def removeDuplicates(nums: List[int]) -> int:
    repeated_indexes = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) - i):
            if(nums[i] == nums[j]):
                repeated_indexes.append(j)
    for item in repeated_indexes:
        nums.pop(item)
        print(nums)
    return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))