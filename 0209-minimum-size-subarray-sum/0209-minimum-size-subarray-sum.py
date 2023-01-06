class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # window_start = 0
        # length = float('inf')
        # running_sum = 0
        # for window_end in range(len(nums)):
        #     running_sum += nums[window_end]
        #     while running_sum >= target:
        #         length = min(length, window_end - window_start + 1)
        #         running_sum -= nums[window_start]
        #         window_start += 1
        # return length if length != float('inf') else 0
        
        
# --- revisit ----

        l = 0
        res = 0
        running_count = 0
        for r in range(len(nums)):
            running_count += nums[r]
            
            while running_count >= target:
                if r - l + 1 < res or res == 0:
                    res = r - l + 1
                running_count -= nums[l]
                l += 1
        return res
            
            
                    
            
            
        