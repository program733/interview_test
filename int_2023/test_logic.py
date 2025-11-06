print('test_logic...')

inputlist = [("Kapil",29), ("Upendra",27),("Jyoti", 28)]
outputolist = [('Upendra', 27), ('Jyoti', 28), ('Kapil', 29)]
#
#
# def print_name(name):
#     print(name)
#
# val = 'test2'
# print_name('test')
# print_name(val)
input_string = "{(({}([()])))}"
def is_balanced(s):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            # Ignore characters other than brackets
            continue

    # If the stack is empty at the end, all brackets are balanced
    return not stack

# Example usage

result = is_balanced(input_string)
if result:
    print("The input string is balanced.")
else:
    print("The input string is not balanced.")


# temp_list = [9,3,2,4,5,6,7,5,2]
#
# ln = len(temp_list)
# for i in range(ln):
#     for j in range(ln-i-1):
#         if temp_list[j] > temp_list[j+1]:
#             temp_list[j],temp_list[j+1]=temp_list[j+1],temp_list[j]
#     print(temp_list)
# print('final')
# print(temp_list)