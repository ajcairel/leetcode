class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # nums.sort()
        # return nums[len(nums)//2]
        
        major = nums[0]
        count = 0
        
        for num in nums:
            if num == major:
                count += 1
            elif count == 0:
                major = num
                count = 1
            else:
                count -= 1
        return major
        