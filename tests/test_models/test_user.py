import sys

from models.user import User
from models.base_model import BaseModel
import unittest


class test_User(unittest.TestCase):
    def test_save(self):
        u = User()
        u.save()

    def test_to_dict(self):
        u = User()
        d = u.to_dict()
        self.assertIsInstance(d, dict)
    
    def test_first_name(self):
        u = User()
        f = u.first_name
        self.assertIsInstance(f, str)

    def test_last_name(self):
        u = User()
        n = u.last_name
        self.assertIsInstance(n, str)

    def test_password(self):
        u = User()
        n = u.password
        self.assertIsInstance(n, str)

    def test_email(self):
        u = User()
        e = u.email
        self.assertIsInstance(e, str)

if __name__ == '__main__':
    unittest.main()
