# ROT13 is a simple letter substitution cipher that replaces a letter with the letter
#  13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

def rot13(message):
    msg_list = []
    cap_char_A = 65
    low_char_a = 97
    for i in range(len(message)):
        ascii_char = ord(message[i])
        if ascii_char >= 65 and ascii_char <= 90:
            new_ascii = (ascii_char - cap_char_A + 13) % 26 
            msg_list.append(chr(new_ascii + cap_char_A))
        elif ascii_char >= 97 and ascii_char <= 122:
            new_ascii = (ascii_char - low_char_a + 13) % 26
            msg_list.append(chr(new_ascii + low_char_a))
        else:
            msg_list.append(message[i])
    return "".join(msg_list)


def rot13(message):
    result = ''
    for char in message:
        if char.isalpha() and char.isupper():
            result += chr((((ord(char) - 65) + 13) % 26) + 65)
        elif char.isalpha() and char.islower():
            result += chr((((ord(char) - 97) + 13) % 26) + 97)
        else:
            result += char
    return result

# import string

# trans = string.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz', 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

# def rot13(message):
#     return message.translate(trans)

# import codecs
# def rot13(message):
#     return codecs.encode(message, 'rot_13')

print(rot13("test"))
# test.assert_equals(rot13("test"),"grfg")
# test.assert_equals(rot13("Test"),"Grfg")