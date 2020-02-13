"""
Given an array of integers,
return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def mult_all(list_in):
    out = 1
    for i in list_in:
        out *= i
    return out


l1 = [1, 2, 3, 4, 5]
l2 = []
for i in l1:
    l2.append(mult_all(l1) / i)

print l2
