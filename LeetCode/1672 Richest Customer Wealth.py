# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         maxWealth = 0
#         for i in accounts:
#             maxWealth = max(maxWealth, sum(i))
#         return maxWealth
x = 13432
num = 13432
pal = 0
while True:
    if num >0:
        pal = pal * 10 + num%10
        num = num//10
        print(num)
    else:
        break
if pal == x:
    print("pal")
else:
    print("not pal")
# Beats Runtime: 51.25% Memory: 7.72%