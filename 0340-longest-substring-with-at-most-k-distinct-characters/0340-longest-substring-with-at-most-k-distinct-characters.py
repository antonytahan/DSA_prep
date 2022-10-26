class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = {}
        window_start = 0
        length = 0
        for window_end in range(len(s)):
            seen[s[window_end]] = seen.get(s[window_end], 0) + 1
            if len(seen) <= k:
                length = max(length, window_end - window_start + 1)
            
            while len(seen) > k:
                seen[s[window_start]] -= 1
                if seen[s[window_start]] == 0:
                    del seen[s[window_start]]
                window_start += 1
        return length
                    
                
            
        