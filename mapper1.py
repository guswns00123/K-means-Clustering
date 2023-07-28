#!/usr/bin/env python
import sys
from math import*

def euclidean_distance(x, y):
    return sqrt(sum(pow(float(a) - float(b), 2) for a, b in zip(x, y)))

# file = open("new_cent", "r")
# file = open("./hw3/cent_32", "r")
file = open("cent_64","r")
# file = open("./hw3/new_cent", "r")
centroids = [[0 for i in range(64)] for j in range(10)]
cent = []
for line in file:
    line = line.strip()
    line, img = line.split(",")
    header, count = line.split(":")
    header, index = header.split(" ")
    cent_img = img.strip().split(" ")
    cent = []

    for i in range(len(cent_img)):
        if (cent_img[i] != ""):
            formatted_num = '{:.5f}'.format(float(cent_img[i]))
            # print(formatted_num)
            # print(cent_img[i])
            cent.append(formatted_num)

    
    centroids[int(index)] = cent


partial_sums_counts = {}

for i in range(10):
    partial_sums_counts.setdefault(i, [0 for i in range(64)] )

def sum_vector(A,B):
    return [float(x)+float(y) for x,y in zip(A, B)]


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

    partial_sums_counts[min_idx] = sum_vector(partial_sums_counts[min_idx], img)
    # print(min_idx, partial_sums_counts[min_idx])

    cnt[min_idx] += 1

   
# print(cnt)
i = 0
for key, value in partial_sums_counts.items():
    print("%s\t%s|%s" %(key, str(value)[1:-1], cnt[i]))
    i +=1
    
