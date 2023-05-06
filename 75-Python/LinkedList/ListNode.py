class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f"{self.val} -> {str(self.next)}"
        else:
            return f"{self.val}"
