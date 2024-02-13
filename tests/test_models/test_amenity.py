import sys

from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase):
    def test_save(self):
        u = Amenity()
        u.save()

    def test_name(self):
        u = Amenity()
        n = u.name
        self.assertIsInstance(n, str)


if __name__ == '__main__':
    unittest.main()
