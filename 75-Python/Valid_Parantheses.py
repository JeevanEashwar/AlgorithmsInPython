def valid_parentheses(s: str) -> bool:
    # Dictionary to store open close parentheses combinations
    open_close = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    # Stack
    stack = []
    
    for char in s:
        if char in open_close:
            # If the stack is empty
            if not stack:
                # Input cannot start with closing parentheses
                return False
            else:
                top_char_in_stack = stack[-1]
                if top_char_in_stack == open_close[char]:
                    stack.pop()
                else:
                    return False
        else:
            stack.append(char)

    return not stack







print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")

print(valid_parentheses("{}{}([])"))

print("##################################################")
print("##################################################")
