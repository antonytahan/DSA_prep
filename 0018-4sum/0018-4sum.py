class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        if (nums[i], nums[j], nums[l], nums[r]) not in seen:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            seen.add((nums[i], nums[j], nums[l], nums[r]))
                        
                        l += 1
                        r -= 1
        return res
                        
        