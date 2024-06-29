#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_fahrenheit
from src.question_b.question_b import get_person_category
from src.question_c.question_c import get_assessment_value
from src.question_c.question_c import get_tax_assessed
from src.question_d.question_d import use_local_variable

class Test_Config(unittest.TestCase):

    def test_get_fahrenheit(self):
        self.assertEqual(32, get_fahrenheit(0))
    def test_get_fahrenheit(self):
        self.assertEqual(41, get_fahrenheit(5))
    def test_get_fahrenheit(self):
        self.assertEqual(50, get_fahrenheit(10))
    def test_get_person_category(self):
        self.assertEqual("Infant", get_person_category(1))
    def test_get_person_category(self):
        self.assertEqual("Child", get_person_category(2))
    def test_get_person_category(self):
        self.assertEqual("Teenager", get_person_category(14))
    def test_get_person_category(self):
        self.assertEqual("Adult", get_person_category(20))
    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
    def test_get_assessment_value(self):
        self.assertEqual(12000, get_assessment_value(20000))
    def test_get_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
    def test_get_get_tax_assessed(self):
        self.assertEqual(72, get_tax_assessed(10000))
    def test_use_local_variable(self):
        self.assertEqual(72, get_tax_assessed(10000))
    def test_use_local_variable(self):
        num = (100)
        use_local_variable(num)
        self.assertEqual(num,100)