# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    age = float(input("Enter an age in calendar years: "))  # Get the number of feet, make sure to cast it to a float!
    dog_years = age * DOG_YRS_MULTIPLIER  # Perform the conversion
    print("That's", dog_years, "in dog years!")
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
