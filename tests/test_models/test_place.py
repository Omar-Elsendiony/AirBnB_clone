import sys

from models.place import Place
from models.base_model import BaseModel
import unittest


class test_Place(unittest.TestCase):
    def test_save(self):
        u = Place()
        u.save()

    def test_name(self):
        u = Place()
        f = u.name
        self.assertIsInstance(f, str)

    def test_city_id(self):
        u = Place()
        n = u.city_id
        self.assertIsInstance(n, str)

    def test_user_id(self):
        u = Place()
        n = u.user_id
        self.assertIsInstance(n, str)

    def test_description(self):
        u = Place()
        e = u.description
        self.assertIsInstance(e, str)

if __name__ == '__main__':
    unittest.main()
