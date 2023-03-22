class Solution:
    def longestPalindrome(self, s: str) -> int:


        chars = []
        
        for c in s:
            if c not in chars:
                chars.append(c)
            else:
                chars.remove(c)
        if len(chars) != 0:
            return len(s) - len(chars) + 1
        else:
            return len(s)
        
 

    
    
    
    # check every char in s
    # if it's not in hash, append it
    # if it is, remove it
    # return the length of s - length of hash + 1
    # if the hash has things in it. This would b