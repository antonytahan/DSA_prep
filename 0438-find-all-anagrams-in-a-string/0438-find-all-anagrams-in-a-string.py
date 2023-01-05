class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        res = []
        l = 0
        word_dict = {}
        matched = 0
        for c in p:
            word_dict[c] = word_dict.get(c, 0) + 1
        
        for r in range(len(s)):
            if s[r] in word_dict:
                word_dict[s[r]] -= 1
                if word_dict[s[r]] == 0:
                    matched += 1
            if matched == len(word_dict):
                res.append(l)
                # if word is longer than 2 chars you can skip potential anagrams between l and r
                if s[l] in word_dict:
                    if word_dict[s[l]] == 0:
                        matched -= 1
                    word_dict[s[l]] += 1
                l += 1
            if r - l + 1 >= len(p):
                if s[l] in word_dict:
                    if word_dict[s[l]] == 0:
                        matched -= 1
                    word_dict[s[l]] += 1
                l += 1
        return res
        