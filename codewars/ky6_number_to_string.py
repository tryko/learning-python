# Write Number in Expanded Form

# You will be given a number and you will need to return it as a string in Expanded Form. For example:

def expanded_form(num):
    print(enumerate(num))
    num_str = str(num)
    num_str_list = []
    for i in range(len(num_str)):
        if num_str[i] == "0":
            continue
        num_clean = num_str[i] + "0"* (len(num_str) - i -1)
        num_str_list.append(num_clean)
    return " + ".join(num_str_list)

# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
print(expanded_form(70304)) # Should return '70000 + 300 + 4'

