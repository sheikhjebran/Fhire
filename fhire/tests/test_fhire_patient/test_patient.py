import unittest
from fhire.classes.fhire import Fhire


class TestPatientGetResponse(unittest.TestCase):

    def test_get_patient_response(self):
        Fhire("").parse_https_post_patient_response