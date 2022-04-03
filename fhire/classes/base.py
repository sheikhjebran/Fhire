import importlib
import inspect
import pkgutil

from ..exceptions import FhireError


class Base:
    ASSERTIONS_PACKAGE = 'fhire.fhire_base'

    def _import_assertion_modules(self):
        ass = importlib.import_module(Base.ASSERTIONS_PACKAGE)
        assertion_modules = []
        for _1, module_name, _2 in pkgutil.iter_modules(ass.__path__):
            assertion_modules.append(importlib.import_module(
                ass.__name__ + '.' + module_name))
        return assertion_modules

    def __new__(cls, *args, **kwargs):
        # retrieve all modules in fhire_fhire_module package
        assertion_modules = cls._import_assertion_modules(cls)
        # bind fhire object instance with assertion functions from fhire_fhire_module modules
        instance = super(Base, cls).__new__(cls)
        for module in assertion_modules:
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
