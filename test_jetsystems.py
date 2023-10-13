print('test_jetsystem...')

#example of decotator
#
# def upper_name(func):
#     def inner(name):
#         val = func(name)
#         update_val = val.upper()
#         return update_val
#     return inner
#
# @upper_name
# def print_name(name):
#     return name
#
# print(print_name('kapricon'))

def check_palindrom(str1):
    half_len = len(str1)//2
    count = 0
    for i in range(half_len):
        if str1[i] == str1[len(str1)-1-i]:
            count+=1
        else:
            return 'False'
    if count ==half_len:
        return "True"

    #
    # if str1 == str1[::-1]:
    #     print('true')
    # else:
    #     print('False')

print(check_palindrom('asdfasd'))
print(check_palindrom('abcddcba'))

