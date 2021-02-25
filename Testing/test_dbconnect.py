import unittest
import Backend.DBConnect


class Test_DBConnect(unittest.TestCase):
    """This class will perform unit testing on DBConnect module.
    Through this class, it is ensured that our program is able
    to perform all CURD operations and filter any unwanted queries"""

    def setUp(self):
        self.db = Backend.DBConnect.DBConnect()

    def test_select(self):
        query = "select * from user_info"
        row = self.db.select(query)
        self.assertIsNotNone(row)  # Test Passed

        query2 = "select * from grades"
        row = self.db.select(query2)
        self.assertIsNotNone(row)  # Test Passed

        query3 = 123
        self.assertRaises(TypeError, self.db.select, query3)  # Test Passed

    def test_update(self):
        query = 12344
        values = ["Chirag", "123"]
        self.assertRaises(TypeError, self.db.update, query, values)  # Test Passed
        query = "update user_info set FName = %s where UserName = %s"
        values = ["Churag", "Chirag"]
        self.db.update(query, values)
        query1 = "select FName from user_info where UserName = %s"
        value = ("Chirag",)
        val = self.db.select(query1, value)
        self.assertEqual("Churag", val[0][0])  # Test Passed

    def test_insert(self):
        query = "insert into user_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = ("Abc", "Def", "abc@gmail.com", "12345", "Abc", "02/02/21", 5, "A", "Mr.")
        self.db.insert(query, values)
        query = "select FName from user_info where UserName = %s"
        values = ("Abc",)
        val = self.db.select(query, values)
        self.assertEqual("Abc", val[0][0])  # Test Passed
        query = 12344
        values = ["Chirag", "123"]
        self.assertRaises(TypeError, self.db.insert, query, values)  # Test Passed

    def test_delete(self):
        query = 10
        values = ["Chirag"]
        self.assertRaises(TypeError, self.db.delete, query, values)  # Test Passed
        query = "delete from user_info where UserName = %s"
        values = ("Abc",)
        self.db.delete(query,values)
        query = "select * from user_info where UserName = %s"
        values = ("Abc",)
        row = self.db.select(query,values)
        self.assertListEqual([],row)  # Test Passed

    def tearDown(self):
        del self.db
