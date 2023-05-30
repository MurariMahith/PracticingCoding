class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        pal = 0
        while True:
            if num >0:
                pal = pal * 10 + num%10
                num = num // 10
            else:
                break
        return x == pal
# Beats Runtime: 18.35% Memory: 14.31%