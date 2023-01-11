class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # initialize a results list
        # res = [0] * len(nums)
        # # initialize two pointers
        # l, r = 0, len(nums) - 1
        # # initialize index to populate with squares
        # highest_sq_i = len(nums) - 1
        # # <= because we need to handle the last number too
        # while l <= r:
        #     left_sq = nums[l] * nums[l]
        #     right_sq = nums[r] * nums[r]
        #     # if the left larger, put that into the index and shift l
        #     if left_sq > right_sq:
        #         res[highest_sq_i] = left_sq
        #         l += 1
        #     else:
        #         # otherwise, populate with right and shift r by 1
        #         res[highest_sq_i] = right_sq
        #         r -= 1
        #     # after populate index, shift index
        #     highest_sq_i -= 1
        # return res
        
        
# --- revisit ----
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            left_sq = nums[l] * nums[l]
            right_sq = nums[r] * nums[r]
            if left_sq < right_sq:
                res.append(right_sq)
                r -= 1
            else:
                res.append(left_sq)
                l += 1
        return res[::-1]
            
        