#!/usr/bin/env python3

#run as python makeExtrudeMeshDict.py puntosSplineReduced.csv system/extrudeMeshDict  --tolerance 1.0 --mergeTol 1.0 --layers 10 --surface outlet.vtk --npoints 300
import argparse


def read_points(fname):
    pts = []

    with open(fname) as f:
        for line in f:

            s = line.strip()

            if not (s.startswith("(") and s.endswith(")")):
                continue

            vals = s.strip("()").split()

            if len(vals) != 3:
                continue

            pts.append(tuple(map(float, vals)))

    return pts

def split_points(points):

    vertices = []
    arc_points = []

    if len(points) < 3:
        raise RuntimeError("Need at least 3 points")

    vertices.append(points[0])
    vertices.append(points[1])
    vertices.append(points[2])

    for i in range(3, len(points)):

        if i % 2 == 1:
            arc_points.append(points[i])

        else:
            vertices.append(points[i])

    return vertices, arc_points


def write_header(f,
                 surface,
                 layers,
                 expansion):

    f.write(
f"""/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\\\    /   O peration     | Version:  v2412                                 |
|   \\\\  /    A nd           | Website:  www.openfoam.com                      |
|    \\\\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      extrudeMeshDict;
}}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

constructFrom   surface;

surface         "<constant>/triSurface/{surface}";

flipNormals     false;

extrudeModel    polyline;

nLayers         {layers};

expansionRatio  {expansion};

polylineCoeffs
{{

"""
    )


def write_vertices(f, vertices):

    f.write(f"vertices {len(vertices)}\n")

    f.write("(\n")

    for p in vertices:

        f.write(

            f"    ({p[0]} {p[1]} {p[2]})\n"

        )

    f.write(");\n\n")

def write_edges(f, vertices, arc_points):

    f.write("edges\n")
    f.write("(\n")

    f.write("    line 0 1\n")
    f.write("    line 1 2\n")

    n_arcs = min(
        len(arc_points),
        len(vertices)-3
    )

    for i in range(n_arcs):

        p = arc_points[i]

        start_vertex = i + 2
        end_vertex   = i + 3
        print(f"arc {start_vertex} {end_vertex} "
         f"{p}")

        f.write(
            f"    arc {start_vertex} {end_vertex} "
            f"({p[0]} {p[1]} {p[2]})\n"
        )

    f.write(");\n\n")


def write_footer(f,
                 tolerance,
                 merge_tol):

    f.write(
f"""
    toleranceCheck  {tolerance};
}}

mergeFaces false;

mergeTol {merge_tol};


// ************************************************************************* //
"""
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_points"
    )

    parser.add_argument(
        "output_dict"
    )

    parser.add_argument(
        "--npoints",
        type=int,
        default=None
    )

    parser.add_argument(
        "--surface",
        default="channel.vtk"
    )

    parser.add_argument(
        "--layers",
        type=int,
        default=500
    )

    parser.add_argument(
        "--expansion",
        type=float,
        default=1.0
    )

    parser.add_argument(
        "--tolerance",
        type=float,
        default=1e-5
    )

    parser.add_argument(
        "--mergeTol",
        type=float,
        default=1e-3
    )

    args = parser.parse_args()

    pts = read_points(args.input_points)

    

    if args.npoints is not None:
        pts = pts[:args.npoints]

    vertices, arc_points = split_points(pts)

    print(f"Total points used: {len(pts)}")
    print(f"Vertices: {len(vertices)}")
    print(f"Arc points: {len(arc_points)}")

    print("\nLast vertices:")
    for p in vertices[-3:]:
        print(p)

    print("\nLast arc points:")
    for p in arc_points[-3:]:
        print(p)


    with open(args.output_dict, "w") as f:

        write_header(
            f,
            args.surface,
            args.layers,
            args.expansion
        )

        write_vertices(
            f,
            vertices
        )

        write_edges(f,vertices,arc_points)

        write_footer(
            f,
            args.tolerance,
            args.mergeTol
        )


if __name__ == "__main__":
    main()
