# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]

# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]

# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]

# NOT WORKING
# import re
# def top_3_words(text):
#     res = re.findall(r"\w+", text)
#     print(res)
#     return
# ---------------------------------------------------

# import re
# from collections import Counter

# def top_3_words(text):
#     c = Counter(re.findall(r"'*[a-z][a-z|']*",  text.lower()))
#     return [w for w,_ in c.most_common(3)]

# ----------------------------------------------------

# import re
# from collections import Counter

# def top_3_words(text):
#     words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
#     top_3 = Counter(words).most_common(3)
#     return [tup[0] for tup in top_3]

# ----------------------------------------------------

from collections import Counter
import re


def top_3_words(text):
    d = re.sub(r" '+ ", " ", text.lower())
    print(d)
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]

# ----------------------------------------------------
# top_3_words("  //wont won't won't")

# WHAT I LEARNED:
# if you want to find words with ' eg(that's, won't) or words between '' ( not sure)
# you can search using re:
# 1) [a-z']*[a-z]+[a-z']
# 2) '*[a-z][a-z|']*