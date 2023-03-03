class Solution:
    def firstUniqChar(self, s: str) -> int:
        used = {}
        
        for char in s:
            used[char] = used.get(char, 0) + 1
            
        for i in range(len(s)):
            if used[s[i]] == 1:
                return i
            
        return -1
        