class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         int_list = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0 :
#                 break
#             if i == 0 or nums[i - 1] != nums[i]:
#                 self.twoSum(i,nums,int_list)    
#         return int_list
            
        
#     def twoSum(self, index : int, nums : List[int], res : List[int]):
#         seen = set()
#         j = index + 1
#         while j < len(nums):
#             complement = -nums[index] - nums[j]
#             if complement in seen:
#                 res.append([nums[index], nums[j], complement])
#                 while j + 1 < len(nums) and nums[j] == nums[j + 1]:
#                     j += 1
#             seen.add(nums[j])
#             j += 1

#         res = []
#         nums.sort()
#         for i, num in enumerate(nums):
#             if num > 0:
#                 break
#             if i != 0 and num == nums[i - 1]:
#                 continue
            
#             l, r = i + 1, len(nums) - 1
            
#             while l < r:
#                 sum = num + nums[l] + nums[r]
#                 if sum > 0:
#                     r -= 1
#                 elif sum < 0:
#                     l += 1
#                 else:
#                     res.append([num, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#         return res


# ------ revisit ----------
#         nums.sort()
#         res = []
#         print(nums)
#         seen = set()
#         for i in range(len(nums)):
#             target = 0 - nums[i]
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 if nums[l] + nums[r] > target:
#                     r -= 1
#                 elif nums[l] + nums[r] < target:
#                     l += 1
#                 else:
#                     if (nums[i], nums[l], nums[r]) not in seen:
#                         res.append([nums[i], nums[l], nums[r]])
#                         seen.add((nums[i], nums[l], nums[r]))
                    
#                     l += 1
#                     r -= 1
#         return res


        nums.sort()
        seen = set()
        print(nums)
        for i in range(len(nums)):
            r = len(nums) - 1
            l = i + 1
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(seen)









                


        
        
                
        
        
        
        
        
        
        