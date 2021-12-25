def align_numbers(x, y):
    """Make sure both inputs' lengths are multiples of 2."""
    len_x = len(x)
    len_y = len(y)
    if len_x == len_y:
        leading_zeros = len_x % 2
        if leading_zeros != 0:
            x = '0'*leading_zeros + x
            y = '0'*leading_zeros + y
    else:
        if len_x > len_y:
            leading_zeros = len_x % 2
            if leading_zeros != 0:
                x = '0'*leading_zeros + x
            y = '0'*(len(x) - len_y) + y
        else:
            leading_zeros = len_y % 2
            if leading_zeros != 0:
                y = '0'*leading_zeros + y
            x = '0'*(len(y) - len_x) + x
        len_x, len_y = len(x), len(y)
    return x, y


def karatsuba(x, y):
    """Perform Karatsuba multiplication."""
    if len(x) == 1:
        return str(int(x) * int(y))
    x, y = align_numbers(x, y)
    input_length = len(x)
    midpoint = input_length // 2
    a, b = x[:midpoint], x[midpoint:]
    c, d = y[:midpoint], y[midpoint:]
    p = str(int(a) + int(b))
    q = str(int(c) + int(d))
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)
    abdc = str(int(pq) - int(ac) - int(bd))

    result = str(int(ac + '0'*input_length) +
                 int(abdc + '0'*midpoint) + int(bd))
    return result
