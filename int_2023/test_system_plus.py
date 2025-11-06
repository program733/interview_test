print("hello world...")

#sorting based on marks
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(subject_marks,key=lambda x:x[1],reverse=True)
print(sorted_list)

#generate fibonacci series

def generate_fibonacci_series():
    a, b = 0, 1
    while True:  
        yield a
        a,b= b,a+b


gen = generate_fibonacci_series()
for i in range(10):
    print(next(gen))


# show class and methods(statis , class and instatnce method)
#
# class Example:
#
#     def __init__(self):
#         pass
#     @staticmethod
#     def static_method():
#         print('this is static method')
#
#     @classmethod
#     def class_method(cls):
#         print('this is the class method')
#
#     def gen_method(self):
#         print('this is instance method')
#
# e1 = Example()
# e1.static_method()
# e1.gen_method()
# Example.class_method()


# reading a file from a static path , raise an error , if file is not there:

import os

# file_path = ""
# try:
#      if file_path != "":
#         with open(file_path,'r') as file:
#             content = file.read()
#      else:
#          raise RuntimeError("file is not there..")
#
# except Exception as e :
#     print(e)


# write a query to find student from student collection whose name is upendra

# query = {"name":"upendra"}
#
# db.col.find(query).limit(1)




