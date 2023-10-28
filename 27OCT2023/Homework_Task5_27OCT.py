"""
Write a Python program to count the number of strings in a list where
the string length is 2 or more and the first and last character are the same.
"""


def count_strings(my_list):
    count = 0
    for li in my_list:
        if len(li) > 1:
            if li[0] == li[-1]:
                count += 1
    return count


string_list = [
    "radar",
    "apple",
    "level",
    "banana",
    "xylophone",
    "civic",
    "elephant",
    "racecar",
    "bb",
    "b",
    "giraffe",
    "noon",
    "keyboard",
    "deified",
    "sun",
    "moon",
    "train",
    "stats",
    "book",
    "dad",
    "cloud",
    "star",
    "a"
]
print(count_strings(string_list))