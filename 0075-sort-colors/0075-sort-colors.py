class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_index = 0
        for i in range(3):
            for r in range(len(nums)):
                if nums[r] == i:
                    nums[insert_index], nums[r] = nums[r], nums[insert_index]
                    insert_index += 1            
        