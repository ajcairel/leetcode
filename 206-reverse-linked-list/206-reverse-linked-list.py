# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        return prev
        
        
    
        
        #1 set prev to None and the current to head
        
        #2 you are going to reverse the list until cur = None 
        
        # think 'cascade'
        
        #3 set nxt to cur.next
        #4 set cur.next to prev
        #5 set prev to cur
        #6 set cur to nxt
        
        #7 return prev 