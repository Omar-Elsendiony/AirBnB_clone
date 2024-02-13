from models.user import User
import unittest


class test_User(unittest.TestCase):
    def test_save(self):
        b = User()
        b.save()

    def test_to_dict(self):
        b = User()
        d = b.to_dict()
        self.assertIsInstance(d, dict)


if __name__ == '__main__':
    unittest.main()
