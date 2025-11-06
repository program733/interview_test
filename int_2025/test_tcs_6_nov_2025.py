a = (1, 2, [3, 4])

a[2].append(5)

print(a)

 
Find the Middle Element in a List

lst = [1,2,3,4,5]

 
Find the largest number in a list

lst = [3, 56, 23, 89, 12, 99, 45]

 
lst = [2, 7, 11, 15, 4, 5]

target = 9

Output = 2,7,4,5

 
Flattening a List

list1 = [1, 2, ['a', None, {0}, ('b', 'abc', 0.0)], '', 'asdf']

Output = [1, 2, 'a', None, 0, 'b', 'abc', 0.0, '', 'asdf']

 
def append_to_list(value, my_list=[]):

my_list.append(value)

return my_list

print(append_to_list(1))

print(append_to_list(2))

print(append_to_list(3))
 
Counting charter from given string with using function

input - “abcabcbb”

output - {‘a’:2, ‘b’:4, ‘c’:2}

 
class Animal:

def speak(self):

return "Animal sound"

class Dog(Animal):

def speak(self):

return "Bark"

d = Dog()

print(d.speak())
 