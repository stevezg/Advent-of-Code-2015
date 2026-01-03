import argparse
import re
from aocd import get_data

def parse_instruction(instruction: str) -> tuple[str, tuple[int, int], tuple[int, int]]:
    """
    Parse a single instruction and return the operation and coordinates.

    Args:
        instruction (str): The instruction string

    Returns:
        tuple: (operation, (start_x, start_y), (end_x, end_y))
    """
    # Match patterns like "turn on 0,0 through 999,999"
    # or "toggle 0,0 through 999,999"
    pattern = r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'
    match = re.match(pattern, instruction.strip())

    if not match:
        raise ValueError(f"Invalid instruction format: {instruction}")

    operation = match.group(1)
    start_x, start_y = int(match.group(2)), int(match.group(3))
    end_x, end_y = int(match.group(4)), int(match.group(5))

    return operation, (start_x, start_y), (end_x, end_y)

def process_instructions_part1(instructions: list[str]) -> int:
    """
    Process instructions for part 1 where lights are simply on/off.

    Args:
        instructions (list[str]): List of instruction strings

    Returns:
        int: Number of lights that are turned on
    """
    # Initialize 1000x1000 grid (using boolean for on/off)
    grid = [[False for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        operation, (start_x, start_y), (end_x, end_y) = parse_instruction(instruction)

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if operation == "turn on":
                    grid[x][y] = True
                elif operation == "turn off":
                    grid[x][y] = False
                elif operation == "toggle":
                    grid[x][y] = not grid[x][y]

    # Count lights that are on
    return sum(sum(row) for row in grid)

def process_instructions_part2(instructions: list[str]) -> int:
    """
    Process instructions for part 2 where lights have brightness levels.

    Args:
        instructions (list[str]): List of instruction strings

    Returns:
        int: Total brightness of all lights
    """
    # Initialize 1000x1000 grid (using integers for brightness)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        operation, (start_x, start_y), (end_x, end_y) = parse_instruction(instruction)

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if operation == "turn on":
                    grid[x][y] += 1
                elif operation == "turn off":
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif operation == "toggle":
                    grid[x][y] += 2

    # Sum all brightness levels
    return sum(sum(row) for row in grid)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 6: Probably a Fire Hazard")
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
                data = file.read()
        except FileNotFoundError:
            print(f"Input file not found: {args.use_file}")
            return
    else:
        try:
            data = get_data(day=6, year=2015)
        except Exception as e:
            print(f"Error fetching data from adventofcode.com: {e}")
            print("Make sure AOC_SESSION environment variable is set with your session token.")
            print("You can also use --use-file to read from a local file.")
            return

    # Split into instructions
    instructions = data.strip().split('\n')

    # Process instructions
    if args.part == 1:
        result = process_instructions_part1(instructions)
        print(f"Part 1 - Number of lights turned on: {result}")
    else:  # part 2
        result = process_instructions_part2(instructions)
        print(f"Part 2 - Total brightness: {result}")

if __name__ == "__main__":
    main()
