# LC1. Reverse a Linked List (Iterative + Recursive)
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    values = list(map(int, input("Enter linked list values: ").split()))
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    reversed_head = reverse_iterative(head)
    print(to_list(reversed_head))
