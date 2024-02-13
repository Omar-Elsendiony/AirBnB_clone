from models.state import State
from models.base_model import BaseModel
import unittest


class test_State(unittest.TestCase):
    def test_name(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_save(self):
            u = State()
            u.save()

    def test_to_dict(self):
        u = State()
        d = u.to_dict()
        self.assertIsInstance(d, dict)

if __name__ == '__main__':
    unittest.main()
