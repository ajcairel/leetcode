class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return Counter(s) == Counter(t) 
        # return sorted(s) == sorted(t)
        
        # counter = {}
        
        # if len(s) != len(t):
        #     return False
        
#         for char in s:
#             if char not in counter:
#                 counter[char] = 1
#             else:
#                 counter[char] += 1
        
#         for char in t:
#             if char in counter:
#                 counter[char] -= 1
#             else:
#                 return False
            
#         for val in counter.values():
#             if val != 0:
#                 return False
        
#         return True

        countS, countT = {}, {} 
    
        if len(s) != len(t):
            return False
    
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        
        return True
    
    # O(s + t)
            
            
        
                 

      