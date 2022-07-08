class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = []
        
        for c in s:
            if c not in hash:
                hash.append(c)
            else:
                hash.remove(c)
      
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)