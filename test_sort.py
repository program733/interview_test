val = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
temp = sorted(val,key=lambda x:x[1])
print(temp)
# sorted_val = val.sort(key=lambda x:x[1])
# print(sorted_val)

def lower_func(func):
    def wrapper():
        res = func()
        result = res.lower()
        return result
    return wrapper

@lower_func
def print_help():
    print("Hellow world")
    return "Helloo"

print(print_help())

fruits = ["mango" if i%3==0 else "orange" for i in range(10)]
print(fruits)

num = [i for i in range(30) if i>=2 if i<=25 if i%4==0 if i%8==0]
print(num)

a = [1, 2, 3]
b = [7, 8, 9]
ans = [(x,y) for x,y in zip(a,b)]
print(ans)