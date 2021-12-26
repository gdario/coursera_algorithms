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


def merge(left, right):
    """Merge the left and right halves in a mergesort."""
    left_length = len(left)
    right_length = len(right)
    output_length = left_length + right_length
    output = [0]*output_length

    i, j = 0, 0

    for k in range(output_length):
        if i < left_length and j < right_length:
            if left[i] <= right[j]:
                output[k] = left[i]
                i += 1
            else:
                output[k] = right[j]
                j += 1
        elif i < left_length and j == right_length:
            output[k] = left[i]
            i += 1
        else:
            output[k] = right[j]
            j += 1

    return output


def mergesort(x):
    """Sorts a vector in O(nlogn)."""
    input_length = len(x)
    if input_length <= 1:
        return x

    midpoint = input_length // 2
    left = x[:midpoint]
    right = x[midpoint:]

    sorted_left = mergesort(left)
    sorted_right = mergesort(right)

    merged = merge(sorted_left, sorted_right)
    return merged
