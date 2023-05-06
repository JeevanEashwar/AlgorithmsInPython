import re

# Approach 1 - using single pointer
def isPalindromeUsingSinglePointer(passedInput):
    input = re.sub(r'\W+', '', passedInput)
    reversed_input = input.upper()[::-1]
    for index, character in enumerate(input.upper()):
        if character != reversed_input[index]:
            return False
    return True

# Approach 2 - using two pointers
def isPalindromeUsingTwoPointers(input):
    input_characters = input.upper()
    left = 0
    right = len(input_characters) - 1
    while left < right:
        while not input_characters[left].isalnum() and left < right:
            left += 1
        while not input_characters[right].isalnum() and left < right:
            right -= 1
        if input_characters[left] != input_characters[right]:
            return False
        left += 1
        right -= 1
    return True

print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
print("isPalindromeUsingSinglePointer - `Do geese see God?`")
print(isPalindromeUsingSinglePointer("Do geese see God?"))
print("##################################################")
print("isPalindromeUsingTwoPointers - `Mr. Owl ate my metal worm`")
print(isPalindromeUsingTwoPointers("Mr. Owl ate my metal worm"))
print("##################################################")
print("##################################################")