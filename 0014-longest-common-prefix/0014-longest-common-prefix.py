class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pre = strs[0]
        
        for string in strs:
            while not string.startswith(pre):
                pre = pre[:-1]
        
        return pre 
        

        

        