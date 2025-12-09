import streamlit as st

st.title("3×3 Rubik's Cube State Input")

# Face names
faces = ["Front", "Back", "Left", "Right", "Up", "Down"]

# A dictionary to store user inputs
cube_state = {}

st.write("### Enter the colors for each face (left → right, top → bottom)")

for face in faces:
    st.subheader(face)

    cols = st.columns(3)  # 3 inputs per row
    face_colors = []

    # 3x3 input grid
    for row in range(3):
        row_colors = []
        for col in range(3):
            with cols[col]:
                color = st.text_input(
                    f"{face} ({row+1},{col+1})",
                    key=f"{face}_{row}_{col}",
                    placeholder="R/G/B/O/Y/W"
                )
                row_colors.append(color.upper())
        face_colors.append(row_colors)

    cube_state[face] = face_colors

st.write("### Final Cube State:")
st.json(cube_state)
