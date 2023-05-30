class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        checker = ""
        for i in range(len(min(strs))):
            checker = checker + strs[0][i]
            for s in strs:
                if s[i] == checker[i]:
                    continue
                else:
                    return res
            res = checker
        return res
# Beats Runtime: 52.70% Memory: 39.50%