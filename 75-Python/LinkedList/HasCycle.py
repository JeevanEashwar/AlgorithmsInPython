class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.val) + '->' + str(self.next)
        else:
            return str(self.val)


def hasCycle(head: ListNode[int]) -> bool:
    visitor_book = []
    pointer = head
    cycle_found = False
    while pointer and not cycle_found:
        cycle_found = any(visitor_node is pointer for visitor_node in visitor_book)
        visitor_book.append(pointer)
        pointer = pointer.next
    return cycle_found


def hasCycleUsingFloydsTechnique(head: ListNode[int]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

