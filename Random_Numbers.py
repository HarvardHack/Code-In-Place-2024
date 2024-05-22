import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    Print 10 random numbers in the range 1 to 100.
    """
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    for number in random_numbers:
        print(number)

if __name__ == '__main__':
    main()
