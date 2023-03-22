class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        ans, majorCount = 0, 0
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            ans = n if count[n] > majorCount else ans
            majorCount = max(majorCount, count[n])
            
        return ans
        
        # nums.sort()
        # return nums[len(nums)//2]
        
#         major = nums[0]
#         count = 0
        
#         for num in nums:
#             if num == major:
#                 count += 1
#             elif count == 0:
#                 major = num
#             else:
#                 count -= 1
        
#         return major


        

       

        

       
        
     
        