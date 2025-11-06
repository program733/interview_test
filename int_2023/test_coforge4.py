print('test_coforge...')

'''
list of dictionaries, 
dic = {
sort based on name's 2nd last character
'''

tlist = [{'name':'upendra','last':'kumar'},{'name':'kap','last':'hunt'}]

slist = sorted(tlist,key=lambda x:x['name'][-2])
print(slist)

select score
rank() over(oder by score desc)
from student