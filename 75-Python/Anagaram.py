# Approach 1 - Using Dictionaries / Hashmaps
def anagram_check_using_dictionaries(one: str, two: str) -> bool:
    if len(one) != len(two):
        return False
    occurence_book1 = {}
    occurence_book2 = {}
    for character in one:
        occurence_book1[character] = occurence_book1.get(character, 0) + 1
    for character in two:
        occurence_book2[character] = occurence_book2.get(character, 0) + 1
    for character in one:
        if occurence_book1[character] != occurence_book2.get(character, 0):
            return False
    return True

# Approach 2 - using sorting
def anagram_check_using_sorting(one: str, two: str) -> bool:
    sorted_one = sorted(one)
    sorted_two = sorted(two)
    if len(one) != len(two):
        return False
    for i in range(len(one)):
        if sorted_one[i] != sorted_two[i]:
            return False
    return True

# Approach 3 - using a single line
def check_anagram_single_line(one: str, two: str) -> bool:
    return sorted(one) == sorted(two)


print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
print("Input - ","ravi", "vari")
print("##################################################")
print("anagram_check_using_dictionaries -")
print(anagram_check_using_dictionaries("ravi", "vari"))
print("##################################################")
print("anagram_check_using_sorting -")
print(anagram_check_using_sorting("ravi", "vari"))
print("##################################################")
print("check_anagram_single_line -")
print(check_anagram_single_line("ravi", "vari"))
print("##################################################")
