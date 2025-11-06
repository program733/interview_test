print('test_ascendion...')
#
# # convert dataframe True False into 1,0
# import pandas as pd
# sample = {'a':[True,False],
#           'b':[False,True]}
#
# df = pd.DataFrame(sample)
# print(df)
#
# res = df.replace(True,1)
# res = res.replace(False,0)
# print(res)
######################################################################3

"""
list two list both are 2d list, have create data fram out of it
ex = [[1,2,3],[4,5,6]]
ex2 = [[9,8,7],[1,7,9]]
"""

import pandas as pd
ex = [[1,2,3],[4,5,6]]
ex2 = [[9,8,7],[1,7,9]]

df = pd.DataFrame(ex)
print(df)
df2 = pd.DataFrame(ex2)
print(df2)
print('111111111')
res = pd.concat([df,df2],axis=1)
print(res)
# res = df.concat(df2)
# print(res)