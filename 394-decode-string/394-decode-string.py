class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0 
        curString = ''
        for char in s:
            print ('char: ', char)
            if char == '[':
                stack.append(curString)
                stack.append(curNum)
                print('It is [')
                print('stack: ', stack)
                print('-----')
                curString = ''
                curNum = 0
            elif char == ']':
                print('It is ]')
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
                print('num: ', num)
                print('prevString: ', prevString)
                print('curString: ', curString)
                print('-----')
            elif char.isdigit():
                curNum = curNum*10 + int(char)
                print ('It is a digit')
                print('curNum: ', curNum)
                print('-----')
            else:
                curString += char
                print('It is a letter')
                print('curString: ', curString)
                print('-----')
        return curString