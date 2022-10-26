class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        length = float('inf')
        running_sum = 0
        for window_end in range(len(nums)):
            running_sum += nums[window_end]
            if running_sum >= target:
                while running_sum >= target:
                    length = min(length, window_end - window_start + 1)
                    running_sum -= nums[window_start]
                    window_start += 1
        return length if length != float('inf') else 0
                    
            
            
        