class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        left = 0 # red
        mid = 0 # white
        right = len(nums) - 1 # blue 
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
                
        
        return nums
            
                
                
        
    