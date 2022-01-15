"""Programming assignment 4"""


def read_data(filename):
    """Read the data into an array"""
    lines = open(filename, 'r', encoding='utf8').readlines()
    values = [int(x) for x in lines]
    return sorted(set(values))


def naive_counter(values, targets):
    """Naive solution to prob2sum"""
    visited_targets = {}
    for i in range(0, len(values)-1):
        for j in range(i+1, len(values)):
            tmp = values[i] + values[j]
            if tmp in targets and tmp not in visited_targets:
                visited_targets[tmp] = tmp
    return len(visited_targets)


def iterative_counter(values, targets):
    """Expects a sorted array"""
    min_target = min(targets)
    max_target = max(targets)
    visited_targets = {}
    i = 0
    j = len(values) - 1
    while j > i:
        current_val = values[i] + values[j]
        if current_val < min_target:
            i += 1
        elif current_val > max_target:
            j -= 1
        else:
            for k in range(j, i, -1):
                tmp = values[i] + values[k]
                if tmp < min_target:
                    break
                elif tmp not in visited_targets:
                    visited_targets[tmp] = tmp
            i += 1
    return len(visited_targets)


if __name__ == '__main__':
    values = read_data('course2/prob_2sum.txt')
    print(iterative_counter(values, range(-10000, 10001)))
