class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # seen = {}
        # window_start = 0
        # length = 0
        # for window_end in range(len(s)):
        #     seen[s[window_end]] = seen.get(s[window_end], 0) + 1        
        #     while len(seen) > k:
        #         seen[s[window_start]] -= 1
        #         if seen[s[window_start]] == 0:
        #             del seen[s[window_start]]
        #         window_start += 1
        #     length = max(length, window_end - window_start + 1)
        # return length
        
        seen = {}
        windowStart = 0
        length = 0
        #loop using windowEnd:
        for windowEnd in range(len(s)):
            # add to hash map and increase counter
            seen[s[windowEnd]] = seen.get(s[windowEnd], 0) + 1
            #if we have k distinct chars, shrink length
            while len(seen) > k:
                seen[s[windowStart]] -= 1
                # delete from hash map if no more occurrences in string
                if seen[s[windowStart]] == 0:
                    del seen[s[windowStart]]
                windowStart += 1
            # update length of longest substring
            length = max(length, windowEnd - windowStart + 1)
        return length

                
            
        