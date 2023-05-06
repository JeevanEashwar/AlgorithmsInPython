class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        top_divider = "----Top----\n"
        bottom_divider = "----Bottom----"
        stack_elements = ""
        for element in self.items:
            stack_elements = f"{element}\n" + stack_elements
        return top_divider + stack_elements + bottom_divider
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)  # prints ----Top----\n3\n2\n1\n----Bottom----
s.pop()
print(s) # prints ----Top----\n2\n1\n----Bottom----
print("Top most element is", s.peek())  # prints 2
