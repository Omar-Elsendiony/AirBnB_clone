import sys

from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase):
    def test_save(self):
        u = Amenity()
        u.save()

    def test_name(self):
        u = Amenity()
        u.save()


if __name__ == '__main__':
    unittest.main()
