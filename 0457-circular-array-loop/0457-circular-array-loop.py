class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            direction = nums[i] > 0
            slow, fast = i, i
            while True:
                slow = self.nextIndex(direction, nums, slow)
                fast = self.nextIndex(direction, nums, fast)
                if fast != -1:
                    fast = self.nextIndex(direction, nums, fast)
                
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
        return False

                
                
            
    
    
    def nextIndex(self, is_forward: bool, nums: List[int], index: int) -> int:
        direction = nums[index] > 0
        if is_forward != direction:
            return -1
        next_index = (index + nums[index]) % len(nums)
        
        if next_index == index:
            return -1
        return next_index
        
        