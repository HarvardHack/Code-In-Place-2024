def main():
    # Ask the user for their height in meters
    height = float(input("Enter your height in meters: "))

    # Determine and print the appropriate message based on the height
    if height > 1.6 and height < 1.9:
        print("Correct height to be an astronaut")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    elif height >= 1.9:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
