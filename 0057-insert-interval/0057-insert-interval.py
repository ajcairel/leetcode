class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            print('i[0]: ', i[0])
            print('i[1]: ', i[1])
            print('s: ', s)
            print('e: ', e)
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
            print('interval: ', i)
            print('left: ', left)
            print('right: ', right)
            print('s: ', s)
            print('e: ', e)
            print('-----')
        return left + [[s, e]] + right

      
   

        
        