import json
from ..exceptions import FhireError
from fhire.fhire_pojo.procedure.get_procedure import get_procedure_from_dict
from fhire.fhire_pojo.procedure.post_procedure import post_procedure_from_dict


def parse_https_get_observation_response(check_obj):
    try:
        return get_procedure_from_dict(json.loads(check_obj._val))
    except AssertionError as e:
        raise FhireError(
            '{} Invalid response given to parse'.format(check_obj._val)) from e


def parse_https_post_observation_response(check_obj):
    try:
        return post_procedure_from_dict(json.loads(check_obj._val))
    except AssertionError as e:
        raise FhireError(
            '{} Invalid response given to parse'.format(check_obj._val)) from e
