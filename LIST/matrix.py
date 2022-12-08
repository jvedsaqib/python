# input a matrix

def input_matrix(row_len, col_len):
    mat = []
    for i in range(row_len):
        col = []
        for j in range(col_len):
            print("[", i ,"][", j ,"] : ")
            temp = int(input())
            col.append(temp)
        mat.append(col)
        print()
    return mat

# print a matrix

def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()

# addition of two matrix

def add(mat1, mat2):
    res_mat = []
    for i in range(len(mat1)):
        res_mat_col = []
        for j in range(len(mat2)):
            temp = mat1[i][j] + mat2[i][j]
            res_mat_col.append(temp)
        res_mat.append(res_mat_col)
    
    return res_mat


#print_matrix(input_matrix(3,3))
