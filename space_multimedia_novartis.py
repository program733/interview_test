print('Hello world...')

# def is_prime(no):
#     for i in range(2,int((no**0.5))+1):
#         if no%i == 0:
#             print('no is  not prime')
#             exit()
#
#     print('given no is prime')
# is_prime(13)
#
# def file_gen(file_path):
#     with open(file_path,'r') as file:
#         for line in file:
#             yield line
#
# for line in file_gen(file_path):
#     print(line)


import pandas as pd

# Create a sample DataFrame (replace this with your actual DataFrame)
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Salary': [50000, 60000, 75000, 60000]}

df = pd.DataFrame(data)

# Sort the DataFrame by 'Salary' column in descending order
df_sorted = df.sort_values(by='Salary', ascending=False)
print(df_sorted)

# Extract the second row (contains the second-highest salary)
second_highest_salary = df_sorted.iloc[1]['Salary']

print("Second-highest salary:", second_highest_salary)
