import argparse
from aocd import get_data

def has_three_vowels(s: str) -> bool:
    """
    Checks if the string contains at least three vowels (a, e, i, o, u).
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string contains at least three vowels, False otherwise.
    """
    vowels = set("aeiou")
    vowel_count = sum(1 for char in s if char in vowels)
    return vowel_count >= 3

def has_double_letter(s: str) -> bool:
    """
    Checks if the string contains at least one letter that appears twice in a row.
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string contains a double letter, False otherwise.
    """
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

def has_no_forbidden_substrings(s: str) -> bool:
    """
    Checks if the string does not contain any of the forbidden substrings.
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string does not contain forbidden substrings, False otherwise.
    """
    forbidden = {"ab", "cd", "pq", "xy"}
    for sub in forbidden:
        if sub in s:
            return False
    return True

def is_nice(s: str) -> bool:
    """
    Determines if a string is "nice" based on the rules.
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string is nice, False otherwise.
    """
    return (
        has_three_vowels(s) and
        has_double_letter(s) and
        has_no_forbidden_substrings(s)
    )

def has_repeating_pair(s: str) -> bool:
    """
    Checks if the string contains a pair of any two letters that appears
    at least twice in the string without overlapping.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string contains a repeating pair, False otherwise.
    """
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        # Look for this pair elsewhere in the string, not overlapping
        if pair in s[i+2:]:
            return True
    return False

def has_repeating_letter_with_gap(s: str) -> bool:
    """
    Checks if the string contains at least one letter which repeats with
    exactly one letter between them (e.g., xyx, abcabca, etc.).

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string contains a repeating letter with gap, False otherwise.
    """
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

def is_nice_part2(s: str) -> bool:
    """
    Determines if a string is "nice" based on the new rules for part 2.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is nice, False otherwise.
    """
    return (
        has_repeating_pair(s) and
        has_repeating_letter_with_gap(s)
    )

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 5")
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
            data = get_data(day=5, year=2015)
        except Exception as e:
            print(f"Error fetching data from adventofcode.com: {e}")
            print("Make sure AOC_SESSION environment variable is set with your session token.")
            print("You can also use --use-file to read from a local file.")
            return

    # Split into strings
    strings = data.strip().split('\n')

    # Process strings and count "nice" ones
    if args.part == 1:
        nice_count = sum(1 for s in strings if is_nice(s))
        print(f"Part 1 - Total number of nice strings: {nice_count}")
    else:  # part 2
        nice_count = sum(1 for s in strings if is_nice_part2(s))
        print(f"Part 2 - Total number of nice strings: {nice_count}")

if __name__ == "__main__":
    main()
