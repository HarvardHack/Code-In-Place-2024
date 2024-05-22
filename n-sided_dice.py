# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll


def main():
    NUM_SIDES = int(input("How many sides does your dice have?: ")) 
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    
    # Roll die
    die = random.randint(1, NUM_SIDES)
    
    
    # Get their total
    total = die
    
    # Print out the results
    
    print("Your roll is", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
