# Approach 1 - Using Python dictionary
def containsDuplicateUsingDictionary(nums):
    occurenceBook = {}
    for num in nums:
        if num in occurenceBook:
            return True
        else:
            occurenceBook[num] = 1
    return False

# Approach 2 - Using Python set
def containsDuplicateUsingSet(nums):
    return len(set(nums)) != len(nums)

print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
print("containsDuplicateUsingDictionary - ", "[1,2,3,4,5,6,7,8]")
print(containsDuplicateUsingDictionary([1,2,3,4,5,6,7,8]))
print("##################################################")
print("canAttendMeetings - ", "[1,2,3,4,5,6,7,8]")
print(containsDuplicateUsingSet([1,2,3,4,5,7,7,8]))
print("##################################################")
print("##################################################")