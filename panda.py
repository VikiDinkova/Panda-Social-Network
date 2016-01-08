    class Panda:
    def __init__(self, name, email, gender):
        if not Panda._check_email(email):
            assert (self._check_email(email) is False)
            email = input("wrong email\nemail:")
        self._name = name
        self._email = email
        self._gender = gender

    @staticmethod
    def _check_email(stri):
        return "@pandamail.com" in stri

    def __str__(self):
        return self._name

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self._name == other._name and self._email == other._email and self._gender == other._gender

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self._gender == "male"

    def isFemale(self):
        return self._gender == "female"


def main():
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    print(ivo.name())
    print(ivo.email())
    print(ivo.gender())
    print(ivo.isMale())
    print(ivo.isFemale())

if __name__ == '__main__':
    main()
