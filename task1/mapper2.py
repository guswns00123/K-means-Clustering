#!/usr/bin/env python
import sys
from math import*

def euclidean_distance(x, y):
    return sqrt(sum(pow(float(a) - float(b), 2) for a, b in zip(x, y)))

#file = open("new_cent", "r")
# file = open("cent_2023", "r")
# file = open("cent_4", "r")
file = open("./hw3/cent_64","r")
# file = open("cent_random_seed_2", "r")
#file = open("./hw3/new_cent", "r")
centroids = [[0 for i in range(64)] for j in range(10)]

for line in file:
    line = line.strip()
    line, img = line.split(",")
    header, count = line.split(":")
    header, index = header.split(" ")
    cent_img = img.strip().split(" ")
    centroids[int(index)] = cent_img

cnt = [0 for i in range(10)]

for line in sys.stdin:
    line = line.strip()
    img = [item for item in line.split(",")]
    min_dis = euclidean_distance(centroids[0] , img)
    # print(min_dis)
    min_idx = 0
    for i in range(1,10):
        dis = euclidean_distance(centroids[i], img)
        if dis < min_dis:
            min_dis = dis
            min_idx = i
            
    img = " ".join(str(k) for k in img)
    print("%s\t%s" %(str(min_idx), img))
    
