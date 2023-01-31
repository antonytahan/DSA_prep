class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i, j = 0, len(s) - 1
        # while i < j:
        #     while i< j and not s[i].isalnum():
        #         i += 1
        #     while i < j and not s[j].isalnum():
        #         j -= 1
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i += 1
        #     j -= 1
        # return True
    
        # filtered_chars = list(filter(lambda ch: ch.isalnum(), s))
        # lower_filtered_chars = list(map(lambda ch: ch.lower(), filtered_chars))
        # reversed_chars = lower_filtered_chars[::-1]
        # return lower_filtered_chars == reversed_chars
        
        

##--------------- revisit------------------------
        left, right = 0, len(s) - 1
        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        
        # filtered_chars = list(filter(lambda ch: ch.isalnum(), s))
        # print(filtered_chars)
        # lower_filtered_chars = list(map(lambda ch: ch.lower(), filtered_chars))
        # print(lower_filtered_chars)
        # return lower_filtered_chars[::-1] == lower_filtered_chars
            
        
        
        
        
    
    
            