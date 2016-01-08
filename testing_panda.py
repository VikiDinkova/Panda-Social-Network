import unittest
from panda import Panda


class TestPanda(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda('Ivo', 'ivo@pandamail.com', 'male')

    def test_str(self):
        self.assertEqual(str(self.ivo), "Ivo")

    def test_eq(self):
        rado = Panda('rado', 'rado@pandamail.com', 'male')
        rado2 = Panda('Ivo', 'ivo@pandamail.com', 'male')
        self.assertFalse(self.ivo == rado)
        self.assertTrue(self.ivo == rado2)

    def test_name(self):
        self.assertEqual(self.ivo.name(), 'Ivo')

    def test_email(self):
        self.assertEqual(self.ivo.email(), 'ivo@pandamail.com')

    def test_gender(self):
        self.assertEqual(self.ivo.gender(), 'male')

    def test_is_male(self):
        self.assertTrue(self.ivo.isMale())

    def test_is_female(self):
        self.assertFalse(self.ivo.isFemale())


if __name__ == '__main__':
    unittest.main()
