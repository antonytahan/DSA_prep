class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = float('inf')
        num2 = float('inf')
        for num in nums:
            if num > num2:
                return True
            elif num > num1:
                num2 = min(num2, num)
            else:
                num1 = num
        return False
            
            
            
                
            