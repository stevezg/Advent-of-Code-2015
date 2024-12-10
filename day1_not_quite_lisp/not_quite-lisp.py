# part1.py

import argparse

def compute_final_floor(instructions: str) -> int:
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

def main():
    parser = argparse.ArgumentParser(description="Compute Santa's final floor.")
    parser.add_argument(
        'input_file',
        nargs='?',
        default='day01/input.txt',
        help='Path to the input file (default: day01/input.txt)'
    )
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as file:
            instructions = file.read().strip()
    except FileNotFoundError:
        print(f"Input file not found: {args.input_file}")
        return
    
    final_floor = compute_final_floor(instructions)
    print(f"Santa ends up on floor: {final_floor}")

if __name__ == "__main__":
    main()
