print("test_brillio")
temp_list = [1,[2,3,[4,5,6],[7,8,[9,10]]]]
#output = [1,2,3,4,5,6,7,8,9,10]
print(temp_list)
# print(len(temp_list))

result = []

def list_append(num_list):
    for i in num_list:
        if str(type(i)) == "<class 'list'>":
            list_append(i)
        else:
            result.append(i)

list_append(temp_list)
print(result)


# for i in temp_list:
#     print(type(i))
#     if str(type(i))=="<class 'int'>":
#         result.append(i)
#     else:
#         result.extend(i)
#
# print(result)

#[9:33 AM] Sunil Roshan Thukkaram

s1= "This is first sentence and it has 1 line"

s2= "This is second sentence and it has 2 line"

#output = 'this '

import re

list_val = list(s1)
print(re.search(s1,s2))
