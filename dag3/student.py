from person import Person


class Student(Person):

    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self._subject = subject

    def get_subject(self):
        return self._subject

    def describe(self):
        return "Elev " + self.get_full_name() + " er tilføjet til fag " + self._subject

    def to_row(self):
        return ["student", self._first_name, self._last_name, self._subject]
