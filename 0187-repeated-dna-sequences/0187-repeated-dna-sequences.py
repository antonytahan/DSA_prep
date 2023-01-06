class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # define variables
        # defined both as set to not add repeated substrings and O(1) lookup
        seen = set()
        res = set()
        # iterate over each letter until the last possible valid substring(10 from end)
        for l in range(len(s) - 10 + 1):
            # define end of string window size
            r = l + 10
            # if substring has been seen and not in the res set add it
            if s[l : r] in seen and s[l : r] not in res:
                res.add(s[l : r])
            # otherwise add to seen if not there
            elif s[l : r] not in seen:
                seen.add(s[l : r])
        # need to return solution in list form
        return list(res)



