import pytest
from word_count import count_words, count_words_in_file

def test_count_words():
    text = "Hello world! Hello Python. Python is fun."
    expected = {'hello': 2, 'world': 1, 'python': 2, 'is': 1, 'fun': 1}
    assert count_words(text) == expected

def test_count_words_in_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "provinces.txt"
    test_file.write_text("Hello world! Hello Python. Python is fun.")
    
    expected = {'hello': 2, 'world': 1, 'python': 2, 'is': 1, 'fun': 1}
    assert count_words_in_file(test_file) == expected

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        count_words_in_file("provinces.txt")
