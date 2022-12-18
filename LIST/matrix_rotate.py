import matrix as m

# mat1 = [
#         [1,2,3],
#         [4,5,6]
#         ]

mat1 = [
    [1,4],
    [2,5],
    [3,6]
]

# mat1 = [
#     [1,5,7],
#     [9,6,3],
#     [2,1,3]
# ]


print(len(mat1))    # row
print(len(mat1[0])) # col

row = len(mat1)
col = len(mat1[0])

temp_mat = []
for i in range(col):
    temp = []
    for j in range(row-1,-1,-1):
        temp.append(mat1[j][i])
    temp_mat.append(temp)

m.print_matrix(mat1)
print()
m.print_matrix(temp_mat)
