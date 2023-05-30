class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if(nums.count(i) == 1):
                return i
# Beats Runtime: 5.70% Memory: 18.80%