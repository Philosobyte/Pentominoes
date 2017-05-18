import numpy as np

class pentomino1:
    length = 1
    height = 5
    target = 1
    indices = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]


class pentomino2:
    length = 3
    height = 3
    target = 2
    indices = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)]


class pentomino3:
    length = 3
    height = 3
    target = 3
    indices = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)]


class pentomino4:
    length = 2
    height = 4
    target = 4
    indices = [(0, 1), (1, 1), (2, 1), (3, 0), (3, 1)]


class pentomino5:
    length = 2
    height = 4
    target = 5
    indices = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]


class pentomino6:
    length = 2
    height = 3
    target = 6
    indices = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)]


class pentomino7:
    length = 2
    height = 3
    target = 7
    indices = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]


class pentomino8:
    length = 2
    height = 4
    target = 8
    indices = [(0, 1), (1, 1), (2, 0), (2, 1), (3, 0)]


class pentomino9:
    length = 2
    height = 4
    target = 9
    indices = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)]


class pentomino10:
    length = 3
    height = 3
    target = 10
    indices = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)]


class pentomino11:
    length = 3
    height = 2
    target = 11
    indices = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]


class pentomino12:
    length = 3
    height = 3
    target = 12
    indices = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]


class pentomino13:
    length = 3
    height = 3
    target = 13
    indices = [(0, 2), (1, 1), (1, 2), (2, 0), (2, 1)]


class pentomino14:
    length = 3
    height = 3
    target = 14
    indices = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]


class pentomino15:
    length = 2
    height = 4
    target = 15
    indices = [(0, 1), (1, 0), (1, 1), (2, 1), (3, 1)]


class pentomino16:
    length = 2
    height = 4
    target = 16
    indices = [(0, 0), (1, 0), (1, 1), (2, 0), (3, 0)]


class pentomino17:
    length = 3
    height = 3
    target = 17
    indices = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)]


class pentomino18:
    length = 3
    height = 3
    target = 18
    indices = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]


def put(matrix, pentomino, offset, rotate=0):
    indices = pentomino.indices
    temp_matrix = np.zeros((pentomino.height, pentomino.length), np.int8)
    for i in range(5):
        temp_matrix[indices[i][0]][indices[i][1]] = 1
    temp_matrix = np.rot90(temp_matrix, rotate)
    for i in range(len(temp_matrix)):
        for j in range(len(temp_matrix[0])):
            matrix[i + offset[0]][j + offset[1]] = temp_matrix[i][j]
    return matrix

def target(pentomino):
    return targets[pentomino]

pentominos = [pentomino1, pentomino2, pentomino3, pentomino4, pentomino5, pentomino6, pentomino7, pentomino8,
              pentomino9, pentomino10, pentomino11, pentomino12, pentomino13, pentomino14, pentomino15, pentomino16,
              pentomino17, pentomino18]
targets = {pentomino1: 1,
           pentomino2: 2,
           pentomino3: 3,
           pentomino4: 4,
           pentomino5: 5,
           pentomino6: 6,
           pentomino7: 7,
           pentomino8: 8,
           pentomino9: 9,
           pentomino10: 10,
           pentomino11: 11,
           pentomino12: 12,
           pentomino13: 13,
           pentomino14: 14,
           pentomino15: 15,
           pentomino16: 16,
           pentomino17: 17,
           pentomino18: 18}




