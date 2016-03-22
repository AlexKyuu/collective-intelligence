# coding=utf-8

from math import sqrt

def read_file(filename):
    lines = [line for line in file(filename)]

    # 第一行是列标题
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # 每行的第一列是行名
        rownames.append(p[0])
        # 剩余部分就是该行对应的数据
        data.append([float(x) for x in p[1:]])

    return rownames, colnames, data


# 皮尔逊相关度计算
def pearson(v1, v2):
    # 简单求和
    sum1 = sum(v1)
    sum2 = sum(v2)

    # 求平方和
    sum1_sq = sum([pow(v, 2) for v in v1])
    sum2_sq = sum([pow(v, 2) for v in v2])

    # 求乘积之和
    p_sum = sum([v1[i] * v2[i] for i in range(len(v1))])

    # 计算 r (Pearson score)
    num = p_sum - (sum1 * sum2 / len(v1))
    den = sqrt((sum1_sq - pow(sum1, 2) / len(v1)) * sum2_sq - pow(sum2, 2) / len(v1))
    if den == 0:
        return 0

    return 1.0 - num / den


class BiCluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance
