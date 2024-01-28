import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current)
path = os.path.abspath(current + "/engine/")
sys.path.append(path)
from engine.file_storage import FileStorage


storage = FileStorage("file.json")
storage.reload()
