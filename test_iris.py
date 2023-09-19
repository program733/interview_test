
def change_divide_output(func):
    def inner(a,b):
        res = func(a,b)
        if res<1:
            return b
        else:
            return  res

    return inner
@change_divide_output
def divide_two_no(a,b):
    return a/b

print(divide_two_no(3,4))

