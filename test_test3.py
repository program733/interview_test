print('test')
a = [1,2,3,0,0,0]
b = [2,4,6]
a[2:] = b
l = len(a)
print(a)
for i in range(l):
    for j in range(l-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

def change(x):
    x = '20'
    print(x)

val = "asdf"
print(val)
print(change(val))
print(val)

import pandas as pd

# Sample DataFrames
data1 = {
    'common_column': ['A', 'B', 'C', 'D'],
    'data1_col': [1, 2, 3, 4]
}

data2 = {
    'common_column': ['B', 'D', 'E', 'F'],
    'data2_col': [5, 6, 7, 8]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames based on the 'common_column'
merged_df = pd.merge(df1, df2)
# 'how' parameter specifies the type of merge (inner, outer, left, or right)

print(merged_df)
