class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(r + l)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(r * l)
                else:
                    stack.append(int(float(l) / r))
        
        return stack[0]
                    
