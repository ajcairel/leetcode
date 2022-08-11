class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        print(end)
        print(s[end])
        while end > 0 and s[end] == " ":
            print('end: ', end)
            end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ":
            print('beg: ', beg)
            print(s[beg])
            beg -= 1
        print(end-beg)
        return end - beg

        
        