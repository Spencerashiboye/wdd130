from collections import Counter
import re

def count_words(text):
    """
    Counts the occurrences of each word in a given text.

    Args:
        text (str): The input text to process.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def count_words_in_file(filename):
    """
    Reads a file and counts the occurrences of each word in its content.

    Args:
        filename (str): The name of the file to process.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
    """
    try:
        # Try reading the file with UTF-8 encoding first
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        # Fallback to a more permissive encoding if UTF-8 fails
        with open(filename, 'r', encoding='latin-1') as file:
            text = file.read()
    return count_words(text)

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        word_counts = count_words_in_file(filename)
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{filename}'. Please ensure it is a valid text file.")
    except Exception as e:
        print(f"An error occurred: {e}")
