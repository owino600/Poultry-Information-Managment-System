#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.medication_operations import Medication

class TestMedication(unittest.TestCase):
    def setUp(self):
        self.medication = Medication(poultry_id='1', species='Chicken', quantity=5, ageweeks=20, dateofmedication=datetime.utcnow(), madecationname='Antibiotics', dosage='50mg', medicationtype='Oral', withdrawalperiod='2 weeks', supplier='Local Farm', cost=200)

    def test_attributes(self):
        self.assertEqual(self.medication.poultry_id, '1')
        self.assertEqual(self.medication.species, 'Chicken')
        self.assertEqual(self.medication.quantity, 5)
        self.assertEqual(self.medication.ageweeks, 20)
        self.assertEqual(self.medication.madecationname, 'Antibiotics')
        self.assertEqual(self.medication.dosage, '50mg')
        self.assertEqual(self.medication.medicationtype, 'Oral')
        self.assertEqual(self.medication.withdrawalperiod, '2 weeks')
        self.assertEqual(self.medication.supplier, 'Local Farm')
        self.assertEqual(self.medication.cost, 200)

if __name__ == '__main__':
    unittest.main()