# test_pythonAssessment.py
import pytest
from pythonAssessment import (
    read_text_file,
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences
)

sample_text = """
This is a test. This test is simple.

It has two paragraphs! Can you believe it? Yes.
"""

def test_read_text_file(tmp_path):
    file = tmp_path / "article.txt"
    file.write_text("Hello world.")
    assert read_text_file(file) == "Hello world."

def test_count_specific_word():
    sample = "This is a test. This test is only a test!"
    assert count_specific_word(sample, "test") == 3
    assert count_specific_word(sample, "this") == 2
    assert count_specific_word(sample, "banana") == 0

def test_identify_most_common_word():
    sample = "Dog cat dog bird cat dog."
    assert identify_most_common_word(sample) == "dog"

def test_identify_most_common_word_tie():
    sample = "apple banana banana apple"
    # Both appear twice — 'apple' comes first in text
    result = identify_most_common_word(sample)
    assert result == "apple"

def test_calculate_average_word_length():
    sample = "Hello world!"
    assert calculate_average_word_length(sample) == 5.0

    sample2 = "Short longer longest."
    # lengths: 5 + 6 + 7 = 18 → 18 / 3 = 6.0
    assert calculate_average_word_length(sample2) == 6.0

    sample3 = ""  # edge case: no words
    assert calculate_average_word_length(sample3) == 0.0

def test_count_paragraphs():
    sample = (
        "This is paragraph one.\n"
        "Still paragraph one.\n\n"
        "This is paragraph two.\n\n"
        "This is paragraph three."
    )
    assert count_paragraphs(sample) == 3

    sample2 = "\n\n\n" # edge case: empty paragraphs
    assert count_paragraphs(sample2) == 0

def test_count_sentences():
    assert count_sentences(sample_text) == 4