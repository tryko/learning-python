#  letters from n to z give an error, count errors
# s="aaabbbbhaijjjm"
# error_printer(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# error_printer(s) => "8/22"


# from re import sub
# def printer_error(s):
#     return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error(s):
    error_sum = sum(1 for letter in s if ord(letter) > ord('m'))
    return  "{}/{}".format(error_sum, len(s))

print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))