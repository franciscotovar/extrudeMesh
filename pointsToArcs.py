#!/usr/bin/env python3

import argparse


def read_points(filename):

    pts = []

    with open(filename) as f:

        for line in f:

            line = line.strip()

            if not line.startswith("("):
                continue

            vals = line.strip("()").split()

            if len(vals) != 3:
                continue

            pts.append(tuple(vals))

    return pts


parser = argparse.ArgumentParser()

parser.add_argument("input")

args = parser.parse_args()

points = read_points(args.input)

vertices = []
edges = []

# First three points are vertices

vertices.append(points[0])
vertices.append(points[1])
vertices.append(points[2])

vertex_index = {
    0: 0,
    1: 1,
    2: 2
}

current_vertex = 3

for i in range(3, len(points)):

    if i % 2 == 0:

        vertices.append(points[i])

        vertex_index[i] = current_vertex

        current_vertex += 1

# Initial straight section

edges.append("line 0 1")
edges.append("line 1 2")

# Arcs

for i in range(3, len(points), 2):

    if i + 1 >= len(points):
        break

    arc_pt = points[i]

    start_vertex = vertex_index[i - 1]
    end_vertex = vertex_index[i + 1]

    edges.append(
        f"arc {start_vertex} {end_vertex} "
        f"({arc_pt[0]} {arc_pt[1]} {arc_pt[2]})"
    )

print(f"vertices {len(vertices)}")
print("(")

for p in vertices:
    print(f"    ({p[0]} {p[1]} {p[2]})")

print(");")
print()
print("edges")
print("(")

for e in edges:
    print(f"    {e}")

print(");")