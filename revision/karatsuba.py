# TODO: in cases like the one in the example below, p = 11, q = 7,
# so they have different lengths.

def karatsuba_multiplication(x: int, y: int) -> int:
    if (x < 10) and (y < 10):
        return x * y
    else:
        n_x = len(str(x))
        n_y = len(str(y))
        n = max(n_x, n_y)
        if (n % 2 != 0):
            n += 1

        factor = 10**(n//2)
        a, b = x // factor, x % factor
        c, d = y // factor, y % factor
        p, q = a + b, c + d
        ac = karatsuba_multiplication(a, c)
        bd = karatsuba_multiplication(b, d)
        pq = karatsuba_multiplication(p, q)
        adbc = pq - ac - bd
        result = 10**n * ac + factor * adbc + bd
        return result
