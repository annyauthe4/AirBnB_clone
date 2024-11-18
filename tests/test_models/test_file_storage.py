import unittest
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit test for the BaseModel class"""
