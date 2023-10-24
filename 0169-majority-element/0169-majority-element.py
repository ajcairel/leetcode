class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        ans, major = 0, 0 
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            ans = n if count[n] > major else ans
            major = max(count[n], major)
            
        return ans
        
   
       

        

       
        
     
        