class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            print('left: ', s[l])
            print('right:', s[r])
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True
    
    
    # Start from the beginning and end (two pointers)
    # increment the position if it is not alphamnumeric
    # if at any point they are not equal, it cannot be a
    # palindrome, so return false 
        