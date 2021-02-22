import unittest
import Backend.SearchingSorting


class Test_Grades(unittest.TestCase):
    def setUp(self):
        self.s = Backend.SearchingSorting.sorting()
        self.so = Backend.SearchingSorting.searching()

    def test_insertion_sort(self):
        lst = [('Tshering', 'Rai', 'abc@gmail.com', '123', '123'),
               ('Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '123', 'Chirag')]

        expected_result = [('Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '123', 'Chirag'),
                           ('Tshering', 'Rai', 'abc@gmail.com', '123', '123')]
        actual_result = self.s.insertion_sort(lst, 0)  # Sorting using First Name
        self.assertEqual(expected_result, actual_result)

        lst = [('Tshering', 'Zai', 'abc@gmail.com', '123', '123'),
               ('Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '123', 'Chirag')]

        expected_result = [('Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '123', 'Chirag'),
                           ('Tshering', 'Zai', 'abc@gmail.com', '123', '123')]
        actual_result = self.s.insertion_sort(lst, 1)  # Sorting using Last Name
        self.assertEqual(expected_result, actual_result)


    def test_binary_search(self):
        lst = [('Tshering', 'Rai', 'abc@gmail.com', '123', '123'),
               ('Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '123', 'Chirag')]
        index = 0
        item = "Chirag"
        expected_result = "Chirag"
        actual_result = (self.so.binary_search(lst,index,item))[0][0]
        self.assertEqual(expected_result,actual_result)
