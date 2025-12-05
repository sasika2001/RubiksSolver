# main.py
from solver_3x3 import solve_cube

def main():
    print("Welcome to 3x3 Rubik's Cube CLI Solver (using PyCuber)")
    scramble = input("Enter scramble moves (like R U R' U'): ").strip()
    cube = solve_cube(scramble)
    print("\nCube representation after scramble:")
    print(cube)

if __name__ == "__main__":
    main()
