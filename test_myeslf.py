# def power_two_no(b,p):
#     mul = 1
#     for i in range(1,p+1):
#         mul*=b
#     return mul
#     return b**p
#
# print(power_two_no(2,10))
#
# sample = "mynameiskhan"
# for i in range(len(sample)):
#     print(sample[len(sample)-1-i],end="")
#

# def big_file_gen(file_path):
#     with open(file_path,'r') as file:
#         line = file.readline()
#         for i, line in enumerate(file):
#             if i<10:
#                 yield line
#             else:
#                 break
#         yield line
# file_path = 'test_sort.py'
# for line in big_file_gen(file_path):
#     print(line)


original_list = [1, 2, 3, 4, 5, 6]

# Create a new list where even numbers are doubled, and odd numbers are squared
new_list = [x * 2 if x % 2 == 0 else x ** 2 for x in original_list]

print(new_list)

