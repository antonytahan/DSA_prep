class Solution:
    def validPalindrome(self, s: str) -> bool:
#         def check_palindrome(s,i,j):
#             while i < j:
#                 if s[i] != s[j]:
#                     return False
#                 i += 1
#                 j -= 1
#             return True
        
#         i = 0
#         j = len(s) - 1
#         while i < j: 
#             if s[i] != s[j]:
#                 return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
#             i += 1
#             j -= 1
#         return True

        # initialize two pointers
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.checkPalindrome(s, l + 1, r) or self.checkPalindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True
        



    def checkPalindrome(self, s: str, l: int, r: int) -> bool:
        # check palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    
    
    
        
            
            
        
                
            

        