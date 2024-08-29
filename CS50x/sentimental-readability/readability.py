def count_letters(text):
    """Count the number of letters in the text."""
    return sum(1 for char in text if char.isalpha())

def count_words(text):
    """Count the number of words in the text."""
    return len(text.split())

def count_sentences(text):
    """Count the number of sentences in the text."""
    return sum(1 for char in text if char in '.?!')

def coleman_liau_index(letters, words, sentences):
    """Calculate the Coleman-Liau index."""
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return 0.0588 * L - 0.296 * S - 15.8

def main():
    # Get user input
    text = input("Phrase: ")

    # Count letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate the Coleman-Liau index
    index = coleman_liau_index(letters, words, sentences)
    rounded_index = round(index)

    # Print the grade
    if rounded_index < 1:
        print("Grade: Before Grade 1")
    elif rounded_index >= 16:
        print("Grade: 16+")
    else:
        print(f"Grade: {rounded_index}")

if __name__ == "__main__":
    main()
