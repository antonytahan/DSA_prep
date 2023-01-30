class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target - nums[i]:
                    count += r - l 
                    l += 1
                else:
                    r -= 1
        return count
            
        