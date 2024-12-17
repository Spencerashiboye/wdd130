import pytest
from collections import Counter
from word_count import count_words, count_words_in_file

def test_count_words():
    # Test with a simple sentence
    text = "Hello world! Hello everyone."
    expected = Counter({"hello": 2, "world": 1, "everyone": 1})
    assert count_words(text) == expected

    # Test with an empty string
    text = ""
    expected = Counter()
    assert count_words(text) == expected

    # Test with special characters
    text = "Python, Python! Python?"
    expected = Counter({"python": 3})
    assert count_words(text) == expected

    # Test with mixed case
    text = "Python python PYTHON"
    expected = Counter({"python": 3})
    assert count_words(text) == expected

@pytest.fixture
def create_temp_file(tmp_path):
    def _create_temp_file(content):
        temp_file = tmp_path / "test_file.txt"
        temp_file.write_text(content, encoding="utf-8")
        return temp_file
    return _create_temp_file

def test_count_words_in_file_utf8(create_temp_file):
    # Test with a UTF-8 encoded file
    content = "Hello world! Hello everyone."
    temp_file = create_temp_file(content)
    expected = Counter({"hello": 2, "world": 1, "everyone": 1})
    assert count_words_in_file(str(temp_file)) == expected

def test_count_words_in_file_non_utf8(create_temp_file):
    # Test with a non-UTF-8 encoded file
    content = "Café résumé naïve"
    temp_file = create_temp_file(content)
    # Write the file in latin-1 encoding
    temp_file.write_text(content, encoding="latin-1")
    expected = Counter({"café": 1, "résumé": 1, "naïve": 1})
    assert count_words_in_file(str(temp_file)) == expected

def test_count_words_in_file_file_not_found():
    # Test with a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        count_words_in_file("non_existent_file.txt")

def test_count_words_in_file_empty(create_temp_file):
    # Test with an empty file
    temp_file = create_temp_file("")
    expected = Counter()
    assert count_words_in_file(str(temp_file)) == expected

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
