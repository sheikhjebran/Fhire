from fhire.fhire_module.base_is import IsBase


class __Patient(IsBase):

    @property
    def parse_https_get_patient_response(self) -> "Fhire":
        self.base.parse_https_get_patient_response()
        return self

    @property
    def parse_https_post_patient_response(self) -> "Fhire":
        self.base.parse_https_post_patient_response()
        return self
