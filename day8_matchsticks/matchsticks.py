import argparse
from aocd import get_data

def calculate_literal_length(s: str) -> int:
    """
    Calculate the length of the string as it appears in the code (literal length).
    This includes the surrounding quotes and all escape sequences.

    Args:
        s (str): The string literal from the input

    Returns:
        int: The literal length
    """
    return len(s)

def calculate_memory_length(s: str) -> int:
    """
    Calculate the length of the string in memory (actual character count).
    This is what the string represents after processing escape sequences.

    Args:
        s (str): The string literal from the input

    Returns:
        int: The memory length
    """
    # Remove the surrounding quotes
    if s.startswith('"') and s.endswith('"'):
        content = s[1:-1]
    else:
        raise ValueError(f"String doesn't have surrounding quotes: {s}")

    # Process escape sequences
    i = 0
    memory_length = 0

    while i < len(content):
        if content[i] == '\\':
            # Escape sequence
            if i + 1 < len(content):
                next_char = content[i + 1]
                if next_char == '\\' or next_char == '"':
                    # \\ or \" -> single character
                    memory_length += 1
                    i += 2
                elif next_char == 'x' and i + 3 < len(content):
                    # \xHH -> single character
                    memory_length += 1
                    i += 4
                else:
                    raise ValueError(f"Invalid escape sequence: \\{next_char}")
            else:
                raise ValueError(f"Trailing backslash in string: {s}")
        else:
            # Regular character
            memory_length += 1
            i += 1

    return memory_length

def calculate_encoded_length(s: str) -> int:
    """
    Calculate the length of the string if it were encoded as a string literal.
    This means escaping special characters in the string and adding surrounding quotes.

    Args:
        s (str): The original string (already a string literal with quotes)

    Returns:
        int: The encoded length
    """
    # First escape backslashes in the original string
    encoded = s.replace('\\', '\\\\')

    # Then escape quotes in the original string
    encoded = encoded.replace('"', '\\"')

    # Finally add surrounding quotes
    encoded = '"' + encoded + '"'

    return len(encoded)

def solve_part1(strings: list[str]) -> int:
    """
    Solve part 1: Find the difference between literal and memory lengths.

    Args:
        strings (list[str]): List of string literals

    Returns:
        int: Total difference
    """
    total_literal = 0
    total_memory = 0

    for s in strings:
        literal_len = calculate_literal_length(s)
        memory_len = calculate_memory_length(s)

        total_literal += literal_len
        total_memory += memory_len

    return total_literal - total_memory

def solve_part2(strings: list[str]) -> int:
    """
    Solve part 2: Find the difference between encoded and literal lengths.
    For part 2, we encode each string literal as a string literal itself.

    Args:
        strings (list[str]): List of string literals

    Returns:
        int: Total difference
    """
    total_encoded = 0
    total_literal = 0

    for s in strings:
        literal_len = calculate_literal_length(s)
        # For part 2, encode the entire string literal as data
        encoded_len = calculate_encoded_length(s)

        total_literal += literal_len
        total_encoded += encoded_len

    return total_encoded - total_literal

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 8: Matchsticks")
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
            data = get_data(day=8, year=2015)
        except Exception as e:
            print(f"Error fetching data from adventofcode.com: {e}")
            print("Make sure AOC_SESSION environment variable is set with your session token.")
            print("You can also use --use-file to read from a local file.")
            return

    # Split into strings (each line is a string literal)
    strings = data.strip().split('\n')

    # Solve the appropriate part
    if args.part == 1:
        result = solve_part1(strings)
        print(f"Part 1 - Total difference: {result}")
    else:  # part 2
        result = solve_part2(strings)
        print(f"Part 2 - Total difference: {result}")

if __name__ == "__main__":
    main()
