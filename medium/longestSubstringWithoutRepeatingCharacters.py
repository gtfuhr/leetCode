class Solution:
    
    def repeat_characters(self, s: str) -> bool:
        for i, char_i in enumerate(s):
            for j, char_j in enumerate(s):
                if i != j and char_i == char_j:
                    return True
                
        return False
                    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = ''
        actual_string = ''
        len_s = len(s)
        
        for i, char in enumerate(s):
            actual_string += char
            
            if (i+1 < len_s):
                if actual_string not in s[i+1:] and not self.repeat_characters(actual_string):
                    longest_string = actual_string
                else:
                    actual_string = ''
    
        return len(longest_string)
            
        
