import unittest
import model.User


class Test_User(unittest.TestCase):
    def setUp(self):
        self.u=model.User.User()

    def test_set_fname(self):
        self.u.set_fname("Chirag")
        self.assertEqual("Chirag",self.u.get_fname())   # Test Passed
        self.u.set_fname("Bimal")
        self.assertEqual("Bimal", self.u.get_fname())   # Test Passed



    def test_set_uname(self):
        self.u.set_uname("Chirag123")
        self.assertEqual("Chirag123", self.u.get_uname())   # Test Passed
        self.u.set_uname("Bimal001")
        self.assertEqual("Bimal001", self.u.get_uname())   # Test Passed

    def test_set_passwd(self):
        self.u.set_passwd("12345678")
        self.assertEqual("12345678",self.u.get_passwd())   # Test Passed
        self.u.set_passwd("ABC@DEFGH")
        self.assertEqual("ABC@DEFGH", self.u.get_passwd())   # Test Passed