class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Init array with 1's for every number in nums
        ans = [1 for _ in nums]
      
        
        #Two Pointers
        left = 1
        right = 1
      
        
        #loop over nums array
        #[~i] takes the 'other end' of i
        #goes from left to right until over
        for i in range(len(nums)):
            ans[i] *= left
            ans[~i] *= right 
            left *= nums[i]
            right *= nums[~i]
            
        return ans
      
        
    
        
    
    # Fill answer with 1's for every num in nums
    
    # Two-Pointer method
    
    