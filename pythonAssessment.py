import re
# regex expressions to use
# r"\b\w+\b" - match all words with no punctuation, use with find_all function from re module
# r"(?<=[.!?]) +" - match punctuation and used to split sentences, use with split function from re module
# "\n\n" - not true regex but can be used to split on line break
from collections import Counter
from pathlib import Path

# Function to load in and read the data from an input
def read_text_file(file_path):
    None

# Function to count the number of times a specific word is used in the text.
def count_specific_word(text, word):
    None

# Function to identify the most common word in the text.
def identify_most_common_word(text):
    None

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