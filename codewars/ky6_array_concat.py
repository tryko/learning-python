# You are given an array(list) strarr of strings and an integer k. 
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# consecutive strings : follow one after another without an interruption

# def longest_consec(strarr, k):
#     if len(strarr) == 0 or k > len(strarr) or k <= 0:
#         return ""
#     str_arr_len = [len(x) for x in strarr]
#     arr_len_sum = []

# def longest_consec(strarr, k):
#     result = ""
    
#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index+k])
#             if len(s) > len(result):
#                 result = s
            
#     return result


# def longest_consec(a, k):
#     if len(a) == 0 or k > len(a) or k <= 0: return ''
#     res=[]
#     for n in range(len(a)-k+1):
#         for t in range(1,k):
#             a[n]+=a[n+t]
#     return max(a,key=len)


# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
