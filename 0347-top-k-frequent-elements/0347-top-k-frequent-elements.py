class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        # for n,c in count.items():
        #     freq[c].append(n)
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
        
        seen = Counter(nums)
        res_tuple = [(-val, key) for key, val in seen.items()]
        for key in seen:
            seen[key] = seen[key] * -1
        return heapq.nsmallest(k, seen.keys(), key = seen.get)             
        
            