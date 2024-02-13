import sys

from models.state import State
from models.base_model import BaseModel
import unittest


class test_State(unittest.TestCase):
    def test_save(self):
        u = State()
        u.save()


if __name__ == '__main__':
    unittest.main()
