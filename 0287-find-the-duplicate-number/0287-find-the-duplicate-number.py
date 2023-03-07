class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stack = {}
        
        for i in range(len(nums)):
            stack[nums[i]] = stack.get(nums[i], 0) + 1
            if stack[nums[i]] == 2:
                return nums[i]
          
        