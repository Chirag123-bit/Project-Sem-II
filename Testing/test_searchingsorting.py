import unittest
import Backend.SearchingSorting


class Test_Grades(unittest.TestCase):
    """This class will perform unit testing on SearchingSorting module.
        Through this class, it is ensured that our program is able
        to perform all searching and soring operations"""
    def setUp(self):
        self.s = Backend.SearchingSorting.sorting()
        self.so = Backend.SearchingSorting.searching()
        self.lst = [('Tshering', 'Bcd'), ("Bimal", "Def"), ('Chirag', 'Abc')]

    def test_linear_search(self):
        index = 0
        item = "Chirag"
        expected_result = "Chirag"
        result = self.so.linear_search(self.lst, index, item)
        actual_result = result[0][0]  # index 0 = First Name
        self.assertEqual(expected_result, actual_result)  # Test Passed

    def test_insertion_sort(self):
        expected_result = [("Bimal", "Def"), ('Chirag', 'Abc'), ('Tshering', 'Bcd')]
        actual_result = self.s.insertion_sort(self.lst, 0)  # Sorting using First Name
        self.assertEqual(expected_result, actual_result)  # Test Passed

        expected_result = [('Chirag', 'Abc'), ('Tshering', 'Bcd'),("Bimal", "Def")]
        actual_result = self.s.insertion_sort(self.lst, 1)  # Sorting using Last Name
        self.assertEqual(expected_result, actual_result)  # Test Passed

    def tearDown(self):
        del self.s
        del self.so
