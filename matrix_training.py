#!/usr/bin/python3
from functools import reduce
import sys


def mat_multi(matrix_1, matrix_2):
    # list notation
    res_mat = [mat_vec_multi(matrix_1, vector) for vector in matrix_2]
    # # map notation
    # res_mat = list(map(lambda vector: mat_vec_multi(matrix_1, vector), matrix_2))
    return res_mat


def mat_vec_multi(matrix, vector):
    # #for loop notation
    # vector_length = len(vector)
    # matrix_x = len(matrix)
    # matrix_y = matrix[0]
    # res_vector = []
    # if matrix_x == vector_length:
    #     index = 0
    #     new_vec_collection=[]
    #     for i in matrix:
    #         new_vec = vec_scal_multi(i, vector[index])
    #         new_vec_collection.append(new_vec)
    #         index += 1
    #     result_vector = reduce(vector_addition, new_vec_collection)
    # # map notation
    # result_vector = reduce(vector_addition, list(map(vec_scal_multi, matrix, vector)))
    # list zip notation
    result_vector = reduce(vector_addition, [vec_scal_multi(x, y) for x, y in zip(matrix, vector)])
    return result_vector


def vec_scal_multi(vector, scalar):
    # # for loop notation
    # new_vector = []
    # for i in vector:
    #     new_vector.append(i*scalar)
    # # map notation
    # new_vector = list(map(lambda x: x*scalar, vector))
    # list notation
    new_vector = [x * scalar for x in vector]
    return new_vector


def vector_addition(vector1, vector2):
    # # map notation/comprehension
    # new_vec = map(lambda x, y: x * y, vector1, vector2)
    # list-zip notation/comprehension
    new_vec = [x + y for x, y in zip(vector1, vector2)]
    bigger_vector = max(vector1, vector2)
    smaller_vector = min(vector1, vector2)
    bigger_vector_remain = bigger_vector[len(smaller_vector):]
    new_vec += bigger_vector_remain
    return new_vec


def matrix_rank(matrix):
    if len(matrix) == len(matrix[0]):
        return len(matrix)
    else:
        return max(len(matrix), len(matrix[0]))


def determinant(matrix):
    def deter_of_2b2():
        a = matrix[0][0]
        b = matrix[1][0]
        c = matrix[0][1]
        d = matrix[1][1]
        deter = a * d - b * c
        return deter

    def deter_of_3b3():
        a = matrix[0][0]
        b = matrix[1][0]
        c = matrix[2][0]
        d = matrix[0][1]
        e = matrix[1][1]
        f = matrix[2][1]
        g = matrix[0][2]
        h = matrix[1][2]
        i = matrix[2][2]
        return 0

    mat_rank = matrix_rank(matrix)
    if mat_rank == 2:
        return deter_of_2b2()
    if mat_rank == 3:
        return deter_of_3b3()


if __name__ == "__main__":
    # matrix_1 = [[2, 3, 4, 5, 0], [4, 4, 5, 1, 1], [4, 4, 5, 1, 1], [1, 3, 4, 0, 1]]
    # matrix_2 = [[1, 4, 3], [1, 4, 2]]
    # print (sys.argv[1])
    matrix = [[2, 2], [3, 1]]
    print("the determinant of the matrix is : {}".format(determinant(matrix)))
    print(matrix_rank(matrix))
    # print("my matrix: ", mat_multi(matrix_1, matrix_2))
