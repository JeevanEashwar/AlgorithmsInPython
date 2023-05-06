from typing import List
def missing_number_using_xor(input: List[int]) -> int:
    sequence = list(range(1, len(input)+1))
    result = 0
    for number in input:
        result ^= number
    for number in sequence:
        result ^= number
    return result

def missing_number_using_sum(input: List[int]) -> int:
    sequence = list(range(1, len(input)+1))
    sum_of_inputs = sum(input)
    sum_of_sequence = sum(sequence)
    return sum_of_sequence - sum_of_inputs
