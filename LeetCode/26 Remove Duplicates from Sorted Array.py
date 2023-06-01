class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = len(nums)
        i = 0
        while i < c:
            if(i+1 != c and nums[i] == nums[i+1]):
                nums.remove(nums[i+1])
                c = c-1
                nums.append("_")
            else:
                i = i + 1
        return c
#Beats Runtime: 5.6% Memory: 10.54%