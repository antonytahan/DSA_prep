class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        lst = s.split()
        for i in range(len(lst) - 1, -1, -1):
            res += lst[i]
            if i is not 0:
                res += " "
        return res