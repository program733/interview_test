print('hello altimetrik...')

#write deocrator example:

def change_name_dec(func):
    def inner(name):
        val = func(name)
        result = val.upper()
        return result
    return inner

@change_name_dec
def print_name(name):
    return name

print(print_name("kapricon"))


###########################################33333333333
#
# u = user.objects.all
# u = u.filter('active':True)
# print(len(u))

# many to many, one to many , and all possible relations


#####################################################

temp_list = [1,-2,3,4,5,-6,-4]
#rearrage(), do use inbuild function, no extra array, timecomplexity o(n) output = [-2,-4,-6,1,3,4,5]

temp_list = [-1, -2, 3, 4, 5, -6, -4]

def rearrange(temp_list):
    negative_index = 0

    for i in range(len(temp_list)):
        if temp_list[i]<0:
            temp_list[i],temp_list[negative_index]=temp_list[negative_index],temp_list[i]
            negative_index+=1


rearrange(temp_list)
print(temp_list)





