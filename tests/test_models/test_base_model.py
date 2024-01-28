
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)


from models.base_model import BaseModel

import unittest

class test_BaseModel(unittest.TestCase):

  def test_save(self):
      b = BaseModel()
      b.save()

  def test_to_dict(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

#   def test_split(self):
#       s = 'hello world'
#       self.assertEqual(s.split(), ['hello', 'world'])
#       # check that s.split fails when the separator is not a string
#       with self.assertRaises(TypeError):
#           s.split(2)

if __name__ == '__main__':
    unittest.main()





