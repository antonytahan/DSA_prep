class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_length = len(words[0])
        word_count = len(words)
        l = 0
        res = []
        
        word_dict = {}
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
        
        for r in range((len(s) - word_count * word_length) + 1):
            seen = {}
            for i in range(0, word_count):
                next_word_index = r + i * word_length
                word = s[next_word_index : next_word_index + word_length]
                if word not in word_dict:
                    break
                
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_dict[word]:
                    break
                
                if i + 1 == word_count:
                    res.append(r)
        return res
                    
                    
            
            
            
        