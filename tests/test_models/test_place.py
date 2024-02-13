import sys

from models.place import Place
from models.base_model import BaseModel
import unittest


class test_Place(unittest.TestCase):
    def test_save(self):
        u = Place()
        u.save()


if __name__ == '__main__':
    unittest.main()
