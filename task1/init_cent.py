#!/usr/bin/env python

from numpy import random
import numpy as np


file = open("./hw3/MNIST/train_img", "r")
img = []
res = []
random_seed = 1000

#random_seed = 2023
random_seed = 1004
#random_seed = 2027
#random_seed = 4000

random.seed(random_seed)
randoms = [random.randint(1,10000) for i in range(10)]
line_num = 0
sample = []

for line in file:
    line_num += 1
    line = line.strip()
    img = [int(img_item) for img_item in line.split(',')]
    if line_num in randoms:
        res.append(img)

random_img = res
cluster = [0 for i in range(10)]
result = ""

for i in range(10):
    format1 = "Centroid " + str(i) + ": "
    img = [str(res[i][j]) for j in range(784)]
    img = ' '.join(img)
    format1 = format1 + str(cluster[i]) + ", " + img
    print(format1)

