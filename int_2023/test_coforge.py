print('test_coforge...')
'''
a web application that allows users to create and view a list of to-do items
'''
#
#
# template => index.html
#
# index.html = div module contains all the to do items, can have two buttons (add and show)
#             script tag or index.js file to create functionlity to add and show buttons
#             index.css file to make ui good .
#
# flask app.py
#
# app = Flask()
#
# list_to_do_item = []
#
# @app.route("/")
# def land_home_page():
#     return list_to_do_item
# @app.route('/add-to-do/<to_do_item>', methods=['post'])
# def add_to_do_items(to_do_item):
#     list_to_do_item.append(to_do_item)
#     return "Item added to to do list"
#
# app.run(host = host, port = port)


"""
file one.csv  =  1,2,3,4
file two.csv  =  2,3,4,6

output 1 : 1,6
output 2 : 2,3,4

not to use any pandas library
"""

file1 = 'file1.txt'
file2 = 'file2.txt'

with open(file1,'r') as file:
 data1 = file.read()

with open(file2,'r') as file2:
 data2 = file2.read()

common_element = set(data1).intersection(set(data2))
non_common_element = []
for i,j in zip(data1,data2):
 if i not in data2:
     non_common_element.append(i)
 if j not in data1:
     non_common_element.append(j)
print(common_element)
print(non_common_element)
