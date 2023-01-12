class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        #adding two checks for leetcode TLE:
        # if sum(nums[:3]) > target:
        #     return sum(nums[:3])
        # elif sum(nums[-3:]) < target:
        #     return sum(nums[-3:])
        
        closest = float('inf')
        res = 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            #while l < r:
            # changing while condition for python TLE
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < closest:
                    closest = abs(nums[i] + nums[l] + nums[r] - target)
                    res = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res = target
                    break
        return res
                        
                    