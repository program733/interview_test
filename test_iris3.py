print('hello world ...')
# input_str = 'I am a good explorer'
# output_str = 'explorer good a am I'
#
# list_str = input_str.split(" ")
# #print(list_str)
#
# print(" ".join(list_str[::-1]))
# #print(input_str[::-1])

question = 'Input = 2,8 output should be 3'

def get_power(base,value):
    mul = 1
    count = 0
    while mul < value:
        mul = mul*base
        count +=1

    print(count)

get_power(5,625)
