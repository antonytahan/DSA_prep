class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res = []
        i, j = 0, 0
        # while i and j less than lengths of lists
        while i < len(firstList) and j < len(secondList):
            # intersection is max of starting and min of ending
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            # only append if start less than end
            if low <= high:
                res.append([low, high])
            # the interval with the earlier end should be moved on since no future intersections
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
            
        