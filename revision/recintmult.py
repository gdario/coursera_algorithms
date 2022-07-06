import math

# TODO: allow the numbers to have any length adding leading zeros.

def check_numbers(x: int, y: int) -> int:
    """Check that two numbers have the same length, which is an integer
    power of 2.
    """
    if not(isinstance(x, str) and isinstance(y, str)):
        x, y = str(x), str(y) 
    len_x = len(x)
    len_y = len(y)
    assert len_x == len_y, "The two numbers have different lengths."
    log_len = math.log2(len_x)
    assert log_len == int(log_len), "The length is not an integer power of two."


def recursive_multiplication(x, y):
    n = len(str(x))
    if n == 1:
        return x * y
    else:
        a, b = int(str(x)[: n//2]), int(str(x)[n//2 :])
        c, d = int(str(y)[: n//2]), int(str(y)[n//2 :])
        ac = recursive_multiplication(a, c)
        ad = recursive_multiplication(a, d)
        bc = recursive_multiplication(b, c)
        bd = recursive_multiplication(b, d)
        result = 10**n * ac + 10**(n/2) * (ad + bc) + bd
        return result