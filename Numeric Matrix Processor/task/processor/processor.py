import sys
import numpy as np
import ast


def add_matrices():
    matrix1_shape = [ast.literal_eval(i) for i in input('Enter size of first matrix:').split()]
    matrix1 = []
    print('Enter first matrix:')
    for i in range(matrix1_shape[0]):
        matrix1.append(list(ast.literal_eval(k) for k in input().split()))
    matrix1 = np.array(matrix1)
    matrix2_shape = [ast.literal_eval(i) for i in input('Enter size of second matrix:').split()]
    matrix2 = []
    print('Enter second matrix:')
    for i in range(matrix2_shape[0]):
        matrix2.append(list(ast.literal_eval(k) for k in input().split()))
    matrix2 = np.array(matrix2)
    if matrix1_shape == matrix2_shape:
        result = matrix1 + matrix2
        print('The result is:')
        for row in result:
            print(' '.join(map(str, row)))
    else:
        print('The operation cannot be performed.')


def mult_matr_numb():
    matrix1_shape = [ast.literal_eval(i) for i in input('Enter size of matrix:').split()]
    matrix1 = []
    print('Enter matrix:')
    for i in range(matrix1_shape[0]):
        matrix1.append(list(ast.literal_eval(k) for k in input().split()))
    matrix1 = np.array(matrix1)
    number = ast.literal_eval(input('Enter constant'))
    result = number * matrix1
    print('The result is:')
    for row in result:
        print(' '.join(map(str, row)))


def mult_matrices():
    matrix1_shape = [ast.literal_eval(i) for i in input('Enter size of first matrix:').split()]
    matrix1 = []
    print('Enter first matrix:')
    for i in range(matrix1_shape[0]):
        matrix1.append(list(ast.literal_eval(k) for k in input().split()))
    matrix1 = np.array(matrix1)
    matrix2_shape = [ast.literal_eval(i) for i in input('Enter size of second matrix:').split()]
    matrix2 = []
    print('Enter second matrix:')
    for i in range(matrix2_shape[0]):
        matrix2.append(list(ast.literal_eval(k) for k in input().split()))
    matrix2 = np.array(matrix2)
    if matrix1_shape[1] == matrix2_shape[0]:
        result = []
        for k in range(matrix1_shape[0]):
            result.append([])
            for l in range(matrix2_shape[1]):
                result[-1].append(sum(matrix1[k,:]*matrix2[:,l]))
        print('The result is:')
        for row in result:
            print(' '.join(map(str, row)))


def transpose_matrix():
    def main_diagonal(matrix: np.ndarray):
        local_result = []
        for i in range(len(matrix)):
            temp = matrix[:,i]
            local_result.append(temp)
        return local_result

    def side_diagonal(matrix: np.ndarray):
        local_result = []
        for i in range(-1, -len(matrix)-1, -1):
            temp = reversed(matrix[:, i])
            local_result.append(temp)
        return local_result

    def vertical(matrix: np.ndarray):
        local_result = []
        for i in range(len(matrix)):
            temp = reversed(matrix[i,:])
            local_result.append(temp)
        return local_result

    def horizontal(matrix: np.ndarray):
        local_result = []
        for i in range(-1, -len(matrix)-1, -1):
            temp = matrix[i, :]
            local_result.append(temp)
        return local_result

    print('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    local_command = input()
    matrix1_shape = [ast.literal_eval(i) for i in input('Enter matrix size:').split()]
    matrix1 = []
    print('Enter matrix:')
    for i in range(matrix1_shape[0]):
        matrix1.append(list(ast.literal_eval(k) for k in input().split()))
    matrix1 = np.array(matrix1)
    if local_command == '1':
        result = main_diagonal(matrix1)
    elif local_command == '2':
        result = side_diagonal(matrix1)
    elif local_command == '3':
        result = vertical(matrix1)
    elif local_command == '4':
        result = horizontal(matrix1)
    print('The result is:')
    for row in result:
        print(' '.join(map(str, row)))


def determinant():
    matrix1_shape = [ast.literal_eval(i) for i in input('Enter matrix size:').split()]
    matrix1 = []
    print('Enter matrix:')
    for i in range(matrix1_shape[0]):
        matrix1.append(list(ast.literal_eval(k) for k in input().split()))
    matrix1 = np.array(matrix1)
    result = np.linalg.det(matrix1)
    print('The result is:')
    print(result)


def inverse():
    matrix1_shape = [ast.literal_eval(i) for i in input('Enter matrix size:').split()]
    matrix1 = []
    print('Enter matrix:')
    for i in range(matrix1_shape[0]):
        matrix1.append(list(ast.literal_eval(k) for k in input().split()))
    matrix1 = np.array(matrix1)
    result = np.linalg.inv(matrix1)
    print('The result is:')
    for row in result:
        print(' '.join(map(str, row)))

while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    command = input()
    if command == '1':
        add_matrices()
    elif command == '2':
        mult_matr_numb()
    elif command == '3':
        mult_matrices()
    elif command == '4':
        transpose_matrix()
    elif command == '5':
        determinant()
    elif command == '6':
        inverse()
    elif command == '0':
        sys.exit()
