import os
import yaml

from common.utils.helpers import Singleton


class Locator(metaclass=Singleton):
    def __init__(self, name):
        self._data = {}
        self._name = name
        self._c = 0

        filename = os.path.join(os.path.relpath('locators'), name + '.yml')
        assert os.path.isfile(filename), f'not found file in {filename}'

        with open(filename, 'r') as stream:
            try:
                self._data = yaml.safe_load(stream)['crawler']
            except yaml.YAMLError as exc:
                print(exc)
 
        self._url = self._data['site']
    
    @property
    def url(self):
        return self._url

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            element = self._data['locators'][self._c]
        except IndexError:
            self._c = 0
            raise StopIteration
        self._c += 1
        return element

    def __getitem__(self, key):
        value = None
        if isinstance(key, str):
            try:
                value = [value['value'] for value in self._data['locators'] \
                            if key in value['locator']][0]
            except IndexError:
                raise TypeError(f"invalid locator '{str(key)}'")
            return value
        raise TypeError(f"invalid locator '{str(key)}'")