print('hello world...')
# import pandas as pd
# dict = {"a":[1,2,3,5],
#          "b":[6,7,8,9]}
#
# df = pd.DataFrame(dict)
# print(df)
# #rename column from a and b to 1 , 2 respectively
#
# df.columns = ['1','2']
# print(df)
# print(df.iloc(len(df)))
# df.shape()

#write a decorator to change string into uppercase

# def up_decorator(func):
#     def inner(name):
#         val = func(name)
#         result = val.upper()
#         return result
#     return inner
# @up_decorator
# def print_name(name):
#     return name
#
# print(print_name("kapricon"))


# sort of dictionary based on value:
# sort based on count

# fruit_count = {'apple':10,'banana':5,'mango':8}
# list_val = [(key,val) for key,val in fruit_count.items()]
#
# sorted_fruit_count = sorted(list_val,key=lambda list_val:list_val[1])
# print(sorted_fruit_count)
#
#
# sorted_dict = dict(sorted(fruit_count.items(), key=lambda item: item[1]))
#
# for item in fruit_count.items():
#     print(item)
# print(sorted_dict)
import os,sys
# filename = 'temp.txt'
# curr
# list_of_files = os.
# try:
#     with open(filename,)

#age of the person , if age is less >=0

class AgeException(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)+" exception occured"

def check_age(age):
    try:
        if age<=0:
            raise AgeException('provid age is less')
        else:
            print('we are good to go')
    except Exception as e:
        print(e)

print(check_age(0))