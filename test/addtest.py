import unittest
import xmlrunner
from code.addnumbers import AddNumbers


class RunAddTest(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(12, 8 + 4)

    def test_fail(self):
        self.assertNotEqual(12, 8 + 3)

    def test_add_pass(self):
        self.assertEqual(AddNumbers().add_numbers(2), 12)

    def test_add_fail(self):
        self.assertNotEqual(AddNumbers().add_numbers(2), 11)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
