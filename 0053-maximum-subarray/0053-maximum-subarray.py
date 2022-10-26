class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         current_max = float('-inf')
#         max_ending = 0
        
#         for num in nums:
#             max_ending += num
#             print(current_max)
#             if current_max < max_ending:
#                 current_max = max_ending
#             print(max_ending)
#             if max_ending < 0:
#                 max_ending = 0
#         return current_max



        
#         maxSub = float('-inf')
#         current_sum = 0
        
#         for num in nums:
#             current_sum += num
#             if maxSub < current_sum:
#                 maxSub = current_sum
#             if current_sum < 0:
#                 current_sum = 0
                
#         return maxSub


        min_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > min_sum:
                min_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return min_sum
        
        