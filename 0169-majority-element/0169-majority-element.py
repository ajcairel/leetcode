class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        major, ans = 0, 0 
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            ans = num if count[num] > major else ans
            major = max(count[num], major)
            
        return ans
        
     
       

        

       
        
     
        