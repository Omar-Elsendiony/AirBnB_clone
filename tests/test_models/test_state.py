import sys

from models.state import State
from models.base_model import BaseModel
import unittest


class test_State(unittest.TestCase):
    def test_name(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name,"California")



if __name__ == '__main__':
    unittest.main()
