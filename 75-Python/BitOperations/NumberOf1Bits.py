# using Remainder When divided by 2
def number_of_1_bits_divided_by_2(n: int) -> int:
    count = 0
    while n != 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count
# Using bitwise '&' operator
def number_of_1_bits_using_AND_operator(n: int) -> int:
    count = 0
    while n != 0:
        n &= n - 1
        count += 1
    return count
