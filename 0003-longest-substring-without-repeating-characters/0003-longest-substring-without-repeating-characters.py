class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = {}
        
        start = 0
        maxLength = 0
        
        for index, char in enumerate(s):
            if char in chars and chars[char] >= start:
                start = chars[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
                
            chars[char] = index
        
        return maxLength
       
   
        
        
      
        
     
        
     