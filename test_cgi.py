# dict_one = [{"a":1, "b": 2, "c": 3}, {"a": 2, "b": 4}, {"c": 47}]


# output = [{"a": 3, "b": 6,"c": 50}]


v_list = [{"a":1, "b": 2, "c": 3}, {"a": 2, "b": 4}, {"c": 47}]

#result = [{key:value} for key, value in v_list.items()]


def calculate_di(t_list):
    result_di = {}
    for di in t_list:
        for key,value in di.items():
            #print(key,value)
            if key in result_di.keys():
                result_di[key] = result_di[key] + value
            else:
                result_di[key] = value

    print(result_di)



calculate_di(v_list)

