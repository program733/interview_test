print('hello world...')
temp_list = [5,5,6,6,6,3,1,8,8,2]
#output = [2,3,1]

temp_set = set(temp_list)
res = []
for i in temp_set:
    if temp_list.count(i)==1:
        res.append(i)

print(res)

import requests

body = {'id':'asdfwae23a'}
id= 'value_of_id'
api_url = 'htttps://res.api.intratech.com{}'.format(id)
header= {'username':'myname','passowrd':'abcd@123'}

res = requests.get(url=api_url,headers=header)
print(res.text)