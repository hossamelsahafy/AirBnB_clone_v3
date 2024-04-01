#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    def setUp(self):
        """Set up for each test"""
        self.db_storage = DBStorage()
        self.model = BaseModel()
        self.model.save()


class TestStorageMethods(unittest.TestCase):
    """Test Class"""

    def setUp(self):
        """Set up test environment."""
        self.storage = storage
        self.first_state_id = list(self.storage.all(State).values())[0].id
        self.user_id = "user_123"  # Replace with a known user ID

    def test_count_all(self):
        """Test counting all objects."""
        expected_count = 992
        actual_count = self.storage.count()
        self.assertEqual(actual_count, expected_count)

    # Additional more test cases

    def test_get_user(self):
        user = self.storage.get(User, self.user_id)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, self.user_id)

    def test_count_users(self):
        expected_user_count = 15
        actual_user_count = self.storage.count(User)
        self.assertEqual(actual_user_count, expected_user_count)

    def test_get_unsupported_class(self):
        # Replace UnsupportedClass with a non-supported class
        obj = self.storage.get(UnsupportedClass, 123)
        self.assertIsNone(obj)

    def test_count_non_existent_class(self):
        with self.assertRaises(AttributeError):
            # Replace with a non-existent class
            self.storage.count(NonExistentClass)

    def test_get_non_existent_object(self):
        obj = self.storage.get(State, "non-existent-id")
        self.assertIsNone(obj)

    def test_count_all_objects(self):
        expected_count = 50  # Adjust with the expected total count of all objects
        actual_count = self.storage.count()
        self.assertEqual(actual_count, expected_count)
    def test_invalid_connection_string(self):
        with self.assertRaises(SpecificException):
        storage = DBStorage("invalid_connection_string")

# Edge Cases - Large Dataset

def test_large_dataset_performance(self):
    # Generate a large number of objects (adjust count as needed)
    for _ in range(1000):
        obj = State()
        self.db_storage.new(obj)  # Assuming DBStorage.new() creates database records

    start_time = time.time()
    self.db_storage.all()
    elapsed_time = time.time() - start_time

# Assert that execution time is within acceptable limits

# Database Interaction

def test_create_record(self):
    new_state = State(name="New State")
    self.db_storage.new(new_state)
    self.db_storage.save()

    # Query the database to verify record creation (implementation depends on your database)

    db_state = # Query to retrieve the newly created state

    self.assertEqual(db_state.name, new_state.name)

# Filtering (assuming DBStorage supports filtering)

def test_filter_by_state_name(self):
    filtered_objects = self.db_storage.all(State, name="California")
