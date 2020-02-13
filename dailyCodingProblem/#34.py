"""
Given a string, find the palindrome that can be made by
inserting the fewest number of characters as possible anywhere
in the word. If there is more than one palindrome of minimum
length that can be made, return the lexicographically earliest one
(the first one alphabetically).

For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount
to make a palindrome). There are seven other palindromes that can
be made from "race" by adding three letters, but "ecarace" comes
first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""


def find_mid(word):
    l1 = list(word)
    print l1
    c = 0
    for i in range(1, len(l1)):
        while i - 1 >= 0:
            if l1[i] == l1[i - 1]:
                c+=1
                if l1[i + 1] == l1[i - 2]:
                    c+=1
