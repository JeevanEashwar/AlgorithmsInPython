# Approach 1 - using two pointers
def two_sum_using_two_pointers(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Approach 2 - using dictionary/hashmap
def two_sum_using_dictionary(nums, target):
    number_index_book = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in number_index_book:
            return [number_index_book[difference], i]
        else:
            number_index_book[nums[i]] = i
    return []


print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
print("Two sum using two pointers -")
print(two_sum_using_two_pointers([1,2,3,4,5,6,7], 8))
print("##################################################")
print("Two sum using hashmap -")
print(two_sum_using_dictionary([1,2,3,4,5,6,7], 8))
print("##################################################")