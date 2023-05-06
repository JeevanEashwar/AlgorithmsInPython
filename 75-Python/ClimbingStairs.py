# Using recursion
def climb_stairs_using_recursion(n):
    if n <= 3:
        return n
    return climb_stairs_using_recursion(n-1) + climb_stairs_using_recursion(n-2)

# Using dynamic programming
def climb_stairs_using_dynamic_programming(n):
    if n <= 3:
        return n
    one, two = 1, 1
    for i in range(1, n):
        temp = one
        one = temp + two
        two = temp
    return one

print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
print("climb_stairs_using_recursion - 5")
print(climb_stairs_using_recursion(5))
print("##################################################")
print("climb_stairs_using_dynamic_programming - 5")
print(climb_stairs_using_dynamic_programming(5))
print("##################################################")
print("##################################################")