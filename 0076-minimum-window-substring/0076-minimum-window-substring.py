class Solution:
    def minWindow(self, s: str, t: str) -> str:
#         if t == "":
#             return t
        
#         have_map = {}
#         need_map = {}
#         for c in t:
#             need_map[c] = 1 + need_map.get(c, 0)
        
    
#         have_count = 0
#         need_count = len(need_map)
#         res, resLen = [-1, -1], float('inf')
#         l = 0
#         for r in range(len(s)):
            
#             have_map[s[r]] = 1 + have_map.get(s[r], 0)
            
#             if s[r] in need_map and have_map[s[r]] == need_map[s[r]]:
#                 have_count += 1
                
#             while have_count == need_count:
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = r - l + 1
#                 have_map[s[l]] -= 1
#                 if s[l] in need_map and have_map[s[l]] < need_map[s[l]]:
#                     have_count -= 1
#                 l += 1
#         l, r = res
        
#         return s[l:r + 1] if resLen != float('inf') else ""









###---------------- revisit------------------

#         if not s or not t:
#             return ""
        
#         need = {}
#         have = {}
#         for char in t:
#             need[char] = need.get(char, 0) + 1
        
#         need_count = len(need)
#         have_count = 0
#         left_index = 0
#         res = [-1, -1]
#         resLen = float('inf')
        
#         for index in range(len(s)):
#             have[s[index]] = have.get(s[index], 0) + 1
#             if s[index] in need and have[s[index]] == need[s[index]]:
#                 have_count += 1
            
#             while have_count == need_count:
#                 if (index - left_index + 1) < resLen:
#                     res = [left_index, index + 1]
#                     resLen = index - left_index + 1
#                 have[s[left_index]] -= 1
#                 if s[left_index] in need and have[s[left_index]] < need[s[left_index]]:
#                     have_count -= 1
#                 left_index += 1
#         return s[res[0]: res[1]] if resLen != float('inf') else ""
                
            
# ------ Revisit -----------


        word_dict = {}
        l = 0
        matched = 0
        res = ""
        for letter in t:
            word_dict[letter] = word_dict.get(letter, 0) + 1
        
        for r in range(len(s)):
            if s[r] in word_dict:
                word_dict[s[r]] -= 1
                if word_dict[s[r]] == 0:
                    matched += 1
                    
            while matched == len(word_dict):
                if r - l + 1 < len(res) or res == "":
                    res = s[l : r + 1]
                    
                if s[l] in word_dict:
                    if word_dict[s[l]] == 0:
                        matched -= 1
                    word_dict[s[l]] += 1
                l += 1
        return res
    

    
                        
            
                
                
                
                
            