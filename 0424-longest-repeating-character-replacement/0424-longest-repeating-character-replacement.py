class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
#         ##O(26n)
#         count = {}
#         res = 0
#         l = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
            
#             if (r - l + 1) - max(count.values()) > k:
#                 count[s[l]] -= 1
#                 l += 1
                
#             res = max(res, r - l + 1)
#         return res
    
    
        # #O(n) - we don't actually care ab searching for new max in dict if doesn't exceed old max
#         count = {}
#         res = 0
#         l = 0
#         maxf = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             maxf = max(maxf, count[s[r]])
#             if (r - l + 1) - maxf > k:
#                 count[s[l]] -= 1
#                 l += 1
                
#             res = max(res, r - l + 1)
#         return res
    

####------------------ reviist ----------------------------

        #if there were unlimited chars somehow, this would be O(n^2) since max(count.values) would take O(n); but 26 chars only so O(26*n)
    
#         res = 0
#         count = {}
#         start_substring = 0
        
#         for end_substring in range(len(s)):
#             count[s[end_substring]] = 1 + count.get(s[end_substring], 0)
            
#             if end_substring - start_substring + 1 - max(count.values()) > k:
#                 count[s[start_substring]] -= 1
#                 start_substring += 1
                
#             res = max(res, end_substring - start_substring + 1)
#         return res
    
    
    
        ##O(n) approach:
        
#         count = {}
#         res = 0
#         l = 0
#         maxf = 0
        
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             maxf = max(maxf, count[s[r]])
            
#             if r - l + 1 - maxf > k:
#                 count[s[l]] -= 1
#                 l += 1
#             res = max(res, r - l + 1)
#         return res



        window_start = 0
        count = {}
        res = 0
        max_freq = 0
        for window_end in range(len(s)):
            count[s[window_end]] = count.get(s[window_end], 0) + 1
            max_freq = max(max_freq, count[s[window_end]])
            if window_end - window_start + 1 - max_freq > k:
                count[s[window_start]] -= 1
                window_start += 1
            res = max(res, window_end - window_start + 1)
        return res
    
    

    
    
    
    
        
            
            
             
        
        