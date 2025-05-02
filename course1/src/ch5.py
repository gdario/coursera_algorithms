class QuickSort:
    def __init__(self, filename):
        self.data = self.read_data(filename)
        self.len_data = len(self.data)
        self.num_comparisons = 0

    def read_data(self, filename):
        with open(filename, 'r') as f:
            data = f.read().splitlines()
        data = [int(x) for x in data]
        return data

    def choose_left_pivot(self, left, right):
        return left

    def choose_right_pivot(self, left, right):
        return right

    def choose_median_of_three_pivot(self, left, right):
        mid = left + (right - left) // 2
        if (self.data[left] < self.data[mid] < self.data[right]) or (
                self.data[right] < self.data[mid] < self.data[left]):
            return mid
        elif (self.data[mid] < self.data[right] < self.data[left]) or (
                self.data[left] < self.data[right] < self.data[mid]):
            return right
        else:
            return left

    def partition(self, left, right):
        p = self.data[left]
        i = left + 1
        for j in range(left+1, right+1):
            if self.data[j] < p:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1
        self.data[left], self.data[i-1] = self.data[i-1], self.data[left]
        return i - 1

    def quicksort(self, left, right):
        if left >= right:
            return self.data
        i = self.choose_median_of_three_pivot(left, right)
        self.data[left], self.data[i] = self.data[i], self.data[left]
        self.num_comparisons += right - left
        j = self.partition(left, right)
        self.quicksort(left, j-1)
        self.quicksort(j+1, right)


if __name__ == '__main__':
    qs = QuickSort('quicksort_data.txt')
    qs.quicksort(0, qs.len_data-1)
    print(qs.data[:10])
    print(qs.num_comparisons)
