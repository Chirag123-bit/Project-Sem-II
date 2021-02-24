import unittest
import Backend.DBConnect

class Test_DBConnect(unittest.TestCase):
    def setUp(self):
        self.db = Backend.DBConnect.DBConnect()

    def test_select(self):
        query = "select * from user_info"
        row = self.db.select(query)
        self.assertIsNotNone(row) #Test Passed

        query2 = "select * from grades"
        row = self.db.select(query2)
        self.assertIsNotNone(row)  # Test Passed

        query3 = 123
        self.assertRaises(TypeError,self.db.select,query3)  # Test Passed


    def test_update(self):
        query = 12344
        values = ["Chirag","123"]
        self.assertRaises(TypeError,self.db.update,query,values)  # Test Passed


    def test_delete(self):
        query = 10
        values = ["Chirag"]
        self.assertRaises(TypeError,self.db.delete,query,values)  # Test Passed


    def tearDown(self):
        del self.db




