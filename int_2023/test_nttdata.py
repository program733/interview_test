print('ntt_data...')

def multiplexers ():
    print([lambda n1: index * n1 for index in range (5)])
    return [lambda n1: index * n1 for index in range (5)]

print ([m1(2)  for m1 in multiplexers ()])

#[5:11 PM] Kumar, Arvind17

a = [1, 2, 3]

b = [7, 8, 9]
#[(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]


# print([(i,j) for i,j in zip(a,b)])
# for i,j in zip(a,b):
#     pass
#
# res = []
# for i in a :
#     for j in b:
#         res.append((i,j))
#
# print(res)
import pandas as pd
temp_str = {"Name":['aa', 'bb', 'xx', 'uu'],"Age":[21, 16, 50, 33]}
#df = pd.DataFrame(['aa', 'bb', 'xx', 'uu'], [21, 16, 50, 33], columns = ['Name', 'Age'])
df = pd.DataFrame(temp_str)
print(df)
# return the name of the person whose age is 16> and <50 and

res = df[df['Age']>16]
res = res[res['Age']<50]
print(res)