# Count the number of Duplicates

# Write a function that will return the count of distinct case-insensitive alphabetic characters
#  and numeric digits that occur more than once in the input string.
#  The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    text_lower = text.lower()
    dic = {}
    for char in text_lower:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    let_res = [ val for key,val in dic.items() if val > 1 ]
    return len(let_res)

# def duplicate_count(s):
#     return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# def duplicate_count(text):
#     seen = set()
#     dupes = set()
#     for char in text:
#         char = char.lower()
#         if char in seen:
#             dupes.add(char)
#         seen.add(char)
#     return len(dupes)

print(set("abcdeab"))
# duplicate_count("") # 0
# duplicate_count("abcde") # 0
# duplicate_count("abcdeaa") # 1
print(duplicate_count("abcdeaB")) # 2
# duplicate_count("Indivisibilities") # 2