class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # using Counter 
        
#         chars = Counter(nums)
        
#         for num in nums:
#             if chars[num] == 1:
#                 return num

# Using a dictionary 
        counts = {}
    
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        for key, val in counts.items():
            if val == 1:
                return key

            
                
        
      
# Bit manipulation 
#         xor = 0
    
#         for num in nums:
#             xor ^= num
#             print(xor)
        
#         return xor

        