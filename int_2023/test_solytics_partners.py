print("hello world...")

# [3:42 PM] Priyanshu Kumar Singh
data = [("ram", 22), ("shyam", 40), ("mohan", 90), ("ram", 50), ("shyam", 10), ("raghu", 80), ("ram", 20)]

# find the highest paid doner from list

def highest_done(llist):

    result = {}
    max = 0
    max_key = ''
    for i in llist:
        key_value = i[0]

        if key_value in result.keys():
            result[i[0]] = result[i[0]] + i[1]
            if result[i[0]] > max:
                max = result[i[0]]
                max_key = i[0]
        else:
            result[i[0]]=i[1]

    print(max)


highest_done(data)