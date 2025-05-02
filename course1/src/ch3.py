def brute_force_inversions(array):
    array_length = len(array)
    n_inversions = 0
    for i in range(array_length - 1):
        for j in range(i, array_length):
            if array[i] > array[j]:
                n_inversions += 1
    return n_inversions


def merge_and_count_split_inv(left, right):
    """Merge the left and right halves in a mergesort."""
    left_length = len(left)
    right_length = len(right)
    output_length = left_length + right_length
    output = [0]*output_length

    i, j, split_inv = 0, 0, 0

    for k in range(output_length):
        if i < left_length and j < right_length:
            if left[i] <= right[j]:
                output[k] = left[i]
                i += 1
            else:
                output[k] = right[j]
                j += 1
                split_inv += left_length - i
        elif i < left_length and j == right_length:
            output[k] = left[i]
            i += 1
        else:
            output[k] = right[j]
            j += 1
            split_inv += left_length - i

    return output, split_inv


def sort_and_count_inv(x):
    """Sorts a vector in O(nlogn)."""
    input_length = len(x)
    if input_length <= 1:
        return x, 0

    midpoint = input_length // 2
    left = x[:midpoint]
    right = x[midpoint:]

    sorted_left, left_inv = sort_and_count_inv(left)
    sorted_right, right_inv = sort_and_count_inv(right)

    merged, split_inv = merge_and_count_split_inv(sorted_left, sorted_right)
    return (merged, left_inv + right_inv + split_inv)
