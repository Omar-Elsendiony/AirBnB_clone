
import sys
import os
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# parent = os.path.dirname(parent)
# sys.path.append(parent)


from models.base_model import BaseModel

import unittest

class test_BaseModel(unittest.TestCase):

  def test_save(self):
      b = BaseModel()
      b.save()

  def test_to_dict(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertIsInstance(d, dict)



if __name__ == '__main__':
    unittest.main()





