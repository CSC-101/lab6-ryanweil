from lab6 import selection_sort_books
import lab6  # Imports the whole lab6 module
from data import Book  # Import Book class from data.py
from lab6 import selection_sort_books, swap_case, str_translate  # Import functions from lab6.py

import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    import unittest
    from lab6 import selection_sort_books, Book  # Adjust import as needed

class TestSelectionSortBooks(unittest.TestCase):
    def test_selection_sort_books_standard(self):
        books = [
            Book(["Harper Lee"], "To Kill a Mockingbird"),
            Book(["George Orwell"], "1984"),
            Book(["Aldous Huxley"], "Brave New World")
        ]
        selection_sort_books(books)
        expected = [
            Book(["George Orwell"], "1984"),
            Book(["Aldous Huxley"], "Brave New World"),
            Book(["Harper Lee"], "To Kill a Mockingbird")
        ]
        self.assertEqual(books, expected)

    def test_selection_sort_books_single(self):
        books = [Book(["J.D. Salinger"], "The Catcher in the Rye")]
        selection_sort_books(books)
        expected = [Book(["J.D. Salinger"], "The Catcher in the Rye")]
        self.assertEqual(books, expected)

    if __name__ == '__main__':
        unittest.main()

    # Part 2

    import unittest
    from lab6 import swap_case  # Ensure swap_case is correctly imported

class TestSwapCase(unittest.TestCase):
    def test_swap_case_mixed(self):
        input_str = "Hello World!"
        result = swap_case(input_str)
        self.assertEqual(result, "hELLO wORLD!")

    def test_swap_case_all_lowercase(self):
        input_str = "python"
        result = swap_case(input_str)
        self.assertEqual(result, "PYTHON")

    def test_swap_case_all_uppercase(self):
        input_str = "JAVA"
        result = swap_case(input_str)
        self.assertEqual(result, "java")

    def test_swap_case_non_english(self):
        input_str = "¡Hola! Привет"
        result = swap_case(input_str)
        self.assertEqual(result, "¡hOLA! пРИВЕТ")  # Non-English letters should swap cases correctly

    def test_swap_case_empty_string(self):
        input_str = ""
        result = swap_case(input_str)
        self.assertEqual(result, "")  # Empty string should return empty

    # Run the tests
    if __name__ == '__main__':
        unittest.main()

    # Part 3

    import unittest
    from lab6 import str_translate  # Ensure str_translate is correctly imported

class TestStrTranslate(unittest.TestCase):
    def test_str_translate_basic(self):
        input_str = "abcdcba"
        result = str_translate(input_str, 'a', 'x')
        self.assertEqual(result, "xbcdcbx")  # Each 'a' is replaced by 'x'

    def test_str_translate_no_replacement(self):
        input_str = "hello world"
        result = str_translate(input_str, 'z', 'x')
        self.assertEqual(result, "hello world")  # No 'z' in the string, so no change

    def test_str_translate_replace_spaces(self):
        input_str = "hello world"
        result = str_translate(input_str, ' ', '_')
        self.assertEqual(result, "hello_world")  # Replaces space with underscore

    def test_str_translate_empty_string(self):
        input_str = ""
        result = str_translate(input_str, 'a', 'x')
        self.assertEqual(result, "")  # Empty string remains empty

    # Run the tests
    if __name__ == '__main__':
        unittest.main()

    # Part 4

import unittest
from lab6 import histogram  # Ensure histogram is correctly imported

class TestHistogram(unittest.TestCase):
    def test_histogram_basic(self):
        text = "apple banana apple orange banana apple"
        result = histogram(text)
        expected = {"apple": 3, "banana": 2, "orange": 1}
        self.assertEqual(result, expected)

    def test_histogram_single_word(self):
        text = "apple apple apple"
        result = histogram(text)
        expected = {"apple": 3}  # Only one word, repeated 3 times
        self.assertEqual(result, expected)

    def test_histogram_empty_string(self):
        text = ""
        result = histogram(text)
        expected = {}  # Empty string should return an empty dictionary
        self.assertEqual(result, expected)

    def test_histogram_mixed_case(self):
        text = "Apple apple Banana banana"
        result = histogram(text)
        expected = {"Apple": 1, "apple": 1, "Banana": 1, "banana": 1}  # Case-sensitive
        self.assertEqual(result, expected)

# Run the tests
if __name__ == '__main__':
    unittest.main()





if __name__ == '__main__':
    unittest.main()
