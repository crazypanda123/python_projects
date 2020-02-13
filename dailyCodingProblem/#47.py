"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that 
stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 
5 dollars and sell it at 10 dollars.
"""

a = [1, 2, 6, 80, 100] 

"""
max = 0

for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
            diff = a[j] - a[i]
            if diff > max:
                max = diff
            continue

print max
"""

max = 0
min_elem = a[0]
for i in range(1, len(a)):
    diff = a[i] - min_elem
    if diff > max:
        max = diff
    if a[i] < min_elem:
        min_elem = a[i]

print (max)



