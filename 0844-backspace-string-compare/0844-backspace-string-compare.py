class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        index1 = len(s) - 1
        index2 = len(t) - 1
        while index1 >=0 or index2 >=0:
            next_i1 = self.get_next_char_index(s, index1)
            next_i2 = self.get_next_char_index(t, index2)
            if next_i1 < 0 and next_i2 < 0:
                return True
            if next_i1 < 0 or next_i2 < 0:
                return False
            if s[next_i1] != t[next_i2]:
                return False
            index1 = next_i1 - 1
            index2 = next_i2 - 1
        return True
            
    def get_next_char_index(self, string: str, index: int) -> int:
        backspaces = 0
        while index >= 0:
            if string[index] == "#":
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                break
            index -= 1
        return index
            
                
            
            
        