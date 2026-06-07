#!/usr/bin/env python3

import argparse


def transpose_points(input_file, output_file, mode="zyx", scale=1.0):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:

        for line in fin:

            stripped = line.strip()

            # Only process lines that look like points
            if stripped.startswith("(") and stripped.endswith(")"):

                vals = stripped.strip("()").split()

                if len(vals) != 3:
                    fout.write(line)
                    continue

                x = float(vals[0])
                y = float(vals[1])
                z = float(vals[2])

                x *= scale
                y *= scale
                z *= scale

                # (x,y,z) -> (y,z,x)
                coords = {"x": x,"y": y,"z": z}

                out = [coords[c] for c in mode]

                fout.write(

                    f"    ({out[0]} {out[1]} {out[2]})\n"

                )

            else:
                # Copy everything else unchanged
                fout.write(line)


def main():
    parser = argparse.ArgumentParser(
        description="Transpose point coordinates (x,y,z) -> (y,z,x)"
    )

    parser.add_argument("input_file", help="Input file")
    parser.add_argument("output_file", help="Output file")
    parser.add_argument("--mode", choices=["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"],default="zyx",help="Coordinate permutation")
    parser.add_argument(

    "--scale",

    type=float,

    default=1e-3,

    help="Scale factor"

)

    args = parser.parse_args()

    transpose_points(args.input_file, args.output_file, args.mode, args.scale)


if __name__ == "__main__":
    main()