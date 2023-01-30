class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # define variables
        product = 1
        count = 0
        l = 0
        # if product is 1 or 0, then answer must be 0 since product < k
        if k <= 1:
            return 0
        # iterate through numbers
        for r in range(len(nums)):
            # adjust new product value
            product *= nums[r]
            # if product gets too big
            while product >= k and l < len(nums):
                #shift left pointer and adjust product
                product /= nums[l]
                l += 1
            # for every new valid number we can multiply with, there are r - l + 1 new subarrays that can be created
            count += r - l + 1 
        return count
        