class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        highest_sq_i = len(nums) - 1
        while l <= r:
            print(l, r)
            left_sq = nums[l] * nums[l]
            right_sq = nums[r] * nums[r]
            if left_sq > right_sq:
                res[highest_sq_i] = left_sq
                l += 1
            else:
                res[highest_sq_i] = right_sq
                r -= 1
            highest_sq_i -= 1
        return res
        