def matrix_multiply(matrixA, matrixB):

    rowCountsInB = len(matrixB)
    for row in matrixA:
        if len(row) != rowCountsInB:
            raise ValueError


    # TODO: check problem with this matrix initialization approach
    # result2 = [[0] * len(matrixB[0])] * len(matrixA)
    # print(result2, len(result2), len(result2[0]))
    # result2[0][0] = 12332
    # print(result2)
    result = [[0,0], [0,0]]

    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


if __name__ == "__main__":
    matrixA = [
        [1,2,3],
        [4,5,6]
    ]
    matrixB = [
        [1,2],
        [3,4],
        [5,6]
    ]
    result = matrix_multiply(matrixA, matrixB)
    print(result)