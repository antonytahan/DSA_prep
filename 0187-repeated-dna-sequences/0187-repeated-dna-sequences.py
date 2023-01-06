class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen = set()
        res = set()
        for l in range(len(s) - 10 + 1):
            if s[l : l + 10] in seen and s[l : l + 10] not in res:
                res.add(s[l : l + 10])
            else:
                seen.add(s[l : l + 10])
        return list(res)
            
        
        
        