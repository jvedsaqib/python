def input_mat(order):
    row_mat = []
    for i in range(0,order):
        col_mat = []
        for j in range(0,order):
            print("Mat[",i,"][",j,"]: ")
            temp = int(input("Enter: "))
            col_mat.append(temp)
        row_mat.append(col_mat)
        print()

    return row_mat

def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end=" ")
        print()

#     0 1 2
#  0 |1 0 0|
#  1 |0 1 0|
#  2 |0 0 1|

def is_unit_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                if mat[j][i] == 1:
                    flag = True
                else:
                    flag = False
                    break
            elif i != j:
                if mat[j][i] == 0:
                    flag = True
                else:
                    flag = False
                    break
    return flag

mat = input_mat(3)

print_mat(mat)

print(is_unit_mat(mat))

