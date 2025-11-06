
temp_aray = [[1 ,2, 3 ,4],[6 ,8, 7, 5],[2, 4, 3, 1]]
print(temp_aray)

# result= []
# i_row = []
# j_row = []
# for i in range(1,len(temp_aray)-1):
#     for j in range(1,len(temp_aray[i])-1):
#         val = temp_aray[i][j]
#         if temp_aray[i][j-1] < val and temp_aray[i-1][j] < val and temp_aray[i][j+1] < val and temp_aray[i+1][j]:
#             print(val)
#             i_row.append(i)
#             j_row.append(j)
#
#     print("")
#
#
# for i,j in zip(i_row,j_row):
#     temp_aray[i][j]= 0
#
# print(temp_aray)

temp_array = [[1, 2, 3, 4], [6, 8, 7, 5], [2, 4, 3, 1]]


def is_greater_than_neighbors(arr, row, col):
    current_element = arr[row][col]
    neighbors = [
        (-1, 0), (1, 0), (0, -1), (0, 1)  # Above, below, left, right
    ]

    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < len(arr) and 0 <= c < len(arr[0]) and arr[r][c] < current_element:
            return False

    return True


for i in range(len(temp_array)):
    for j in range(len(temp_array[i])):
        if not is_greater_than_neighbors(temp_array, i, j):
            temp_array[i][j] = 0

# Print the updated array
for row in temp_array:
    print(row)
