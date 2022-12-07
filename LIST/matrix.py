# input a matrix and print it

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


def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()


#print_matrix(input_matrix(3,3))
