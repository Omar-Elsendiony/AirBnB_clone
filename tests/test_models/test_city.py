import sys

from models.city import City
from models.base_model import BaseModel
import unittest


class test_City(unittest.TestCase):
    def test_name(self):
        u = City()
        n = u.name
        self.assertIsInstance(n, str)

    def test_state_id(self):
        u = City()
        s = u.state_id
        self.assertIsInstance(s, str)

if __name__ == '__main__':
    unittest.main()
