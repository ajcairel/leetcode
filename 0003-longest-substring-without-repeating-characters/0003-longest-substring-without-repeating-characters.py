class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        maxLength = 0
        
        for i in range(len(s)):
# If s[i] not in seen, we can keep increasing the window size by moving the right pointer
            if s[i] not in seen:
                maxLength = max(maxLength, i - left + 1)
            
# There are tow cases if s[i] is seen
# 1. s[i] is inside the current window, we need to change the window by moving left pointer to seen[s[i]] + 1
# 2. s[i] is NOT inside the current window, we can keep increasing the window
            else:
                if seen[s[i]] < left:
                    maxLength = max(maxLength, i - left + 1)
                else:
                    left = seen[s[i]] + 1
            seen[s[i]] = i
        
        return maxLength
        
     