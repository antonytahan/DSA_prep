class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
#         res = []
        
#         for i in range(len(intervals)):
#             if newInterval[1] < intervals[i][0]:
#                 res.append(newInterval)
#                 return res + intervals[i:]
#             elif newInterval[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 newInterval[0] = min(newInterval[0], intervals[i][0])
#                 newInterval[1] = max(newInterval[1], intervals[i][1])
#         res.append(interval)
#         return res


        #second method, greedy:
#         index, n = 0, len(intervals)
#         res = []
#         while index < n and newInterval[0] > intervals[index][0]:
#             res.append(intervals[index])
#             index += 1
#         if not res or res[-1][1] < newInterval[0]:
#             res.append(newInterval)
#         else:
#             res[-1][1] = max(res[-1][1], newInterval[1])
        
#         while index < n:
#             if res[-1][1] < intervals[index][0]:
#                 res.append(intervals[index])
#             else:
#                 res[-1][1] = max(res[-1][1], intervals[index][1])
#             index += 1
                
#         return res
    
        #3rd method, really neat
        #Collect the intervals strictly left or right of the new interval, then merge the new one with the middle ones (if any) before inserting it between left and right ones.

        # s, e = newInterval
        # left = [i for i in intervals if i[1] < s]
        # right = [i for i in intervals if i[0] > e]
        # if left + right != intervals:
        #     s = min(s, intervals[len(left)][0])
        # #~len(right) basically returns -len(right) - 1 
        #     e = max(e, intervals[~len(right)][1])
        # return left + [[s,e]] + right
        
        
        
#-----revisit -------
    # 3 approaches:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = (min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]))
        res.append(newInterval)
        return res
        

            

            
            
        