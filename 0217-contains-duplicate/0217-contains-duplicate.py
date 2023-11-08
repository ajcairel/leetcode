class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums)) 
#         check = set(nums)
        
#         if (len(check) == len(nums)):
#             return False;
#         else:
#             return True;

        return len(nums) != len(set(nums))
        