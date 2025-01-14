#Write a Python program to find the longest substring without repeating characters in a given string.
def longest_unique_substring(s):
    seen = {}
    start = 0
    max_length = 0
    substring = ""

    for index, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = index
        if index - start + 1 > max_length:
            max_length = index - start + 1
            substring = s[start:index + 1]
    
    return substring, max_length


string = input("Enter a string: ")
substring, length = longest_unique_substring(string)
print(f"Longest substring without repeating characters: '{substring}' with length {length}")
