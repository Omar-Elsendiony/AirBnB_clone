import sys
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class test_FileStorage(unittest.TestCase):
    def test_save(self):
        b = BaseModel()
        b.save()

    def test_reload(self):
        fs = FileStorage()
        ids = []
        objs_by_id = {}
        for i in range(10):
            bm = BaseModel()
            fs.new(bm)
            bm.save()
            ids.append(bm.id)
            objs_by_id[bm.id] = bm
    def test_file_path():
        fs = FileStorage()
        fs.__file_path = None
    


if __name__ == '__main__':
    unittest.main()
