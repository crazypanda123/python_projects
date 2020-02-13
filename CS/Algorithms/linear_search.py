def linear_search(arr, n, x):
    for i in range(0, n):
        if l1[i] == x:
            return i
    return -1


l1 = [10, 30, 2, 5]
x = 40
n1 = len(l1)

print (x, 'is present at index', linear_search(l1, n1, 40))
