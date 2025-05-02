from collections import defaultdict
import os
import random


def generate_dataset(outfile='values.txt', seed=42, n=1000000):
    """Generate and save a sequence of random values."""
    random.seed(seed)
    values = [random.randint(-int(1e11), int(1e11)) for _ in range(n)]

    with open(outfile, 'w', encoding='utf8') as f:
        for x in values:
            f.write(str(x) + '\n')


def create_hash_table(values):
    hash_table = defaultdict(list)
    for value in values:
        hash_table[round(value / 100000)].append(value)
    return hash_table


def find_pairs(htable):
    visited_targets = {}
    visited_keys = {}
    for key in htable:
        if -key in htable and -key not in visited_keys:
            visited_keys[-key] = 1
            for x in htable[key]:
                for y in htable[-key]:
                    tmp = x + y
                    if abs(tmp) <= 10000 and tmp not in visited_targets:
                        visited_targets[tmp] = 1
    return len(visited_targets)


if __name__ == '__main__':
    FILENAME = 'prob_2sum.txt'

    with open(FILENAME, 'r', encoding='utf8') as f:
        values = f.readlines()
        values = [int(x) for x in set(values)]

    hash_table = create_hash_table(values)
    print('Element in the hash table: {}'.format(len(hash_table)))
    print(find_pairs(hash_table))
