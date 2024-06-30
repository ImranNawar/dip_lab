import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do name like 'Imran Nawar' work?"""

        formatted_name = get_formatted_name('imran', 'nawar')
        self.assertEqual(formatted_name, "Imran Nawar")  # Compare the value in formatted_name to the string 'Janis Joplin'. If they are equal as expected, fine. But if they don’t match, let me know!

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()