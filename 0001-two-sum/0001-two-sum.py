class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}
        
        for index, num in enumerate(nums):
            if num in pairs:
                return [pairs[num], index]
            else:
                pairs[target - num] = index
                
            
        
     