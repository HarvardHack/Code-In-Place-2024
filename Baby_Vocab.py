from collections import Counter

def main():
    words = load_words_from_file("words.txt")
    word_counts = Counter(words)
    for word, count in word_counts.items():
        print_histogram_bar(word, count)

def print_histogram_bar(word, count):
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    return words

if __name__ == '__main__':
    main()
