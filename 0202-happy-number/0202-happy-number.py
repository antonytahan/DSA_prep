class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.calculateSum(slow)
            fast = self.calculateSum(self.calculateSum(fast))
            if slow == fast:
                return slow == 1
    
    def calculateSum(self, num: int) -> int:
        sum_squares = 0
        while num > 0:
            digit = num % 10
            sum_squares += digit * digit
            num //= 10
        return sum_squares
            
        