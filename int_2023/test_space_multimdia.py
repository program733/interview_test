print("Hello world...")
myuserid= 'inter_user'
mypassword= 'inter_password'
host='db4free.net'
myport= 3306
mydatabase= 'test_inter'

import mysql.connector

cnx = mysql.connector.connect(user=myuserid, password=mypassword,
                              host=host,
                              database=mydatabase)

cursor = cnx.cursor()
query_str = 'show tables'

cursor.execute(query_str)

for table_name in cursor:
   print(table_name)

# select * from student table
quer_all = """select * from student;



"""

res = cursor.execute(quer_all)
print(res)
#print(res) id, name , age,

rows = cursor.fetchall()
for row in rows:
    print(row)
# #print(cursor.execute(query_str))
#
# query_find = 'select count(age)/5*100 as d_age from student_table group by age'
# cursor.execute(query_find)
# for i in cursor:
#     print(i)
# cnx.close()