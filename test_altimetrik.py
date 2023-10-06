print('hello world...')

"""
|  A|  B|  C|  D|
+---+---+---+---+
| 10| 20| 11| 20|
| 20| 11| 10| 99|
| 10| 11| 20|  1|
| 30| 12| 20| 99|
| 10| 11| 20| 20|
| 40| 13| 15|  3|
| 30|  8| 11| 99|

|  A|A_Count|  B|B_Count|  C|C_Count|  D|D_Count|
+---+-------+---+-------+---+-------+---+-------+
| 10|      3|  8|      1| 10|      1|  1|      1|
| 20|      1| 11|      3| 11|      2|  3|      1|
| 30|      2| 12|      1| 15|      1| 20|      2|
| 40|      1| 13|      1| 20|      3| 99|      3|
+---+-------+---+-------+---+-------+---+-------+
"""

import pandas as pd
df = pd.DataFrame()
cols = df.columns
result = []
for col in cols:
    col_val = df['col']
    set_val = set(col_val)
    col_val_count = {}
    for i in set_val:
        col_val_count.get(i,col_val.count(i))
    result.append(col_val_count)

print(result)