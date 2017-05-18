from functools import reduce
from math import factorial
import random
from pentominos import *
import numpy as np

side = 8



def output_str(input_var, output_var, rect_tuple):
    return_value = ''.join([input_var + '(:, :, 1, ' + str(i + 1) + ') = [\n ' + str(rect_tuple[0][i])[1:] + ';\n'
                      for i in range(len(rect_tuple[0]))])
    return return_value + ''.join([output_var, ' = categorical([\n'] + [str(x) + '\n' for x in rect_tuple[1]] + [']);'])


def combination(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))


def random_pentomino():
    pentomino = pentominos[random.randint(0, len(pentominos) - 1)]
    rotate = random.randint(0, 3)
    if rotate == 0 or rotate == 2:
        height = pentomino.height
        length = pentomino.length
    else:
        height = pentomino.length
        length = pentomino.height
    vert_offset = random.randint(0, side - height)
    hor_offset = random.randint(0, side - length)
    return put(np.zeros((side, side), np.int8), pentomino, (vert_offset, hor_offset), rotate), target(pentomino)

def random_pentominos(num):
    matrices = np.zeros((num, side, side), np.int8)
    targets = np.zeros((num, 18), np.int8)
    for i in range(num):
        temp = random_pentomino()
        matrices[i] = temp[0]
        targets[i] = temp[1]
    return matrices, targets

def all_possible_pentominos():
    matrices = np.zeros((2452, side, side), np.int8)
    targets = np.zeros((2452, 1), np.int8)
    count = 0
    for pentomino in pentominos:
        for rotate in range(4):
            if pentomino == pentomino1 and rotate > 1:
                break
            if pentomino == pentomino14 and rotate > 0:
                break
            if rotate % 2 == 0:
                height = pentomino.height
                length = pentomino.length
            else:
                height = pentomino.length
                length = pentomino.height
            for vert_offset in range(side - height + 1):
                for hor_offset in range(side - length + 1):
                    matrices[count] = put(np.zeros((side, side), np.int8), pentomino, (vert_offset, hor_offset), rotate)
                    targets[count] = target(pentomino)
                    count += 1

    return matrices, targets
output_file = open('pentomino_test_all.m', 'w')
tup = all_possible_pentominos()
output = output_str('testsamples', 'testtargets', tup)
print(output)
output_file.write(output)
output_file.close()
