class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         res = []
#         seen = set()
#         for i in range(len(nums) - 3):
#             for j in range(i + 1, len(nums) - 2):
#                 l, r = j + 1, len(nums) - 1
#                 while l < r:
#                     if nums[i] + nums[j] + nums[l] + nums[r] < target:
#                         l += 1
#                     elif nums[i] + nums[j] + nums[l] + nums[r] > target:
#                         r -= 1
#                     else:
#                         if (nums[i], nums[j], nums[l], nums[r]) not in seen:
#                             res.append([nums[i], nums[j], nums[l], nums[r]])
#                             seen.add((nums[i], nums[j], nums[l], nums[r]))
                        
#                         l += 1
#                         r -= 1
#         return res


# ----- Revisit ---
        #start by sorting in order to implement two pointer solution
        nums.sort()
        # initialize variables needed
        res = []
        seen = set()
        # to implement two pointer, we need to iterate over the other two numbers
        # go up until the last possible 4sum
        for i in range(len(nums) - 3):
            # go from first number + 1 up until the last possible 3sum
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                # now implement two pointer approach
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        # make sure that we have not already seen this combo
                        if (nums[i], nums[j], nums[l], nums[r]) not in seen:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            seen.add((nums[i], nums[j], nums[l], nums[r]))
                        # regardless if seen or not, we need to move pointers
                        l += 1
                        r -= 1
        return res
                        
        