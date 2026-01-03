import hashlib

def find_lowest_number(secret_key: str, prefix: str = "000000") -> int:
    """
    Finds the lowest positive number that, when appended to the secret key,
    produces an MD5 hash starting with the given prefix.
    
    Args:
        secret_key (str): The secret key.
        prefix (str): The required prefix for the hash (default is "00000").
        
    Returns:
        int: The lowest positive number that produces a valid hash.
    """
    number = 1  # Start with the first positive number
    while True:
        # Concatenate the secret key and number, then compute MD5 hash
        test_input = f"{secret_key}{number}"
        hash_result = hashlib.md5(test_input.encode()).hexdigest()
        
        # Check if the hash starts with the desired prefix
        if hash_result.startswith(prefix):
            return number
        number += 1

def main():
    secret_key = "ckczppom"
    result = find_lowest_number(secret_key)
    print(f"The lowest number for prefix '00000' is: {result}")

if __name__ == "__main__":
    main()
