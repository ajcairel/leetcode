class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = {}
        
        start = 0
        longest = 0
        
        for index, char in enumerate(s):
            if char in chars and start <= chars[char]:
                start = chars[char] + 1
            else:
                longest = max(longest, index - start + 1)
            chars[char] = index
                
        return longest
        
       
     
       
   
        
        
      
        
     
        
     