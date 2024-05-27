import random

NUM_PAIRS = 3

def main():
    # Milestone #1: Create the truth list
    truth_list = create_truth_list(NUM_PAIRS)
    print("Truth List:", truth_list)  # For debugging

    # Milestone #2: Shuffle the list
    random.shuffle(truth_list)
    print("Shuffled Truth List:", truth_list)  # For debugging

    # Milestone #3: Create a displayed list
    displayed_list = ['*'] * len(truth_list)
    print("Displayed List:", displayed_list)

    # Milestone #6: Play multiple turns
    while '*' in displayed_list:
        clear_terminal()
        print("Displayed List:", displayed_list)
        
        # Get two valid indices from the user
        index1 = get_valid_index(displayed_list)
        index2 = get_valid_index(displayed_list, index1)
        
        # Show the values to the user
        if truth_list[index1] == truth_list[index2]:
            print(f"Match! Both values are {truth_list[index1]}")
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]
        else:
            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")
        
        input("Press Enter to continue...")

    clear_terminal()
    print("Congratulations! You won!")
    print("Final Displayed List:", displayed_list)

def create_truth_list(num_pairs):
    truth_list = []
    for i in range(num_pairs):
        truth_list.append(i)
        truth_list.append(i)
    return truth_list

def get_valid_index(displayed_list, previous_index=None):
    while True:
        try:
            index = int(input("Enter an index: "))
            if index < 0 or index >= len(displayed_list):
                print("Invalid index. Must be between 0 and", len(displayed_list) - 1)
            elif displayed_list[index] != '*':
                print("Invalid index. This card is already revealed.")
            elif index == previous_index:
                print("Invalid index. You can't choose the same index twice.")
            else:
                return index
        except ValueError:
            print("Invalid input. Please enter an integer.")

def clear_terminal():
    for _ in range(20):
        print('\n')

if __name__ == '__main__':
    main()
