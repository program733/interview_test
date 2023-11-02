print('test_impetus...')

llist = [1,-1,3,4,5,-6,-6,-8,-8,9,7]
# continius sub array with highest sum

from  itertools import combinations

lenlist = len(llist)
max = 0
comb= ()

for i in range(lenlist-1):
    for j in range(lenlist-i):
        sum_sub = sum(llist[i:j])
        if sum_sub > max:
            max = sum_sub
            comb = llist[i:j]

print(comb,max)

# for i in range(1,lenlist):
#     for sub in combinations(llist,i):
#         sum_sub = sum(sub)
#         if sum_sub > max:
#             max = sum_sub
#             comb = sub
#
# print(comb,max)

#imp