#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.medication_operations import Medication
from models.inventory import Inventory

class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    def setUp(self):
        """Setup for each test"""
        self.storage = storage.DBStorage()

    def tearDown(self):
        """Cleanup after each test"""
        self.storage.close()

    def test_all(self):
        """Test the 'all' method"""
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)

    def test_new(self):
        """Test the 'new' method"""
        obj = BaseModel()
        self.storage.new(obj)
        objs = self.storage.all()
        self.assertIn(obj, objs.values())

    def test_save(self):
        """Test the 'save' method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        objs = self.storage.all()
        self.assertIn(obj, objs.values())

    def test_delete(self):
        """Test the 'delete' method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.delete(obj)
        objs = self.storage.all()
        self.assertNotIn(obj, objs.values())

    def test_reload(self):
        """Test the 'reload' method"""
        # This test will depend on your specific implementation

    def test_get(self):
        """Test the 'get' method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        retrieved_obj = self.storage.get(BaseModel, obj.id)
        self.assertEqual(obj, retrieved_obj)

if __name__ == "__main__":
    unittest.main()