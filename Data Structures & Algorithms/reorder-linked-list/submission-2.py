# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        find th emiddle of the linked list
        then once we find the middle we must in place merge
        the two halfs.

        for this we will have slow fast pointers to first
        and then perform the merge

        '''
        if not head or not head.next:
            return
        
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second = slow.next
        slow.next=None
        prev=None

        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp

        pointer1 = head
        pointer2= prev

        while pointer2 is not None:
            temp1=pointer1.next
            temp2=pointer2.next

            pointer1.next=pointer2
            pointer2.next=temp1

            pointer1=temp1
            pointer2=temp2