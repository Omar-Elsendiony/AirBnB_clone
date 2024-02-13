from models.state import State
import unittest


class test_State(unittest.TestCase):
    def test_name(self):
        state = State()
        n = state.name
        self.assertIsInstance(n, str)

    def test_save(self):
        u = State()
        u.save()

    def test_to_dict(self):
        u = State()
        d = u.to_dict()
        self.assertIsInstance(d, dict)
    
    def test_update(self):
        s = State()
        print(s)
        # self.assertIn("name", State.name)
        

if __name__ == '__main__':
    unittest.main()
