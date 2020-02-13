"""The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

For example, given the set [1, 2, 3, 4],
it should return [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], 
[1, 3, 4], [2, 3, 4], [1, 2, 3, 4]].

You may also use a list or array to represent a set.
"""
import math

a = [1, 2, 3, 4]

def power_set(a):
    len_set = len(a)
    len_pset = int(math.pow(2, len_set))
    pset = []

    for i in range(0, len_pset):
        subset = []
        for j in range(0, len_set):
            if (i & (1 << j)) > 0:
                subset.append(a[j])
        pset.append(subset)
    return pset

print power_set(a)



