class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
            i += 1
        return insertIndex
        