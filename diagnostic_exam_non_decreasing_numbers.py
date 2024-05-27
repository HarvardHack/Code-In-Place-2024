def main():
    print("Enter a sequence of non-decreasing numbers.")
    
    # Initialize the sequence list and the previous number as None
    sequence = []
    previous_num = None
    
    while True:
        try:
            num = float(input("Enter num: "))
            # Check if the entered number is less than the previous number
            if previous_num is not None and num < previous_num:
                break
            sequence.append(num)
            previous_num = num
        except ValueError:
            print("Please enter a valid number.")
    
    print("Thanks for playing!")
    print(f"Sequence length: {len(sequence)}")

if __name__ == "__main__":
    main()
