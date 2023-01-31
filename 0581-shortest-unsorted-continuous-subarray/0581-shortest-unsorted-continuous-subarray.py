class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        # while in order, keep going
        while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
            low += 1
        # all in order
        if low == len(nums) - 1:
            return 0
        
        # other end -- while in order, keep going
        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1
        
        if high == 0:
            return 0
        
        # now we have low and high. Need to find the max and min of the subarray in between
        subarray_min, subarray_max = min(nums[low:high + 1]), max(nums[low:high + 1])
        
        # now lets backtrack low pointer to extend subarray if we encounter a smaller number than the current subarray min
        while low > 0 and nums[low - 1] > subarray_min:
            low -= 1
        
        
        # Let's do the same on the other end if we encounter a larger number than curr sub max
        while high < len(nums) - 1 and nums[high + 1] < subarray_max:
            high += 1
        #return size
        return high - low + 1 

            
            
        
        
                
                
        
        