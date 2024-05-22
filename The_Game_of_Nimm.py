def main():
    stones = 20
    turns = 1

    while stones > 0:
        whose_turn_is_it = turns % 2
        print(f"There are {stones} stones left.")
        if whose_turn_is_it > 0:
            how_many_to_remove = input("Player 1 would you like to remove 1 or 2 stones? ")
            while how_many_to_remove not in ['1', '2']:
                how_many_to_remove = input("Please enter 1 or 2: ")
            how_many_to_remove = int(how_many_to_remove)
            stones -= how_many_to_remove
            turns += 1
            print()
        elif whose_turn_is_it == 0:
            how_many_to_remove = input("Player 2 would you like to remove 1 or 2 stones? ")
            while how_many_to_remove not in ['1', '2']:
                how_many_to_remove = input("Please enter 1 or 2: ")
            how_many_to_remove = int(how_many_to_remove)
            stones -= how_many_to_remove
            turns += 1
            print()
    
    if whose_turn_is_it > 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == '__main__':
    main()
