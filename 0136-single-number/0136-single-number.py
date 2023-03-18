class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        chars = Counter(nums)
        
        for num in nums:
            if chars[num] == 1:
                return num
        