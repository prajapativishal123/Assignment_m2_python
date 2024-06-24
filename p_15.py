''' Write a Python program to count occurrences of a substring in a string'''


def count_substring(main_string, substring):
    return main_string.count(substring)
main_string = "hello world, hello universe"
substring = "hello"
print(count_substring(main_string, substring))
