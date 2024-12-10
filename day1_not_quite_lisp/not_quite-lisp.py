# part1.py

def compute_final_floor(instructions: str) -> int:
    """
    Computes the final floor after processing the instructions.
    
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
        # If there are other characters, you can handle them here
    return floor

def main():
    # Read the input from a file
    try:
        with open('day01/input.txt', 'r') as file:
            instructions = file.read().strip()
    except FileNotFoundError:
        print("Input file not found. Please ensure 'input.txt' is in the 'day01' directory.")
        return
    
    final_floor = compute_final_floor(instructions)
    print(f"Santa ends up on floor: {final_floor}")

if __name__ == "__main__":
    main()
