import argparse

def count_unique_houses_with_robo_santa(directions: str) -> int:
    """
    Counts the number of unique houses visited by Santa and Robo-Santa.
    
    Args:
        directions (str): A string of directions (^, v, >, <).
        
    Returns:
        int: Number of unique houses visited.
    """
    # Starting positions
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited = set()
    visited.add((0, 0))  # Add starting location

    # Process each direction
    for i, move in enumerate(directions):
        # Determine who is moving
        if i % 2 == 0:  # Santa's turn
            if move == '^':
                santa_y += 1
            elif move == 'v':
                santa_y -= 1
            elif move == '>':
                santa_x += 1
            elif move == '<':
                santa_x -= 1
            visited.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if move == '^':
                robo_y += 1
            elif move == 'v':
                robo_y -= 1
            elif move == '>':
                robo_x += 1
            elif move == '<':
                robo_x -= 1
            visited.add((robo_x, robo_y))

    return len(visited)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 3, Part 2")
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to the input file containing Santa\'s directions'
    )
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as file:
            directions = file.read().strip()
    except FileNotFoundError:
        print(f"Input file not found: {args.input_file}")
        return

    unique_houses = count_unique_houses_with_robo_santa(directions)
    print(f"Total unique houses visited: {unique_houses}")

if __name__ == "__main__":
    main()
