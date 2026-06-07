#!/usr/bin/env python3

import sys

try:
    import vtk
except ImportError:
    raise RuntimeError(
        "VTK not available. Install with: pip install vtk"
    )


reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName(sys.argv[1])
reader.Update()

polydata = reader.GetOutput()

writer = vtk.vtkPolyDataWriter()
writer.SetFileName(sys.argv[2])
writer.SetFileTypeToASCII()
writer.SetInputData(polydata)

if not writer.Write():
    raise RuntimeError("Failed writing vtk file")

print(f"Converted {sys.argv[1]} -> {sys.argv[2]}")