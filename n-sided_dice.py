import random

def main():
    # Prompt the user for the number of sides on the dice
    sides = int(input("How many sides does your dice have? "))
    
    # Simulate rolling the dice
    roll = random.randint(1, sides)
    
    # Print the outcome of the roll
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()
