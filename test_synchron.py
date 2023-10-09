print("hello synchron...")


def appendNumber(newarr):
    newarr.append(4)


arr = [1, 2, 3]

print(arr)#[1, 2, 3]

appendNumber(arr)

print(arr)#[1, 2, 3, 4]


class P:    x = 1


class C1(P):    pass
class P:
    x = 1
class C1(P):
    pass
class C2(C1):
    pass
class C3(C2):
    x = 1


print(P.x, C1.x, C2.x, C3.x)
C3.x = 2
print(P.x, C1.x, C2.x, C3.x)
C1.x = 2
print(P.x, C1.x, C2.x, C3.x)
P.x = 2
print(P.x, C1.x, C2.x, C3.x)


constrains
by
Rahul
Jadhav1
Rahul
Jadhav1
5: 42
PM

constrains

Table: emp
cols: emp_id, salary, designatio...by
Rahul
Jadhav1
Rahul
Jadhav1
5: 43
PM

Table: emp

cols: emp_id, salary, designation, doj

o / p: get
all
details
of
persona
having
3
rd
hgihest
salary

100
100
100
90
90
80
by
Rahul
Jadhav1
Rahul
Jadhav1
5: 46
PM

100

100

100

90

90

80

select *
from emp where

salary = (select...by Upendra Kumar (Guest)
5: 49
PM
Upendra
Kumar(Guest)

select *
from emp where

salary = (
    select distict(salary) as sal
from emp
    order

by
sal
desc
limit
3
offset
3)

Table: Student
Cols: roll_num, marks_obt, t...by
Rahul
Jadhav1
Rahul
Jadhav1
5: 50
PM

Table: Student

Cols: roll_num, marks_obt, total_marks, div

o / p: roll_num, percentage

conn < - active
connection

conn < - active
connection
query = 'select... by Upendra Kumar (Guest)
6: 00
PM
Upendra
Kumar(Guest)

conn < - active
connection

query = 'select * from Student'

result = conn.execute(query)

df = pd.DataFrame(jsonify(result))

df['percentage'] = df[df['marks_obt]/df['
total_marks
']].multiply(100)