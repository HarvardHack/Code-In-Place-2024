def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct_count = 0
    total_questions = len(translations)

    # Loop through each key (English word) in the dictionary
    for english_word, spanish_word in translations.items():
        user_answer = input(f"What is the Spanish translation for {english_word}? ").rstrip().lower()

        # Check if user answer matches the Spanish translation
        if user_answer == spanish_word:
            print("That is correct!\n")  # Add newline after correct message
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_word}.\n")  # Add newline after incorrect message

    # Print the final score
    print(f"You got {correct_count}/{total_questions} words correct, come study again soon!")

if __name__ == "__main__":
    main()
