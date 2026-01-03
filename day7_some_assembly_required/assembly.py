import argparse
import re
from aocd import get_data
from functools import lru_cache

class Circuit:
    def __init__(self, instructions: list[str]):
        self.instructions = {}
        self.wire_values = {}

        # Parse all instructions
        for instruction in instructions:
            self._parse_instruction(instruction.strip())

    def _parse_instruction(self, instruction: str):
        """Parse a single instruction and store the operation for each wire."""
        # Match patterns like: "123 -> x" or "x AND y -> z" or "NOT x -> z"
        parts = instruction.split(' -> ')
        if len(parts) != 2:
            raise ValueError(f"Invalid instruction format: {instruction}")

        expression, target_wire = parts

        # Store the expression that produces this wire's value
        self.instructions[target_wire] = expression

    @lru_cache(maxsize=None)
    def get_wire_value(self, wire: str) -> int:
        """
        Get the value of a wire, computing it if necessary.
        Uses memoization to avoid recomputing values.
        """
        # If it's already computed, return it
        if wire in self.wire_values:
            return self.wire_values[wire]

        # If it's a direct number, return it
        if wire.isdigit():
            value = int(wire)
            self.wire_values[wire] = value
            return value

        # If it's not in instructions, it's an undefined wire
        if wire not in self.instructions:
            raise ValueError(f"Undefined wire: {wire}")

        # Get the expression for this wire
        expression = self.instructions[wire]

        # Parse and evaluate the expression
        value = self._evaluate_expression(expression)

        # Cache the result
        self.wire_values[wire] = value
        return value

    def _evaluate_expression(self, expression: str) -> int:
        """Evaluate a circuit expression."""
        tokens = expression.split()

        if len(tokens) == 1:
            # Direct assignment: "123" or "x"
            return self.get_wire_value(tokens[0])

        elif len(tokens) == 2:
            # NOT operation: "NOT x"
            if tokens[0] != "NOT":
                raise ValueError(f"Invalid unary operation: {expression}")
            operand = self.get_wire_value(tokens[1])
            return ~operand & 0xFFFF  # 16-bit NOT

        elif len(tokens) == 3:
            # Binary operation: "x AND y" or "x OR y" or "x LSHIFT 2" or "x RSHIFT 2"
            left = self.get_wire_value(tokens[0])
            op = tokens[1]
            right = self.get_wire_value(tokens[2])

            if op == "AND":
                return left & right
            elif op == "OR":
                return left | right
            elif op == "LSHIFT":
                return (left << right) & 0xFFFF  # 16-bit left shift
            elif op == "RSHIFT":
                return left >> right
            else:
                raise ValueError(f"Unknown operation: {op}")

        else:
            raise ValueError(f"Invalid expression: {expression}")

    def reset(self):
        """Reset all computed wire values (for part 2)."""
        self.wire_values.clear()
        self.get_wire_value.cache_clear()

def solve_part1(instructions: list[str]) -> int:
    """Solve part 1: find the value of wire 'a'."""
    circuit = Circuit(instructions)
    return circuit.get_wire_value('a')

def solve_part2(instructions: list[str]) -> int:
    """Solve part 2: override wire 'b' with value from part 1, then find new value of 'a'."""
    circuit = Circuit(instructions)

    # Get the value of wire 'a' from part 1
    value_a = circuit.get_wire_value('a')

    # Reset the circuit
    circuit.reset()

    # Override wire 'b' with the value from part 1
    circuit.wire_values['b'] = value_a
    circuit.get_wire_value.cache_clear()  # Clear cache since we're changing values

    # Get the new value of wire 'a'
    return circuit.get_wire_value('a')

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 7: Some Assembly Required")
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
            data = get_data(day=7, year=2015)
        except Exception as e:
            print(f"Error fetching data from adventofcode.com: {e}")
            print("Make sure AOC_SESSION environment variable is set with your session token.")
            print("You can also use --use-file to read from a local file.")
            return

    # Split into instructions
    instructions = data.strip().split('\n')

    # Solve the appropriate part
    if args.part == 1:
        result = solve_part1(instructions)
        print(f"Part 1 - Value of wire 'a': {result}")
    else:  # part 2
        result = solve_part2(instructions)
        print(f"Part 2 - New value of wire 'a': {result}")

if __name__ == "__main__":
    main()
