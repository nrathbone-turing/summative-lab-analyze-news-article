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

def test_count_specific_word():
    assert count_specific_word(sample_text, "test") == 2
    assert count_specific_word(sample_text, "this") == 2
    assert count_specific_word(sample_text, "banana") == 0

def test_identify_most_common_word():
    assert identify_most_common_word(sample_text) == "this"  # case-insensitive tie breaker?


def test_calculate_average_word_length():
    avg = calculate_average_word_length("Hello world!")
    assert round(avg, 2) == 5.0


def test_count_paragraphs():
    assert count_paragraphs(sample_text) == 2


def test_count_sentences():
    assert count_sentences(sample_text) == 4


def test_read_text_file(tmp_path):
    file = tmp_path / "article.txt"
    file.write_text("Hello world.")
    assert read_text_file(file) == "Hello world."