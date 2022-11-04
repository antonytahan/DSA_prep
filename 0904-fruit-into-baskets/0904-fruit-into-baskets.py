class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # initialize variables and sliding window
        seen = {}
        window_start = 0
        fruits_picked = 0
        # initialize window_end as for loop iterator
        for window_end in range(len(fruits)):
            # add vals to dictionary
            seen[fruits[window_end]] = seen.get(fruits[window_end], 0) + 1
            # if we exceeded the limit, shrink window
            while len(seen) > 2:
                seen[fruits[window_start]] -= 1
                if seen[fruits[window_start]] == 0:
                    del seen[fruits[window_start]]
                # increment start of window
                window_start += 1
            # get max of self and the number of fruits in baskets within limit
            #fruits_picked = max(fruits_picked, sum(seen.values()))
            fruits_picked = max(fruits_picked, window_end - window_start + 1)

        return fruits_picked
        
        