import argparse
from aocd import get_data

def look_and_say(sequence: str) -> str:
    """
    Generate the next term in the look-and-say sequence.

    Args:
        sequence (str): The current sequence

    Returns:
        str: The next sequence in the look-and-say series
    """
    if not sequence:
        return ""

    result = []
    current_digit = sequence[0]
    count = 1

    # Iterate through the sequence starting from the second character
    for i in range(1, len(sequence)):
        if sequence[i] == current_digit:
            count += 1
        else:
            # Append count and digit to result
            result.append(str(count))
            result.append(current_digit)

            # Reset for next digit
            current_digit = sequence[i]
            count = 1

    # Don't forget the last group
    result.append(str(count))
    result.append(current_digit)

    return ''.join(result)

def solve_part1(initial_sequence: str, iterations: int = 40) -> int:
    """
    Solve part 1: Find the length after the specified number of iterations.

    Args:
        initial_sequence (str): The starting sequence
        iterations (int): Number of iterations to perform

    Returns:
        int: Length of the sequence after iterations
    """
    sequence = initial_sequence
    for _ in range(iterations):
        sequence = look_and_say(sequence)
    return len(sequence)

def solve_part2(initial_sequence: str) -> int:
    """
    Solve part 2: Find the length after 50 iterations.

    Args:
        initial_sequence (str): The starting sequence

    Returns:
        int: Length of the sequence after 50 iterations
    """
    return solve_part1(initial_sequence, 50)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 10: Elves Look, Elves Say")
    parser.add_argument(
        '--part',
        type=int,
        choices=[1, 2],
        default=1,
        help='Which part of the puzzle to solve (default: 1)'
    )
    parser.add_argument(
        '--use-file',
        type=str,
        help='Use a local file instead of fetching data from adventofcode.com'
    )
    args = parser.parse_args()

    # Get the input data
    if args.use_file:
        try:
            with open(args.use_file, 'r') as file:
                data = file.read().strip()
        except FileNotFoundError:
            print(f"Input file not found: {args.use_file}")
            return
    else:
        try:
            data = get_data(day=10, year=2015).strip()
        except Exception as e:
            print(f"Error fetching data from adventofcode.com: {e}")
            print("Make sure AOC_SESSION environment variable is set with your session token.")
            print("You can also use --use-file to read from a local file.")
            return

    # The input is a single line with the initial sequence
    initial_sequence = data

    # Solve the appropriate part
    if args.part == 1:
        result = solve_part1(initial_sequence)
        print(f"Part 1 - Length after 40 iterations: {result}")
    else:  # part 2
        result = solve_part2(initial_sequence)
        print(f"Part 2 - Length after 50 iterations: {result}")

if __name__ == "__main__":
    main()
