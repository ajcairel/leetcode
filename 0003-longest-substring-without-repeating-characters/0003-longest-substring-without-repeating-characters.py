class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        used = {}
        maxLength = 0
        start = 0
        
        for index, char in enumerate(s):
            # print(used)
            # print(start)
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1 )
                
            used[char] = index
            
        return maxLength
        
     
        
     