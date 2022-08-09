class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        newX = str(x)
        
        print(newX[0])
        
        start = 0
        end = len(newX) - 1
        
        while start < end:
            if newX[start] != newX[end]:
                return False
            start += 1
            end -= 1
        
        return True
        