import unittest
import os
import csv
from src.validator import Validator

class ValidatorTests(unittest.TestCase):

    def setUp(self):
        script_dir = os.path.dirname(__file__)
        rel_path = 'data\\postcodes.csv'
        self.abs_file_path = os.path.join(script_dir, rel_path)

    def test_validator(self):
        validator = Validator()
        valid = validator.validate('23324')
        self.assertFalse(valid)
        valid = validator.validate('dfgdf')
        self.assertFalse(valid)

        with open(self.abs_file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            index = 0
            for row in reader:
                index = index + 1
                #skip title row and only check in use postcodes
                if index > 1 and row[1] == "Yes":
                    valid = validator.validate(row[0])
                    self.assertTrue(valid)                               

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(exit=False)
