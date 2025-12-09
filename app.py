import streamlit as st

# Patch for Python 3.10+ compatibility
import sys
if sys.version_info >= (3, 10):
    import collections.abc
    import builtins
    import types
    import importlib

    # Monkey patch old Iterable import for rubik_solver
    import rubik_solver.utils
    rubik_solver.utils.collections = collections
    importlib.reload(rubik_solver.utils)

from rubik_solver import utils  # Pure Python solver

st.title("3×3 Rubik's Cube Solver (Python)")

# Standard face order required by the solver: U, R, F, D, L, B
solver_order = ["Up", "Right", "Front", "Down", "Left", "Back"]

# UI display order (full names)
ui_faces = ["Front", "Back", "Left", "Right", "Up", "Down"]

# Storage for cube state
cube_state = {}

st.write("### Enter the colors for each face (Use: W=White, Y=Yellow, R=Red, O=Orange, G=Green, B=Blue)")

# Build the UI input
for face in ui_faces:
    st.subheader(face)
    cols = st.columns(3)
    face_colors = []

    for r in range(3):
        row_colors = []
        for c in range(3):
            with cols[c]:
                color = st.text_input(
                    f"{face} ({r+1},{c+1})",
                    key=f"{face}_{r}_{c}",
                    placeholder="W/Y/R/O/G/B"
                ).upper()
                row_colors.append(color)
        face_colors.append(row_colors)
    cube_state[face] = face_colors

st.write("### Current Cube State (JSON)")
st.json(cube_state)

# --- Conversion to solver format ---
def convert_to_solver_format(cube_state):
    # Map UI faces to solver order
    final_state = ""
    for face in solver_order:
        face_key = face
        for row in cube_state[face_key]:
            for color in row:
                final_state += color
    return final_state

st.write("---")

if st.button("Solve Cube"):
    try:
        cube_string = convert_to_solver_format(cube_state)
        st.write("### Solver Format String:")
        st.code(cube_string)

        # Solve the cube using rubik-solver (pure Python)
        solution = utils.solve(cube_string, 'Kociemba')  # Kociemba algorithm
        st.success("### 🔥 Shortest Solution:")
        st.write(' '.join(solution))

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Check that:\n- All faces contain valid letters (W,Y,R,O,G,B)\n- Exactly one center of each color exists\n- Cube is valid.")
