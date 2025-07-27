import re
# regex expressions to use
# r"\b\w+\b" - match all words with no punctuation, use with find_all function from re module
# r"(?<=[.!?]) +" - match punctuation and used to split sentences, use with split function from re module
# "\n\n" - not true regex but can be used to split on line break
from collections import Counter
from pathlib import Path

# Function to load in and read the data from an input
def read_text_file(file_path):
    # Step 1: Ensure file_path is a Path object
    # Use pathlib to handle file system compatibility (cross-platform)
    file_path = Path(file_path)
    
    # Step 2: Read the file contents using .read_text()
    # Assume the encoding is UTF-8 unless specified otherwise

    # Step 3: Return the full contents as a single string
    return file_path.read_text(encoding="utf-8")

# Function to count the number of times a specific word is used in the text.
def count_specific_word(text, word):
    # Step 1: Normalize both the text and word to lowercase for case-insensitive comparison
    word = word.lower()
    
    # Step 2: Use regex to find all word-like sequences (r"\b\w+\b")
    # This filters out punctuation and captures actual words only
    words = re.findall(r"\b\w+\b", text.lower())
    
    # Step 3: Loop through the list of words
    # Count how many match the given word exactly
    count = 0
    for w in words:
        if w == word:
            count += 1
    # Step 4: Return the count
    return count

# Function to identify the most common word in the text.
def identify_most_common_word(text):
    None
    # Step 1: Convert the text to lowercase to ensure case-insensitive counting

    # Step 2: Use regex to extract all word-like sequences (r"\b\w+\b")
    # This ensures we ignore punctuation and symbols

    # Step 3: Use collections.Counter to count each word's frequency

    # Step 4: Find the word with the highest count using .most_common(1)

    # Step 5: Return that word

# Function to calculate the average length of words in the text.
# exclude punctuation and special characters
def calculate_average_word_length(text):
     None

# Function to count the number of paragraphs in the text.
# define paragraphs based on empty line breaks
def count_paragraphs(text):
     None

# Function to count the number of sentences in the text.
# define sentences based on punctuation marks
def count_sentences(text):
     None

# Main function to display and print results