# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).
# Examples

# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    word_list = text.split("-")
    formatted_sentence = " ".join(word_list)
    word_list = formatted_sentence.split("_")
    formatted_sentence = " ".join(word_list)
    word_list = formatted_sentence.split(" ")
    for i in range(len(word_list)):
        if i == 0:
            continue
        word_list[i] = word_list[i].capitalize()
    return "".join(word_list)


# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s

# title capitalize every word in a string
# "this is string example....wow!!!"; = > This Is String Example....Wow!!!

# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

# def to_camel_case(text):
#     words = text.replace('_', '-').split('-')
#     return words[0] + ''.join([x.title() for x in words[1:]])

print(to_camel_case("A-Pippi_Was-Savage"))# APippiWasSavage