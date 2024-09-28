
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def init_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        cur = head
        while  cur.next :
            if cur.val != cur.next.val :
                cur = cur.next
                continue
            del_node = cur.next
            cur.next = del_node.next
        return head 


head = init_linked_list([1, 1, 2])

solution = Solution()

head = solution.deleteDuplicates(head)

print_linked_list(head)






