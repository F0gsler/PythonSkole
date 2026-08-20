from person import Person


class Teacher(Person):

    def __init__(self, first_name, last_name, subjects):
        super().__init__(first_name, last_name)
        self._subjects = subjects

    def get_subjects(self):
        return self._subjects

    def has_subject(self, subject):
        return subject in self._subjects

    def add_subject(self, subject):
        if subject not in self._subjects:
            self._subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self._subjects:
            self._subjects.remove(subject)

    def get_subjects_text(self):
        if len(self._subjects) == 0:
            return " - (ingen fag endnu)"
        text = ""
        for subject in self._subjects:
            text = text + " - " + subject + "\n"
        return text.rstrip("\n")

    def describe(self):
        return self.get_full_name() + " er tilmeldt følgende fag:\n" + self.get_subjects_text()

    def to_row(self):
        return ["teacher", self._first_name, self._last_name, "|".join(self._subjects)]
