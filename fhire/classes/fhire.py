import importlib
import inspect
import pkgutil

from ..exceptions import FhireError


class Fhire:
    FHIRE_PACKAGE = 'fhire.fhire_action'

    def _import_fhire_modules(self):
        ass = importlib.import_module(Fhire.FHIRE_PACKAGE)
        fhire_modules = []
        for _1, module_name, _2 in pkgutil.iter_modules(ass.__path__):
            fhire_modules.append(importlib.import_module(
                ass.__name__ + '.' + module_name))
        return fhire_modules

    def __new__(cls, *args, **kwargs):
        # retrieve all modules in fhire package
        fhire_modules = cls._import_fhire_modules(cls)
        # bind fhire object instance with fhire functions from fhire modules
        instance = super(Fhire, cls).__new__(cls)
        for module in fhire_modules:
            for item in inspect.getmembers(module, inspect.isfunction):
                func_name = item[0]
                func = item[1]
                bound_method = func.__get__(instance, instance.__class__)
                setattr(instance, func_name, bound_method)
        return instance

    def __init__(self, value):
        self._val = value

    @property
    def value(self):
        return self._val

    # Basic check

    def is_none(self):
        try:
            assert self._val is None
            return self
        except AssertionError:
            raise FhireError('{} is not None'.format(self._val))

    def is_not_none(self):
        try:
            assert self._val is not None
            return self
        except AssertionError:
            raise FhireError('{} is None'.format(self._val))
