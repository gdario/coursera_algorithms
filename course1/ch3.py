def brute_force_inversions(array):
    array_length = len(array)
    n_inversions = 0
    for i in range(array_length - 1):
        for j in range(i, array_length):
            if array[i] > array[j]:
                n_inversions += 1
    return n_inversions
