
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
#
# def appendNumber(newarr):
#     newarr.append(4)
#
#
# arr = [1, 2, 3]
#
# print(arr)
#
# appendNumber(arr)
#
# print(arr)
#
# a = (1,2,3)
# temp = {}
# temp[a]='this is string'
# temp[a]= 'this is tsting '
#
# temp['a']=1
# temp['a']=2
#
#
# print(temp[a])
# print(temp['a'])
#
# temp_str = 'this is value'
# print(temp_str)
# temp_str[5]='help'
# print(temp_str)
# import os
# print(os.getcwd())
# print(os.getcwdb())
#
# def gen_ex(n):
#     i = 2
#     while n>i:
#         if i%2==0:val = i
#         yield val
#         i += 1
#
# even_gen = gen_ex(10)
# for i in even_gen:
#     print(i)

# pyList = ['P', 'y', 't', 'h', 'o', 'n']
#
# pyTuple = ('P', 'y', 't', 'h', 'o', 'n')
#
# sObject = slice(3)
#
# print(pyList[sObject]) #= ['h','o','n']
#
# sObject = slice(1, 5, 2)
#
# print(pyTuple[sObject]) #= ('y','h','n')
#
#
# def outer_function():
#     global num
#     num = 20
#
#     def inner_function():
#         global num
#         num = 30
#         print('num =', num)
#
#     inner_function()
#     print('num =', num)
#
#
# num = 10
# outer_function()
# print('num =', num)

# class myiterator():
#
#     def __init__(self,start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<self.end:
#             self.start +=1
#             return (self.start)
#         else:
#             raise StopIteration
#
# myitr = myiterator(1,9)
# for item in myitr:
#     print(item)
#
# class Mylist:
#
#     def __init__(self,value):
#         self.value = value
#
#     def __add__(self, other):
#         if isinstance(other,Mylist):
#             return self.value+other.value
#
#     def __str__(self):
#         return str(self)
#
# m1 = Mylist(4)
# m2 = Mylist(6)
# m3 = Mylist(7)
# print(m1+m3)

#
# django-admin startproject myproject
# django manage.py startapp myapp
#
# # model class
# from django.db import modeles
#
# class Task(models.Model):
#
#     name = models.CharField(max_length = 20)
#     completed = models.BooleanField(default = True)
#
#     def __str__(self):
#         return self.title
#
# from rest_framework import serializers
# from .mdoels import task
#
# class TaskSerialise(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['name','completed']
#
# from .model import Task
# from .serialser import Taskserialiser
# class TaskViewset(viewsets.ModelViewSet):
#     queryset = task.objects.all()
#     serialiser_class = TaskSerialise
#
#
# url.py
# router.rigister(r'task/',TaskViewset)


from abc import ABC, abstractmethod


# Define an abstract class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):

    def __init__(self,side):
        self.side =side

    def calculate_area(self):
        return self.side*self.side

s = Square(4)
print(s.calculate_area())
