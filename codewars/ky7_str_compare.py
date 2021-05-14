def solution(string, ending):
    sub_str = string[len(string) - len(ending):]
    return sub_str == ending

# def solution(string, ending):
#     return string.endswith(ending)

# solution = str.endswith

print(solution('abcde', 'cde')) # true
print(solution('abcde', '')) # true
# 'sensei', 'i'
print(solution('sensei', 'i'))