class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
#         start, end = newInterval[0], newInterval[1]
#         left, right = [], []
    
#         for i in intervals:
#             if i[1] < start:
#                 left += i,
#             elif i[0] > e:
#                 right += i,
#             else:
#                 start = min(start, i[0])
#                 end = max(end, i[1])
        
#         return left + [[start, end]] + right 
    
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s, e]] + right
        