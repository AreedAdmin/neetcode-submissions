# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        #find middle of a linked list using floyds algorithm
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        slow.next=None    

        #Then starting from second half reverse the list
        prev=None
        while curr is not None:
            next_node=curr.next
            curr.next = prev
            prev = curr
            curr=next_node

        #then in place msort the second list to the first by swapping out the values

        #now we have head which is head of first half and prev which is head of second half of linked lists
        #we msut then merge them
        first=head
        second=prev
        while second is not None:
    
            tmp=first.next
            first.next=second
            first=second
            second=tmp

        return second
        