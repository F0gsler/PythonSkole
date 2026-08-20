from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return self._first_name + " " + self._last_name

    @abstractmethod
    def describe(self):
        pass
