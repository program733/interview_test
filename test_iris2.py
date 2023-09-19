print('hello world')

# temp = {'abc',1,1.5}
# print(temp)
#
# def print_ten():
#     for i in range(10):
#         yield i
#
#
# print(print_ten())
# # for i in print_ten():
# #     print(i)
#
# max, name , score,
# df['scire'].max()
#
# df['sco']
#
# temp = [{'a':1},{'b':2,'c':3},{'d':4}]
# output = ['a','b','c','d']
#
# result = [i.keys() for i in temp]
# print(result)
#
# #[i for i in ]

# temp = [2,3,67,56,23,45,78,70,12,76,82]
#
# print(temp)
# max = 0
# second_max = 0
# for i in temp:
#     if i > max:
#         second_max = max
#         max = i
#     if i > second_max and i < max:
#         second_max = i

temp = [{'a':1},{'b':2,'c':3},{'d':4}]
output = ['a','b','c','d']

result = [key for i in temp for key in i.keys()]
print(result)




