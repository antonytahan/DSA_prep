class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        res = []
        l = 0
        count = 0
        if k <= 1:
            return 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l < len(nums):
                product /= nums[l]
                l += 1
            lst = []
            # for i in range(r, l - 1, -1):
            #     count += 1
            #     lst.append(nums[i])
            #     res.append(lst)
            count += r - l + 1
        return count
        