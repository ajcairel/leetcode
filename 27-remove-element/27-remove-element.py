class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for num in nums:
            if num != val:
                nums[x] = num
                x += 1
        return x

    
    # return the number in place, so you only increment down the line if it is NOT the value to be removed
    # [3,2,2,3] remove: 3
    # x = 0, 3 is what is to be removed, it's at index 0
    # when you get to 2, it is not to be removed, so it takes the place of 3, at index 0. 
    # Increment x, x = 1
    # Next in line is 2, not to be removed, so it takes index 1 spot. Increment x. x = 2
    # The rest are 3's, so no more moves made, return x which is now 2