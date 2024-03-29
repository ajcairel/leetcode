class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        start, end = newInterval[0], newInterval[1]
        
        left, right = [], []
        
        for i in intervals:
            if i[1] < start:
                left += i,
            elif i[0] > end:
                right += i,
            else:
                start = min(i[0], start)
                end = max(i[1], end)
        
        return left + [[start, end]] + right
                
        
    
        
     
        
        
        
   
                
            

   

      
   

        
        