import unittest
from name_function import get_formatted_name


class NamesTestCases(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("hussein", "elhawary")
        self.assertEqual(formatted_name, "Hussein Elhawary")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("hussein", "elhawary", "abdel-moamen")
        self.assertEqual(formatted_name, "Hussein Abdel-Moamen Elhawary")


if __name__ == '__main__':
    unittest.main()