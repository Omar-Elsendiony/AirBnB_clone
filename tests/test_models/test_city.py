import sys

from models.city import City
from models.base_model import BaseModel
import unittest


class test_City(unittest.TestCase):
    def test_name(self):
        u = City()
        u.name = None
        self.assertNotIsInstance(u.name, str)

    def test_state_id(self):
        u = City()
        u.state_id = None
        self.assertNotIsInstance(u.state_id, str)

if __name__ == '__main__':
    unittest.main()
