class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # time limit exceeded
        # define variables
        # running_max = 0
        # l = 0
        # res = []
        # for r in range(k - 1, len(nums)):
        #     running_max = max(nums[l : r + 1])
        #     res.append(running_max)
        #     l += 1
        # return res
    
        
#         dq = deque()
#         current_max = 0
#         res = []
        
#         for i, n in enumerate(nums):
#             print(i, dq)
#             # ensure value at the index in first element of deque is greatest in sliding window
#             while dq and nums[dq[-1]] < n:
#                 dq.popleft()
#             # append the current index to deque
#             dq.append(i)
            
#             # make sure sliding window only contains the correct window indices
#             if dq[0] == i - k :
#                 dq.popleft()
                
            
#             # populate result with max of sliding window
#             if i >= k - 1:
#                 res.append(nums[dq[0]])
#         return res


        d = deque()
        out = []
        for i, n in enumerate(nums):
            #print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
            while d and nums[d[-1]] < n:
                d.pop()
                #print("\t Popped from d because d has elements and nums[d.top] < curr element")
            d.append(i)
            #print("\t Added i to d")
            if d[0] == i - k:
                d.popleft()
                #print("\t Popped left from d because it's outside the window's leftmost (i-k)")
            if i>=k-1:
                out.append(nums[d[0]])
                #print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
        return out
            
            
        
        
            
        
        
        
        