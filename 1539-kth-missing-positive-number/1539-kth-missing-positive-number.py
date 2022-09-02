class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr)
        
        while start < end:
            mid = (start + end) // 2
            if arr[mid] - mid - 1 < k:
                start = mid + 1
            else: 
                end = mid
                
        return end + k