def reverse_bits(n: int) -> int:
    reversed_int = 0
    for i in range(32):
        lsb = (n >> i) & 1
        reversed_int = reversed_int | (lsb << (31 - i))
    return reversed_int

