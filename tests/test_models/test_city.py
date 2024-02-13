import sys

from models.city import City
from models.base_model import BaseModel
import unittest


class test_City(unittest.TestCase):
    def test_save(self):
        u = City()
        u.save()


if __name__ == '__main__':
    unittest.main()
