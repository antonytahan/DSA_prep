class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # sort in order to implement a two pointer approach
        nums.sort()
        # define variables
        count = 0
        # loop through all possible first numbers
        for i in range(len(nums) - 2):
            # define l and r pointers
            l, r = i + 1, len(nums) - 1
            # two pointer approach
            while l < r:
                # if triplet is smaller than target
                if nums[i] + nums[l] + nums[r] < target:
                    # add r - l to count since last of the triplet can be r or any number between l and r since r is the biggest
                    count += r - l
                    # increment l after adjusting count
                    l += 1
                else:
                    # else r is too big, shrink r
                    r -= 1
        return count
            
        