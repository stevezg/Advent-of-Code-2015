import argparse
from aocd import get_data
from itertools import permutations
from collections import defaultdict

def parse_distances(lines: list[str]) -> dict:
    """
    Parse the distance data into a dictionary of dictionaries.

    Args:
        lines (list[str]): List of distance lines

    Returns:
        dict: Distance matrix as {city1: {city2: distance, ...}, ...}
    """
    distances = defaultdict(dict)

    for line in lines:
        parts = line.split()
        if len(parts) != 5 or parts[1] != 'to' or parts[3] != '=':
            continue

        city1, city2 = parts[0], parts[2]
        distance = int(parts[4])

        # Add both directions since distances are bidirectional
        distances[city1][city2] = distance
        distances[city2][city1] = distance

    return distances

def calculate_route_distance(route: list[str], distances: dict) -> int:
    """
    Calculate the total distance of a route.

    Args:
        route (list[str]): List of cities in order
        distances (dict): Distance matrix

    Returns:
        int: Total distance, or float('inf') if route is invalid
    """
    total_distance = 0

    for i in range(len(route) - 1):
        city1, city2 = route[i], route[i + 1]
        if city2 not in distances[city1]:
            return float('inf')  # Invalid route
        total_distance += distances[city1][city2]

    return total_distance

def find_shortest_route(distances: dict) -> int:
    """
    Find the shortest route that visits all cities exactly once.

    Args:
        distances (dict): Distance matrix

    Returns:
        int: Length of the shortest route
    """
    cities = list(distances.keys())

    if not cities:
        return 0

    shortest_distance = float('inf')

    # Try all permutations of cities
    for route in permutations(cities):
        distance = calculate_route_distance(route, distances)
        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance

def find_longest_route(distances: dict) -> int:
    """
    Find the longest route that visits all cities exactly once.

    Args:
        distances (dict): Distance matrix

    Returns:
        int: Length of the longest route
    """
    cities = list(distances.keys())

    if not cities:
        return 0

    longest_distance = 0

    # Try all permutations of cities
    for route in permutations(cities):
        distance = calculate_route_distance(route, distances)
        if distance > longest_distance:
            longest_distance = distance

    return longest_distance

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 9: All in a Single Night")
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
            data = get_data(day=9, year=2015)
        except Exception as e:
            print(f"Error fetching data from adventofcode.com: {e}")
            print("Make sure AOC_SESSION environment variable is set with your session token.")
            print("You can also use --use-file to read from a local file.")
            return

    # Parse the distance data
    # The data might be a single line with embedded \n or multiple lines
    if '\n' in data:
        lines = data.strip().split('\n')
    else:
        # Handle the case where \n is escaped as \\n
        lines = data.strip().split('\\n')

    distances = parse_distances(lines)

    if not distances:
        print("No distance data found!")
        return

    print(f"Found {len(distances)} cities")

    # Solve the appropriate part
    if args.part == 1:
        result = find_shortest_route(distances)
        print(f"Part 1 - Shortest route distance: {result}")
    else:  # part 2
        result = find_longest_route(distances)
        print(f"Part 2 - Longest route distance: {result}")

if __name__ == "__main__":
    main()
