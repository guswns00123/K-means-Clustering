#!/usr/bin/env python
import sys

cur_idx = None
cluster = {}
total = 0

centroids = [0 for i in range(64)] 

for line in sys.stdin:
    line = line.strip()
    idx, partial = line.split("\t")
    partial_sum, cnt = partial.split("|")
    partial_sum = partial_sum.split(",")
    for i in range(len(partial_sum)):
        partial_sum[i] = float(partial_sum[i].strip())
    idx = int(idx)
    cnt = int(cnt)

    if (cur_idx == idx):
        total += cnt
        centroids = [centroids[i] + float(partial_sum[i]) for i in range(64)]
        
    else:
        if cur_idx is not None:

            if total > 0:
                new_cent = [str(centroids[i]/total) for i in range(64)]
                new_cent = ' '.join(new_cent)
                total = str(total)
                print("Centroid "+ str(cur_idx) + ": " + str(total) + "," + new_cent)
                total = cnt
                centroids = [0 for i in range(64)] 
                centroids = [centroids[i] + float(partial_sum[i]) for i in range(64)]
            else:
                new_cent = [str(centroids[i]) for i in range(64)]
                new_cent = ' '.join(new_cent)
                print("Centroid "+ str(cur_idx) + ": " + "0" + "," + new_cent)
                total = cnt
                centroids = [0 for i in range(64)] 
                centroids = [centroids[i] + float(partial_sum[i]) for i in range(64)]

        elif cur_idx is None:
            total = cnt
            centroids = [centroids[i] + float(partial_sum[i]) for i in range(64)]
        
        
    cur_idx = idx


if total > 0:
    new_cent = [str(centroids[i]/total) for i in range(64)]
    new_cent = ' '.join(new_cent)
    total = str(total)
    print("Centroid "+ str(cur_idx) + ": " + str(total) + "," + new_cent)

else:
    new_cent = [str(centroids[i]) for i in range(64)]
    new_cent = ' '.join(new_cent)
    print("Centroid "+ str(cur_idx) + ": " + "0" + "," + new_cent)
