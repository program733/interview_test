print('test_iris...')

l1 = [1,2,3,4]
l2 = ['a','b','c']

# create list from l1 and l2
output ={}
lenl1 = len(l1)

for i in range(lenl1):
    if i<len(l2):
        output[l1[i]]=l2[i]
    else:
        output[l1[i]]='xyz'
print(output)

input_string = "{(({}([()]))){}"
def is_balenced(strings):
    stack = []
    open_braces = "({["
    close_braces = ")}]"
    stack_map = {')':"(", "}":"{","]":"["}

    for char in strings:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces:
            print(stack.pop)
            print(".")
            print(stack_map[char])
            if not stack or stack.pop() != stack_map[char]:
                print(char)
                return False
        else:
            continue
    #print(not stack)

    return not stack

print(is_balenced(input_string))