import sys

from models.review import Review
from models.base_model import BaseModel
import unittest


class test_Review(unittest.TestCase):
    def test_save(self):
        u = Review()
        u.save()


if __name__ == '__main__':
    unittest.main()
