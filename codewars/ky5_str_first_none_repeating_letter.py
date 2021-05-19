# First non-repeating character

# Write a function named first_non_repeating_letter that takes a string input, 
# and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't',
#  since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character,
#  but the function should return the correct case for the
#  initial letter. For example, the input 'sTreSS' should return 'T'.


# doesn't work for capital letters
# def first_non_repeating_letter(input_str):
#     let_list = []
#     for let in input_str:
#         if let not in let_list:
#             let_list.append(let)
#         else:
#             val_index = let_list.index(let)
#             let_list.pop(val_index)
#     if len(let_list):
#         return let_list[0]
#     return ""


def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""

# def first_non_repeating_letter(string):
#     singles = [i for i in string if string.lower().count(i.lower()) == 1]
#     return singles[0] if singles else ''

# first_non_repeating_letter('a') # 'a'
# first_non_repeating_letter('moonmen') # 'e'
# first_non_repeating_letter('stress') # 't'
first_non_repeating_letter('moonmen') # 'e'