class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f"{self.val} -> {str(self.next)}"
        else:
            return f"{self.val}"

#Using intermediate array
def reverse_linked_list_using_array(head: ListNode) -> ListNode:
    input = []
    current = head
    while current is not None:
        input.append(current.val)
        current = current.next
    new_head = ListNode(input[0], None)
    for value in input[1:]:
        new_head = ListNode(value, new_head)
    return new_head

#using swapping technique
def reverse_linked_list_using_swapping(head: ListNode) -> ListNode:
    current = head
    previous = None
    while current is not None:
        # Swap current and previous
        temp = current.next
        # Perform swapping
        current.next = previous
        previous = current
        current = temp
    return previous
