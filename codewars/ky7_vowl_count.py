def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# def getCount(s):
#     return sum(c in 'aeiou' for c in s)

# def getCount(inputStr):
#     num_vowels = 0
#     for char in inputStr:
#         if char in "aeiouAEIOU":
#            num_vowels = num_vowels + 1
#     return num_vowels

# def getCount(inputStr):
#     return len([x for x in inputStr if x in 'aeoiu'])