from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        
        :rtype Optional[ListNode]
        
        """
 
        head = temp = ListNode()
        
        while list1 and list2:
            
            if list1.val <= list2.val:    
                temp.next = ListNode(list1.val)
                list1 = list1.next
                
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
                
            temp = temp.next
            
        # rest not empty list list1 or list2 
        temp.next = list1 or list2
        return head.next

