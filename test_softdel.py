print('test_softdel...')

'''
write a pattern
*****
****
***
**
*

use recuservie function
'''

def print_star(num):
    for i in range(num):
        print('*',end="")
    num = num-1
    print()
    if num>=1:
        print_star(num)

print_star(5)



#
# class A:
#
#     def xyz(self):
#         print('xyz')
#
# class B:
#     def xyz(self):
#         print('bxyz')
#
# class C(A,B):
#
#     xyz()

a = 2
b = a
a = 3
print(b)











