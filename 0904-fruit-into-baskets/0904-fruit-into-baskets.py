class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        window_start = 0
        fruits_picked = 0
        for window_end in range(len(fruits)):
            seen[fruits[window_end]] = seen.get(fruits[window_end], 0) + 1
            while len(seen) > 2:
                seen[fruits[window_start]] -= 1
                if seen[fruits[window_start]] == 0:
                    del seen[fruits[window_start]]
                window_start += 1
            fruits_picked = max(fruits_picked, sum(seen.values()))
        return fruits_picked
        
        