import argparse

def compute_final_floor(instructions: str) -> int:
    """
    Computes the final floor Santa ends up on after following all instructions.
    
    Args:
        instructions (str): A string of '(' and ')' characters.
        
    Returns:
        int: The final floor number.
    """
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

def find_first_basement_position(instructions: str) -> int:
    """
    Finds the position of the first character that causes Santa to enter the basement.
    
    Args:
        instructions (str): A string of '(' and ')' characters.
        
    Returns:
        int: The 1-based index position of the first character that causes Santa 
             to reach floor -1. Returns -1 if never reached.
    """
    floor = 0
    for index, char in enumerate(instructions):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return index + 1  # Convert 0-based index to 1-based
    return -1  # If never reaches the basement

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 1")
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to the input file containing the instructions'
    )
    args = parser.parse_args()

    # Read the input file
    try:
        with open(args.input_file, 'r') as file:
            instructions = file.read().strip()
    except FileNotFoundError:
        print(f"Input file not found: {args.input_file}")
        return

    # Part 1: Compute the final floor
    final_floor = compute_final_floor(instructions)
    print(f"Part 1: Santa ends up on floor {final_floor}")

    # Part 2: Find the position of the first basement entry
    basement_position = find_first_basement_position(instructions)
    if basement_position != -1:
        print(f"Part 2: Santa enters the basement at position {basement_position}")
    else:
        print("Part 2: Santa never enters the basement")

if __name__ == "__main__":
    main()
