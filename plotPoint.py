#!/usr/bin/env python3
import numpy as np

import matplotlib.pyplot as plt

ys=[]

zs=[]

with open("points_transposed.txt") as f:

    for line in f:

        vals = line.replace("(","").replace(")","").split()

        if len(vals) != 3:

            continue

        ys.append(float(vals[1]))

        zs.append(float(vals[2]))

plt.plot(ys,zs)

plt.axis('equal')

plt.show()

pts = np.loadtxt("points_transposed.txt")

plt.plot(pts[:,1], pts[:,2], '-')

plt.axis('equal')

plt.show()