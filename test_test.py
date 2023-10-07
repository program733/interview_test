print('test')

'''

2 digits

3 small or capital char 

3 again shld be digits
'''

import re
def check_str(temp_str):

    pattern = "{2,}[0-9][a-zA_Z]{3,}[0-9]"

    if re.match(pattern.temp_str):
        return True
    else:
        return False

check_str('23kapr123')

#Explain the purpose of the if __name__ == "__main__": block in Python scripts.
#
#
# employee
# find firstname which have
#
# select firstname from eployee where firstname in 'A*A%'
#
# a,b = 0,1
# a = b
# b = a+b



