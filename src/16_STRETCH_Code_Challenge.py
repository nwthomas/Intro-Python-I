"""
This file contains a code challenge I'd previously completed in JavaScript on CodeWars. I thought it would be
fun to try implementing it here.

Here's the link to the original Code Challenge: https://www.codewars.com/kata/55f2b110f61eb01779000053
"""


def get_sum(a, b):
    if a == b:
        return a
    total = 0
    for i in range(min(a, b), max(a, b) + 1):
        total += int(i)
    return total


print(get_sum(1, 2))  # should return 3
print(get_sum(1, 10))  # should return 55
print(get_sum(4, 4))  # should return 4
