import argparse

def compute_wrapping_paper(l: int, w: int, h: int) -> int:
    """
    Computes the total wrapping paper needed for a single present.
    
    Args:
        l (int): Length of the present.
        w (int): Width of the present.
        h (int): Height of the present.
    
    Returns:
        int: Total wrapping paper required for the present.
    """
    # Surface area
    side1 = l * w
    side2 = w * h
    side3 = h * l
    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    
    # Slack (area of the smallest side)
    slack = min(side1, side2, side3)
    
    return surface_area + slack

def compute_ribbon(l: int, w: int, h: int) -> int:
    """
    Computes the total ribbon needed for a single present.
    
    Args:
        l (int): Length of the present.
        w (int): Width of the present.
        h (int): Height of the present.
    
    Returns:
        int: Total ribbon required for the present.
    """
    # Smallest perimeter
    sides = sorted([l, w, h])  # Sort to get smallest two sides
    smallest_perimeter = 2 * (sides[0] + sides[1])
    
    # Volume
    volume = l * w * h
    
    return smallest_perimeter + volume

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 2")
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to the input file containing the dimensions of the presents'
    )
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as file:
            dimensions = file.readlines()
    except FileNotFoundError:
        print(f"Input file not found: {args.input_file}")
        return

    total_paper = 0
    total_ribbon = 0

    for line in dimensions:
        # Parse the dimensions, e.g., "2x3x4" -> l=2, w=3, h=4
        try:
            l, w, h = map(int, line.strip().split('x'))
        except ValueError:
            print(f"Invalid line format: {line.strip()}")
            continue
        
        total_paper += compute_wrapping_paper(l, w, h)
        total_ribbon += compute_ribbon(l, w, h)
    
    print(f"Part 1: Total wrapping paper required: {total_paper} square feet")
    print(f"Part 2: Total ribbon required: {total_ribbon} feet")

if __name__ == "__main__":
    main()
