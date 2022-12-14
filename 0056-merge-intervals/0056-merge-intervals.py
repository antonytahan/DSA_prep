class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # res = []
        # intervals.sort()
        # res.append(intervals[0])
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][1] = max(intervals[i][1], res[-1][1])
        #     else:
        #         res.append(intervals[i])
        # return res
            
            
#-------revisit--------

        # intervals.sort()
        # res = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][1] = max(res[-1][1], intervals[i][1])
        #     else:
        #         res.append(intervals[i])
        # return res
        
        
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # does it start before the previous interval ends?
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
            
            
        