class Solution:
    def isValid(self, s: str) -> bool:
        
        parens = {'(': ')', '{':'}', '[':']'}
        stack = []
        
        for thing in s:
            if thing in parens:
                stack.append(thing)
            elif len(stack) == 0 or parens[stack.pop()] != thing:
                return False
            
        return len(stack) == 0 
   
    
	
# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket
        
        