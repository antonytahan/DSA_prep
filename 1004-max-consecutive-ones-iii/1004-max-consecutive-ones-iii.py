class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        maxOnes = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                maxOnes += 1
            
            while (r - l + 1) - maxOnes > k:
                if nums[l] == 1:
                    maxOnes -= 1
                l += 1
        
            res = max(res, r - l + 1)
        return res





