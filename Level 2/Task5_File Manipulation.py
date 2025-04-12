def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Clean the text and split into words
        words = text.lower().split()
        word_count = {}

        # Count word occurrences
        for word in words:
            # Remove punctuation from each word
            word = ''.join(char for char in word if char.isalnum())
            if word:
                word_count[word] = word_count.get(word, 0) + 1

        # Sort the dictionary by key (word)
        sorted_word_count = dict(sorted(word_count.items()))

        # Display the result
        print(f"\n📊 Word Count in '{filename}':\n")
        for word, count in sorted_word_count.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("❌ File not found. Please check the filename and try again.")

# Example usage
filename = input("Enter the filename (with .txt extension): ")
count_words_in_file(filename)
