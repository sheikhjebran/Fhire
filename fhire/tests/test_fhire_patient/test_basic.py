import unittest
from fhire.classes.fhire import Fhire


from fhire.exceptions import FhireError


# noinspection PyStatementEffect
class TestIsBasicChecks(unittest.TestCase):

    def test_is_none_pass(self):
        self.assertIsInstance(Fhire(None).is_none(), Fhire)

    def test_is_none_fail(self):
        with self.assertRaises(FhireError):
            Fhire("I am not none").is_none()

    def test_is_not_none_pass(self):
        self.assertIsInstance(Fhire("I am not none").is_not_none(), Fhire)

    def test_is_not_none_fail(self):
        with self.assertRaises(FhireError):
            Fhire(None).is_not_none()
