#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path


# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

CASE_DIR = Path.cwd()

PROFILE_VTK = CASE_DIR / "constant/triSurface/outlet.vtk"

BC_TEMPLATE_DIR = CASE_DIR / "templates/0"

MAKE_DICT_SCRIPT = CASE_DIR / "utils/makeExtrudeMeshDict.py"

VTP2VTK_SCRIPT = CASE_DIR / "utils/vtp2vtk.py"

GEOMETRY_FILE = CASE_DIR / "geometry/puntosSplineReduced.csv"


# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------

def run(cmd, logfile=None):

    print("\n>>>", " ".join(cmd))

    if logfile:

        with open(logfile, "w") as f:

            subprocess.run(
                cmd,
                stdout=f,
                stderr=subprocess.STDOUT,
                check=True
            )

    else:

        subprocess.run(
            cmd,
            check=True
        )

def find_outlet_vtp():

    files = list(
        CASE_DIR.glob(
            "VTK/*/boundary/outlet.vtp"
        )
    )

    if not files:

        raise FileNotFoundError(
            "No outlet.vtp found"
        )

    return files[0]


# ------------------------------------------------------------------
# Clean case
# ------------------------------------------------------------------

def clean_case():

    if Path("./Allclean").exists():

        run(["./Allclean"])


# ------------------------------------------------------------------
# Generate VTK profile
# ------------------------------------------------------------------

def generate_profile():

    run(["blockMesh"])

    run([
        "foamToVTK",
        "-ascii"
    ])


# ------------------------------------------------------------------
# Convert VTP -> VTK
# ------------------------------------------------------------------

def convert_surface():

    profile_vtp = find_outlet_vtp()

    PROFILE_VTK.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    run([
        "python3",
        str(VTP2VTK_SCRIPT),
        str(profile_vtp),
        str(PROFILE_VTK)
    ])


# ------------------------------------------------------------------
# Generate extrudeMeshDict
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

        "--npoints", "300"#300

    ])


# ------------------------------------------------------------------
# Run extrudeMesh
# ------------------------------------------------------------------

def run_extrude():

    run(

        ["extrudeMesh"],

        logfile="log.extrudeMesh.arc"

    )


def run_checkmesh():

    run(

        [

            "checkMesh",

            "-writeAllFields",

            "-time",

            "1"

        ],

        logfile="log.checkMesh.arc"

    )

# ------------------------------------------------------------------
# Create_initial_conditions
# ------------------------------------------------------------------

def create_initial_conditions():

    if Path("0").exists():

        shutil.rmtree("0")

    shutil.copytree(

        "0.orig",

        "0"

    )

# ------------------------------------------------------------------
# Rename patches
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
# Main
# ------------------------------------------------------------------

def main():

    clean_case()

    generate_profile()

    convert_surface()

    generate_dict()

    run_extrude()

    run_checkmesh()

    rename_patches()
    create_initial_conditions()

    print("\nCase ready.")


if __name__ == "__main__":

    main()