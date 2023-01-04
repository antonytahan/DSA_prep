class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word_dict = {}
        for c in s1:
            word_dict[c] = word_dict.get(c, 0) + 1
        
        matched, l = 0, 0
        for r in range(len(s2)):
            if s2[r] in word_dict:
                word_dict[s2[r]] -= 1
                if word_dict[s2[r]] == 0:
                    matched += 1
            if matched == len(word_dict):
                return True
            
            if r  - l + 1 >= len(s1):
                if s2[l] in word_dict:
                    if word_dict[s2[l]] == 0:
                        matched -= 1
                    word_dict[s2[l]] += 1
                l += 1
        return False
            


            
