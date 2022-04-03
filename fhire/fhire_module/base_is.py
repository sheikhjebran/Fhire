from typing import Any


class IsBase:
    __base = None

    def __init__(self, object_under_test: Any):
        self.object = object_under_test

    def __call__(self, *args, **kwargs):
        return self

    @property
    def base(self):
        if not IsBase.__base:
            from ..classes.base import Base
            IsBase.__base = Base

        return IsBase.__base(self.object)
