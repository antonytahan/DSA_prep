class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort() 
        # closest = float('inf')
        # res = 0
        # for i in range(len(nums) - 2):
        #     l = i + 1
        #     r = len(nums) - 1
        #     while l < r:
        #         if abs(nums[i] + nums[l] + nums[r] - target) < closest:
        #             closest = abs(nums[i] + nums[l] + nums[r] - target)
        #             res = nums[i] + nums[l] + nums[r]
        #         if nums[i] + nums[l] + nums[r] < target:
        #             l += 1
        #         elif nums[i] + nums[l] + nums[r] > target:
        #             r -= 1
        #         else:
        #             res = target
        #             break
        # return res

        #sort in order to implement two pointer appraoch
        nums.sort()
        # define variables
        closest = float('inf')
        res = 0
        # iterate over all numbers
        for i in range(len(nums)):
            # define l and r
            l, r = i + 1, len(nums) - 1
            while l < r:
                # distance condition
                if abs(nums[i] + nums[l] + nums[r] - target) < closest:
                    closest = abs(nums[i] + nums[l] + nums[r] - target)
                    res = nums[i] + nums[l] + nums[r]

                # two pointer method of shifting l and r
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    # we have hit the target, and can return
                    return nums[i] + nums[l] + nums[r]
        return res

