class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    lst.append(i)
                    lst.append(j)
                    return lst
        return lst
# Beats Runtime: 24.44% Memory: 36.60%