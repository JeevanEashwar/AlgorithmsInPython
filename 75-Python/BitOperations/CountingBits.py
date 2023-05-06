from typing import List
def number_of_1_bits_using_AND_operator(n: int) -> int:
    count = 0
    input_ = n
    while input_ != 0:
        input_ = input_ & (input_ - 1)
        count += 1
    return count

def counting_bits_brute_force(n: int) -> List[int]:
    result = []
    for i in range(n+1):
        result.append(number_of_1_bits_using_AND_operator(i))
    return result

def number_of_bits_using_cache(n: int) -> List[int]:
    """
    result[n] = result[n/2], if n is even number
    result[n] = result[n/2] + 1, if n is odd number
    """
    result = [0, 1]
    if n < 2:
        return result[:n+1]
    for i in range(2, n+1):
        if i % 2 == 0:
            result.append(result[i//2])
        else:
            result.append(result[i//2] + 1)
    return result
