class Solution:
    def isValid(self, s: str) -> bool:
        
        parens = {"(":")", "[":"]", "{":"}"}
        stack = []
        
        for p in s:
            if p in parens:
                stack.append(p)
            elif len(stack) == 0 or parens[stack.pop()] != p:
                return False
            
        return len(stack) == 0
                
   
    
       
        