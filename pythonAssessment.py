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
    # Step 1: Convert the text to lowercase to ensure case-insensitive counting
    text = text.lower()
    
    # Step 2: Use regex to extract all word-like sequences (r"\b\w+\b")
    # This ensures we ignore punctuation and symbols
    words = re.findall(r"\b\w+\b", text)
    
    # Step 3: Use collections.Counter to count each word's frequency
    # returns a list with one tuple: (word, count)
    counts = Counter(words)
    
    # Step 4: Find the word with the highest count using .most_common(1)
    most_common_word = counts.most_common(1)[0][0]
    
    # Step 5: Return that word
    return most_common_word

# Function to calculate the average length of words in the text.
# exclude punctuation and special characters
def calculate_average_word_length(text):
    # Step 1: Convert text to lowercase again
    text = text.lower()
    
    # Step 2: Use regex to extract all word-like sequences (r"\b\w+\b")
    # This filters out punctuation and gives a clean list of words
    words = re.findall(r"\b\w+\b", text)
    
    # If there are no words at all (edge case validation), return 0.0 to avoid `ZeroDivisionError`
    if not words:
        return 0.0
    
    # Step 3: Calculate the total number of characters across all words
    # Sum the lengths of all words in the list
    total_chars = 0
    for word in words:
        total_chars += len(word)
    
    # Step 4: Divide total characters by number of words to get average
    average = total_chars / len(words)
    
    # Step 5: Return the average rounded to two decimal places
    return round(average, 2)

# Function to count the number of paragraphs in the text.
# define paragraphs based on empty line breaks
def count_paragraphs(text):
    # Step 1: Split the text on two consecutive newlines ("\n\n")
    # This creates a list of paragraph blocks
    raw_paragraphs = text.split("\n\n")
    
    # Step 2: Strip whitespace from each paragraph and filter out empty ones
    # This avoids counting accidental blank lines
    paragraphs = []
    for p in raw_paragraphs:
        if p.strip():  # Only keep non-empty paragraphs
            paragraphs.append(p)

    # Step 3: Return the number of non-empty paragraphs
    return len(paragraphs)

# Function to count the number of sentences in the text.
# define sentences based on punctuation marks
def count_sentences(text):
    None
    # Step 1: Use regex split to break the text at punctuation that ends sentences
    # Pattern: r"(?<=[.!?]) +" to match space(s) that follow a sentence-ending punctuation

    # Step 2: Strip and filter out any blank segments (e.g., extra punctuation at end)

    # Step 3: Return the number of non-empty sentences


# Main function to display and print results