import unittest
from unittest.mock import patch
from to_test import Employee


class TestEmployee(unittest.TestCase):


    def test_raise_salary(self):
        emp = Employee('Vladimir', 'Putin', 10000)
        emp.raise_salary()
        self.assertEqual(emp.salary, 11000)

    def test_form_email(self):
        emp = Employee('A', 'B', 100)
        
    def test_scedule(self):
        emp1 = Employee('Boris', 'Eltsyn', 1)
        with patch("to_test.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Very good response"

            scedule = emp1.scedule()
            mocked_get.assert_called_with("http://netcracker.com/scedule/Eltsyn")
            self.assertEqual(scedule, "Very good response")
    

