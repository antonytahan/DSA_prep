class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        # ##O(n) approach
        # seen = {}
        # l = 0
        # res = 0 
        # for r in range(len(s)):
        #     if s[r] not in seen:
        #         res = max(res, r - l + 1)
        #         seen[s[r]] = r
        #     else:
        #         if seen[s[r]] < l:
        #             res = max(res, r - l + 1)
        #         else:
        #             l = seen[s[r]] + 1
        #         seen[s[r]] = r
        # return res

        
        # #O(2n) approach:
        # l = 0
        # res = 0
        # charSet = set()
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res
            
            
            

##--------revisit ------------



        #initialize left pointer, set
        #for every char not in set, add it, also increment a counter
        #when we encounter a seen char, res = max(res, counter), and 
        #keep removing char at l index, decrease count from set until this char can be added
        
#         seen = set()
#         res = 0
#         left = 0
#         count = 0
#         for index in range(len(s)):
            
#             if s[index] in seen:
#                 while s[index] in seen:
#                     seen.remove(s[left])
#                     left += 1
#                     count -= 1
                    
#             if s[index] not in seen:
#                 seen.add(s[index])
#                 count += 1
#                 res = max(res, count)
                
#         return res




        seen = set()
        window_start = 0
        length = 0
        for window_end in range(len(s)):
            while s[window_end] in seen:
                seen.remove(s[window_start])
                window_start += 1
            seen.add(s[window_end])
            length = max(length, window_end - window_start + 1)
        return length
            
            
                
            
        