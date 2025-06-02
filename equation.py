import sys
import os
import math

def parse_float(prompt):
    while True:
        value = input(f"{prompt} = ").strip()
        try:
            return float(value)
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead")

def solve_quadratic(a, b, c):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2*a)
        root2 = (-b + math.sqrt(discriminant)) / (2*a)
        print("There are 2 roots")
        print(f"x1 = {root1}")
        print(f"x2 = {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print("There are 1 roots")
        print(f"x1 = {root}")
    else:
        print("There are 0 roots")

def interactive_mode():
    a = parse_float("a")
    while a == 0:
        print("Error. a cannot be 0")
        a = parse_float("a")
    b = parse_float("b")
    c = parse_float("c")
    solve_quadratic(a, b, c)

def file_mode(filepath):
    if not os.path.exists(filepath):
        print(f"file {filepath} does not exist")
        sys.exit(1)

    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
            parts = content.split()
            if len(parts) != 3:
                raise ValueError("invalid file format")
            a, b, c = map(float, parts)
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)
            solve_quadratic(a, b, c)
    except ValueError:
        print("invalid file format")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: ./equation [filename]")
        sys.exit(1)