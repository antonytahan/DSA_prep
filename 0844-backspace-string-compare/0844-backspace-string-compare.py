class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         index1 = len(s) - 1
#         index2 = len(t) - 1
#         while index1 >=0 or index2 >=0:
#             next_i1 = self.get_next_char_index(s, index1)
#             next_i2 = self.get_next_char_index(t, index2)
#             if next_i1 < 0 and next_i2 < 0:
#                 return True
#             if next_i1 < 0 or next_i2 < 0:
#                 return False
#             if s[next_i1] != t[next_i2]:
#                 return False
#             index1 = next_i1 - 1
#             index2 = next_i2 - 1
#         return True
            
#     def get_next_char_index(self, string: str, index: int) -> int:
#         backspaces = 0
#         while index >= 0:
#             if string[index] == "#":
#                 backspaces += 1
#             elif backspaces > 0:
#                 backspaces -= 1
#             else:
#                 break
#             index -= 1
#         return index



    def backspaceCompare(self, s : str, t: str) -> bool:
        # initialize variables. We'll be iterating backwards
        index_s = len(s) - 1
        index_t = len(t) - 1
        # while either of them are larger than 0, keep going
        while index_s >= 0 or index_t >= 0:
            # call our function to get the indices of the next valid char for each
            next_index_s = self.nextChar(s, index_s)
            next_index_t = self.nextChar(t, index_t)
            # if both are out of bounds, it means that they match -> return True
            if next_index_s < 0 and next_index_t < 0:
                return True
            # if only one of them is out of bounds, they do not match -> return False
            elif next_index_s < 0 or next_index_t < 0:
                return False
            # if the next valid char does not match, return False
            elif s[next_index_s] != t[next_index_t]:
                return False
            # set our s and t indices to the next valid index of each - 1
            index_s = next_index_s - 1
            index_t = next_index_t - 1
        # if we successfully exit, that means strings match
        return True


    def nextChar(self, strng : str, index: int) -> int:
        # some function that tells us what the index of the next valid char is
        # to track backspaces
        backspaces = 0
        # make sure we are within range
        while index >= 0:
            # increment backspace counter
            if strng[index] == "#":
                backspaces += 1
            # decrement backspace counter if not backspace and non zero backspace count
            elif backspaces > 0:
                backspaces -= 1
            # otherwise we have our next char index
            else:
                break
            index -= 1
        return index
            
                
            
            
        