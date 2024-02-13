import sys

from models.review import Review
from models.base_model import BaseModel
import unittest


class test_Review(unittest.TestCase):
    def test_save(self):
        u = Review()
        u.save()

    def test_place_id(self):
        u = Review()
        n = u.place_id
        self.assertIsInstance(n, str)

    def test_user_id(self):
        u = Review()
        n = u.user_id
        self.assertIsInstance(n, str)

    def test_text(self):
        u = Review()
        n = u.text
        self.assertIsInstance(n, str)

if __name__ == '__main__':
    unittest.main()
