s = "tonystark is the iron man"
print(s)
temp_l = list(s)
#print(temp_l)
set_s = set(temp_l)
#print(set_s)
ans_d = {}
for i in set_s:
    ans_d[i]=temp_l.count(i)
    #print("count",temp_l.count(i))

print(ans_d)
