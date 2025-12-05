# solver_3x3.py
import pycuber as pc

def solve_cube(scramble_moves=None):
    """
    scramble_moves: optional string with moves to scramble the cube
    Example: "R U R' U'"
    """
    cube = pc.Cube()  # solved cube

    if scramble_moves:
        # Apply scramble
        try:
            sequence = pc.Formula(scramble_moves)
            cube(sequence)
        except Exception as e:
            print("Error parsing scramble moves:", e)
            return

    print("\nCurrent Cube State:")
    print(cube)

    # PyCuber does not have built-in solver, but we can print cube state
    # For automated solution, you can integrate with external solver later

    return cube

# Test code
if __name__ == "__main__":
    scramble = input("Enter scramble moves (like R U R' U'): ").strip()
    solve_cube(scramble)
