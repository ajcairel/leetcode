class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1 for _ in nums]
        left = 1
        right = 1 
        
        for i in range(len(nums)):
            answer[i] *= left
            answer[-1-i] *= right 
            left *= nums[i]
            right *= nums[-1-i]
            
        return answer
        
        
    
    # Fill answer with 1's for every num in nums
    
    # Two-Pointer method
    
    