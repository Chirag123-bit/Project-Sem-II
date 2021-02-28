import unittest
import model.user


class Test_User(unittest.TestCase):
    """This class will perform unit testing on user module.
        Through this class, it is ensured that our program is able
        to perform all CURD operations and filter any unwanted queries"""

    def setUp(self):
        self.u = model.user.User()

    def test_set_fname(self):
        self.u.set_fname("Chirag")
        self.assertEqual("Chirag", self.u.get_fname())  # Test Passed
        self.u.set_fname("Bimal")
        self.assertEqual("Bimal", self.u.get_fname())  # Test Passed

    def test_set_uname(self):
        self.u.set_uname("Chirag123")
        self.assertEqual("Chirag123", self.u.get_uname())  # Test Passed
        self.u.set_uname("Bimal001")
        self.assertEqual("Bimal001", self.u.get_uname())  # Test Passed

    def test_set_passwd(self):
        self.u.set_passwd("12345678")
        self.assertEqual("12345678", self.u.get_passwd())  # Test Passed
        self.u.set_passwd("ABC@DEFGH")
        self.assertEqual("ABC@DEFGH", self.u.get_passwd())  # Test Passed

    def test_set_dob(self):
        self.assertRaises(TypeError, self.u.set_dob, 2010)  # Test Passed
        self.u.set_dob("2010-01-01")
        self.assertEqual("2010-01-01", self.u.get_dob())  # Test Passed

    def tearDown(self):
        del self.u
