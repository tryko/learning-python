# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

import re
# def pig_it(text):        
#     word_start_pos = None
#     word_end_pos = None
#     new_text = text
#     for i in range(len(text)):
#         if text[i].isalpha():
#             if word_start_pos is None:
#                 word_start_pos = i
#             else:
#                 word_end_pos = i
#         else:
#             if word_start_pos is not None and word_end_pos is not None:
#                 new_word = text[word_start_pos+1:word_end_pos] + text[word_start_pos] + "ay"
#                 new_text = text[:word_start_pos] + new_word + text[word_end_pos:]
#                 word_start_pos = None
#                 word_end_pos = None
#                 print(new_text)
        

    
# def pig_it(text):
#     lst = text.split()
#     print(lst)
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())


# NOW THAT'S A SOLUTION
def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)
    
print(pig_it('Hello,world,Hello, a !'))