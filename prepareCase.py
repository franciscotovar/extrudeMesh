#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path


# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

CASE_DIR = Path.cwd()

PROFILE_VTP = CASE_DIR / "VTK/polyline_0/boundary/outlet.vtp"

PROFILE_VTK = CASE_DIR / "constant/triSurface/outlet.vtk"

BC_TEMPLATE_DIR = CASE_DIR / "templates/0"

MAKE_DICT_SCRIPT = CASE_DIR / "utils/makeExtrudeMeshDict.py"

VTP2VTK_SCRIPT = CASE_DIR / "utils/vtp2vtk.py"

GEOMETRY_FILE = CASE_DIR / "geometry/puntosSplineReduced.csv"
# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------

def run(cmd):

    print("\n>>>", " ".join(cmd))

    subprocess.run(
        cmd,
        check=True
    )

# ------------------------------------------------------------------
# Clean case
# ------------------------------------------------------------------

def clean_case():

    if Path("./Allclean").exists():

        run(["./Allclean"])

# ------------------------------------------------------------------
# 1. Generate VTK profile using blockMesh -> foamToVTK
# ------------------------------------------------------------------

def generate_profile():

    run(["blockMesh"])

    run([

        "foamToVTK",

        "-ascii"

    ])


# ------------------------------------------------------------------
# 1. Convert VTP -> VTK 
# ------------------------------------------------------------------


def convert_surface():

    PROFILE_VTK.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    run([
        "python3",
        str(VTP2VTK_SCRIPT),
        str(PROFILE_VTP),
        str(PROFILE_VTK)
    ])

# ------------------------------------------------------------------
# 2. Generate extrudeMeshDict
#  python utils/makeExtrudeMeshDict.py geometry/puntosSplineReduced.csv system/extrudeMeshDict  --tolerance 1.0e-2 --mergeTol 1.0e-2 --layers 500 --surface outlet.vtk --npoints 300
# ------------------------------------------------------------------

def generate_dict():

     run([

        "python3",

        str(MAKE_DICT_SCRIPT),

        str(GEOMETRY_FILE),

        "system/extrudeMeshDict",

        "--tolerance", "1.0e-2",

        "--mergeTol", "1.0e-2",

        "--layers", "500",

        "--surface", "outlet.vtk",

        "--npoints", "300"

    ])


# ------------------------------------------------------------------
# 3. Run extrudeMesh
# ------------------------------------------------------------------

def run_extrude():

        #run([

        #"bash",

        #"-c",

        #"USE_ARC=true arc extrudeMesh"
        run(["./Allrun"


    ])


# ------------------------------------------------------------------
# 4. Rename patches
# ------------------------------------------------------------------

def rename_patches():

    boundary_file = (
        CASE_DIR /
        "constant/polyMesh/boundary"
    )

    text = boundary_file.read_text()

    text = text.replace(
        "originalPatch",
        "inlet"
    )

    text = text.replace(
        "otherSide",
        "outlet"
    )

    text = text.replace(
        "sides",
        "walls"
    )

    boundary_file.write_text(text)

    print("Patches renamed.")


# ------------------------------------------------------------------
# 5. Copy BC templates
# ------------------------------------------------------------------

def copy_templates():

    dst = CASE_DIR / "0"

    if dst.exists():

        shutil.rmtree(dst)

    shutil.copytree(
        BC_TEMPLATE_DIR,
        dst
    )

    print("BC templates copied.")


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main():

    clean_case()
    
    generate_profile()

    convert_surface()
    
    generate_dict()

    run_extrude()

    rename_patches()

    copy_templates()

    print("\nCase ready.")


if __name__ == "__main__":

    main()