class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insert_index = 0
        # for i in range(3):
        #     for r in range(len(nums)):
        #         if nums[r] == i:
        #             nums[insert_index], nums[r] = nums[r], nums[insert_index]
        #             insert_index += 1
        
        #dutch flag method:
        # define variables
        l, r = 0, len(nums) - 1
        pointer = 0
        # while our current pointer is less than the rightmost boundary of 2s
        while pointer <= r:
            # if our pointer is 0, swap it with the rightmost boundary of 0s
            if nums[pointer] == 0:
                nums[l], nums[pointer] = nums[pointer], nums[l]
                l += 1
                pointer += 1
            # same thing if pointer is 2
            elif nums[pointer] == 2:
                nums[r], nums[pointer] = nums[pointer], nums[r]
                r -= 1
                # don't increment pointer here because the number swapped in might be 0
                # this is not applicable for left pointer because we know if it was a 2 we would have sorted it already given that we are iterating from left to right
            else:
                pointer += 1