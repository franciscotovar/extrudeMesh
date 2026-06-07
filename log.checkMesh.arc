/*---------------------------------------------------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  2412                                  |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
Build  : _8dbc61e11c-20241220 OPENFOAM=2412 version=v2412
Arch   : "LSB;label=32;scalar=64"
Exec   : checkMesh -writeAllFields -time 1
Date   : Jun 07 2026
Time   : 15:39:06
Host   : franciscos-MacBook-Pro.local
PID    : 72754
I/O    : uncollated
Case   : /Users/tovar/OpenFOAM/tovar-v2412/run/hydrodynamic_age/extrudeMesh/polyline
nProcs : 1
trapFpe: Floating point exception trapping enabled (FOAM_SIGFPE).
fileModificationChecking : Monitoring run-time modified files using timeStampMaster (fileModificationSkew 5, maxFileModificationPolls 20)
allowSystemOperations : Allowing user-supplied system call operations

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
Create time

Create mesh for time = 1

Check mesh...
    Writing mesh quality as fields (aspectRatio cellAspectRatio cellDeterminant cellRegion cellShapes cellVolume cellVolumeRatio cellZone faceWeight faceZone minPyrVolume minTetVolume nonOrthoAngle skewness wallDistance)

Time = 1

Mesh stats 
    points:           115731
    faces:            315200
    internal faces:   284800
    cells:            100000
    faces per cell:   6
    boundary patches: 3
    point zones:      0
    face zones:       0
    cell zones:       0

Overall number of cells of each type:
    hexahedra:     100000
    prisms:        0
    wedges:        0
    pyramids:      0
    tet wedges:    0
    tetrahedra:    0
    polyhedra:     0

Checking topology...
    Boundary definition OK.
    Cell to face addressing OK.
    Point usage OK.
    Upper triangular ordering OK.
    Face vertices OK.
    Number of regions: 1 (OK).

Checking patch topology for multiply connected surfaces...
    Patch               Faces    Points     Surface topology
    sides               30000    30060    ok (non-closed singly connected)  
    originalPatch       200      231      ok (non-closed singly connected)  
    otherSide           200      231      ok (non-closed singly connected)  
    ".*"                30400    30402    ok (closed singly connected)      


Checking faceZone topology for multiply connected surfaces...
    No faceZones found.

Checking basic cellZone addressing...
    No cellZones found.

Checking basic pointZone addressing...
    No pointZones found.

Checking geometry...
    Overall domain bounding box (0.01 -3385.5611 0) (3918.5868 346.50252 85)
    Mesh has 3 geometric (non-empty/wedge) directions (1 1 1)
    Mesh has 3 solution (non-empty) directions (1 1 1)
    Boundary openness (2.0094983e-17 -3.0410714e-17 2.388291e-18) OK.
    Max cell openness = 2.4563626e-16 OK.
    Max aspect ratio = 3.3269965 OK.
    Minimum face area = 85. Maximum face area = 293.64373.  Face area magnitudes OK.
    Min volume = 1907.0742. Max volume = 2495.9717.  Total volume = 2.2018769e+08.  Cell volumes OK.
    Mesh non-orthogonality Max: 0.82219341 average: 0.034842365
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 0.044909254 OK.
    Coupled point location match (average 0) OK.

Mesh OK.

Writing fields with mesh quality parameters
    Writing non-orthogonality (angle) to nonOrthoAngle
    Writing face interpolation weights (0..0.5) to faceWeight
    Writing face skewness to skewness
    Writing cell determinant to cellDeterminant
    Writing aspect ratio to aspectRatio
    Writing approximate aspect ratio to cellAspectRatio
    Writing cell shape (hex, tet etc.) to cellShapes
    Writing cell volume to cellVolume
    Writing cell volume ratio to cellVolumeRatio
    Writing minTetVolume to minTetVolume
    Writing minPyrVolume to minPyrVolume
    Writing cell region to cellRegion
    Writing cell zoning to cellZone
    Writing face zoning to faceZone

End

