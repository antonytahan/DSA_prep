class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        prev = lower - 1
        res = []
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1

            if curr - (prev + 1) > 1:
                res.append(str(prev + 1) + "->" + str(curr - 1))
            elif curr - (prev + 1) > 0:
                res.append(str(curr - 1))
            prev = curr
        return res
                
            
            
        

            
            
            
        