import random

def roll_dice():
    """Simulates rolling a single six-sided die."""
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Example usage:
if __name__ == "__main__":
    print ("Ramya")
    print("Rolling the die...")
    result = roll_dice()
    print(f"The die rolled a win number : {result}")

    # You can also simulate multiple rolls or multiple dice
    print("\nRolling two dice:")
    die1 = roll_dice()
    die2 = roll_dice()
    print(f"Die 1: {die1}, Die 2: {die2}")
    print(f"Total: {die1 + die2}")

