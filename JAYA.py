#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 10:12
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : JAYA.py
# @Statement : JAYA algorithm
# @Reference : Rao R. Jaya: A simple and new optimization algorithm for solving constrained and unconstrained optimization problems[J]. International Journal of Industrial Engineering Computations, 2016, 7(1): 19-34.
import copy
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(value, lb, ub):
    """
    The boundary check
    :param value:
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    for i in range(len(value)):
        value[i] = max(value[i], lb[i])
        value[i] = min(value[i], ub[i])
    return value


def main(pop, iter, lb, ub):
    """
    The main function of the JAYA
    :param pop: the number of candidates
    :param iter: the iteration number
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    pos = []  # the position of all candidates
    score = []  # the score of all candidates
    dim = len(lb)  # dimension
    for i in range(pop):
        temp_pos = [random.uniform(lb[j], ub[j]) for j in range(dim)]
        pos.append(temp_pos)
        score.append(obj(temp_pos))
    iter_best = []
    gbest = min(score)  # the score of the best-so-far candidate
    gbest_pos = pos[score.index(gbest)].copy()  # the position of the best-so-far candidate
    iter_con = 0

    # Step 2. The main loop
    for t in range(iter):
        # Step 2.1. Identify the best and worst solutions
        best_score = min(score)
        best_pos = pos[score.index(best_score)].copy()
        worst_score = max(score)
        worst_pos = pos[score.index(worst_score)].copy()
        if best_score < gbest:
            gbest = best_score
            gbest_pos = best_pos.copy()
            iter_con = t + 1
        iter_best.append(gbest)

        # Step 2.2. Modify solutions
        new_pos = copy.deepcopy(pos)
        new_score = []
        for i in range(pop):
            for j in range(dim):
                new_pos[i][j] += random.random() * (best_pos[j] - abs(pos[i][j])) - random.random() * (
                            worst_pos[j] - abs(pos[i][j]))
            new_pos[i] = boundary_check(new_pos[i], lb, ub)  # boundary check
            new_score.append(obj(new_pos[i]))

        # Step 2.3. Evaluate new solutions
        for i in range(pop):
            if new_score[i] < score[i]:
                score[i] = new_score[i]
                pos[i] = new_pos[i].copy()

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.show()
    return {'best score': gbest, 'best solution': gbest_pos, 'convergence iteration': iter_con}


if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 1000
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
