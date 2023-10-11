print('test')

'''

2 digits

3 small or capital char 

3 again shld be digits
'''

import re
def check_str(temp_str):

    pattern = r"^\d{2,}[0-9]"

    if re.search(pattern,temp_str):
        return True
    else:
        return False

print(check_str('2a333kapr123'))

#Explain the purpose of the if __name__ == "__main__": block in Python scripts.
#
#
# employee
# find firstname which have
#
# select firstname from eployee where firstname like 'A*A%'
#
# a,b = 0,1
# a = b
# b = a+b

#
a = (1,2,3)
b = a
a += 4,
print(type(a))
print(a==b)
c =(1,2,3,6)

# a = [1,2]
# b=a
# b= b+3
# print(a)
# print(a==b)
