print('test_test2')

# l1= [1,2,3,4]
# l2 = [4,5,6,7]
# print(l1+l2)
# print(l1-l2)

#overide useing magic methods,


# [12:22 PM] Girish Jadhav

logs = [

"10 120 sign-in",

"13 78 sign-in",

"10 128 sign-out",

"13 98 sign-out",

"15 11 sign-out",

]

# those useid who have spend more then 5 secs
#expected_output = ["10", "13"]
print(logs)

result  = []
res = {}
ids = []
for log in logs:
    temp_log = log.split(" ")
    ids.append(temp_log[0])
    res[temp_log[0]+temp_log[2]]=temp_log[1]
print(res)
setids = set(ids)
print(ids)
for i in setids:
    try:
        key = str(i)+"sign-in"
        key2 = str(i)+"sign-out"
        diff = int(res[key2])-int(res[key])
        if diff>5:
            result.append(i)
    except Exception as e:
        print(e)

print(result)



