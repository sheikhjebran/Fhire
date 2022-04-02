import unittest
from fhire.classes import Fhire
from fhire.exceptions import FhireError


class TestPatientGetResponse(unittest.TestCase):

    def test_get_patient_response(self):
        patient = Fhire('test').parse_https_get_patient_list_response()
        print(patient)
