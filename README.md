ExtrudeMesh Polyline Workflow

This project generates CFD-ready volumetric meshes by extruding a surface profile along a curved polyline trajectory.

Workflow

1. Generate trajectory points (PHIDL / Python).
2. Build extrudeMeshDict using makeExtrudeMeshDict.py.
3. Generate a profile surface (outlet.vtk recommended).
4. Run Allrun.
5. Verify mesh quality using checkMesh.

Important Notes

* Use original spline points only.
* Curved paths require vertex / arc-point alternation.
* Profile orientation is critical.
* Always validate the final mesh with checkMesh.

Current Status

Validated for:

* Curved serpentine trajectories.
* Polyline extrusion using original spline points.
* Hexahedral mesh generation.
* Mesh quality verification (Mesh OK).

Future Work

* Mesh refinement and wall grading.
* Geometric amplification metrics.
