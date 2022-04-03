import json
from fhire.exceptions import FhireError
from fhire.fhire_pojo.patient.create_patient_response import create_patient_response_from_dict
from fhire.fhire_pojo.patient.get_patient_response import get_patient_response_from_dict


def parse_https_get_patient_response(check_obj):
    try:
        return get_patient_response_from_dict(json.loads(check_obj._val))
    except AssertionError as e:
        raise FhireError(
            '{} Invalid response given to parse'.format(check_obj._val)) from e


def parse_https_post_patient_response(check_obj):
    try:
        return create_patient_response_from_dict(json.loads(check_obj._val))
    except AssertionError as e:
        raise FhireError(
            '{} Invalid response given to parse'.format(check_obj._val)) from e
