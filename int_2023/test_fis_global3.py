import random

print('test_fisglobal...')


'''
different layers of https, defind https, how vm is differnt from docker, 
'''
# list of words

#sort based on length
lwords = ['apple','ball','cat','dog','egg']
lenwords = [len(i) for i in lwords]
rand = [len(random.choice(lwords)) for i in lwords]
swords = sorted(lwords,key=lambda x:len(x))
print(swords)

import pandas as pd
import random
df = pd.DataFrame(lwords,columns=['name'])

df['length']= lenwords
df['randrom'] = rand
print(df)