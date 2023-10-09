
import re
strings = ["12abc123", "45XYZ789", "123abc789", "ABc123456"]
pattern = r"\d{2}[a-zA-Z]{3}\d{3}"

for string in strings:
    if re.match(pattern, string):
        print(f"String '{string}' matches the pattern.")
    else:
        print(f"String '{string}' does not match the pattern.")


"""select e1.name as emp1 , e2.name as emp2
from employee e1
left join empoyeee e2
on e1.id=e2.id
where e1.id<e2.id"""

def appendNumber(newarr):
    newarr.append(4)


arr = [1, 2, 3]

print(arr)

appendNumber(arr)

print(arr)

a = (1,2,3)
temp = {}
temp[a]='this is string'
temp[a]= 'this is tsting '

temp['a']=1
temp['a']=2


print(temp[a])
print(temp['a'])

temp_str = 'this is value'
print(temp_str)
temp_str[5]='help'
print(temp_str)
import os
print(os.getcwd())
print(os.getcwdb())

def gen_ex(n):
    i = 2
    while n>i:
        if i%2==0:val = i
        yield val
        i += 1

even_gen = gen_ex(10)
for i in even_gen:
    print(i)