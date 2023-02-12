class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
#         low, high = 0, len(nums) - 1
#         # while in order, keep going
#         while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
#             low += 1
#         # all in order
#         if low == len(nums) - 1:
#             return 0
        
#         # other end -- while in order, keep going
#         while high > 0 and nums[high] >= nums[high - 1]:
#             high -= 1
        
#         if high == 0:
#             return 0
        
#         # now we have low and high. Need to find the max and min of the subarray in between
#         subarray_min, subarray_max = min(nums[low:high + 1]), max(nums[low:high + 1])
        
#         # now lets backtrack low pointer to extend subarray if we encounter a smaller number than the current subarray min
#         while low > 0 and nums[low - 1] > subarray_min:
#             low -= 1
        
        
#         # Let's do the same on the other end if we encounter a larger number than curr sub max
#         while high < len(nums) - 1 and nums[high + 1] < subarray_max:
#             high += 1
#         #return size
#         return high - low + 1 



        # define low and high variables to track first instance of decrease and increase
        low, high = 0, len(nums) - 1
        # find first instance of decrease
        while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
            low += 1

        # if we reached the end of the list, that means that the list is sorted
        if low == len(nums) - 1:
            return 0

        # same thing for high
        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1

        # I don't think we even need this - we would have returned 0 from the low check
        if high == 0:
            return 0

        # We have our low and high, but now we need to check if the subarray minimum and maximum are smaller/larger than the nonsubarray elements
        # We'd need to increase the subarray size if so
        subarray_min = min(nums[low : high + 1])
        subarray_max = max(nums[low : high + 1])
        # while our current subarray minimum is smaller than the previous elements outside the subarray we have to extend the subarray
        while low > 0 and subarray_min < nums[low - 1]:
            low -= 1
        # same thing for the other side
        while high < len(nums) - 1 and subarray_max > nums[high + 1]:
            high += 1
        # return subarray size
        return high - low + 1

            
            
        
        
                
                
        
        