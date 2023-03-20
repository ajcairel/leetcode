class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
#         chars = Counter(nums)
        
#         for num in nums:
#             if chars[num] == 1:
#                 return num
#         counts = {}
    
#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1
        
#         for n in counts:
#             if counts[n] == 1:
#                 return n
        xor = 0
    
        for num in nums:
            xor ^= num
        
        return xor
        