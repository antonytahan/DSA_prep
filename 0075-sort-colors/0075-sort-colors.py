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
        l, r = 0, len(nums) - 1
        curr = 0
        while curr <= r:
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1        