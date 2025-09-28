from unittest import TestCase
from validator import Validator


class TestValidator(TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validni_heslo(self):
        self.assertTrue(self.validator.validuj_heslo("a1b2c3"), "Heslo 'a1b2c3' je platné.")

    def test_prilis_kratke_heslo(self):
        self.assertFalse(self.validator.validuj_heslo("a1b2"), "Heslo 'a1b2' je příliš krátké.")

    def test_heslo_bez_cisla(self):
        self.assertFalse(self.validator.validuj_heslo("abcdef"), "Heslo 'abcdef' neobsahuje číslo.")

    def test_prazdne_heslo(self):
        self.assertFalse(self.validator.validuj_heslo(""), "Prázdné heslo není platné.")

    def test_heslo_jen_cisla(self):
        self.assertTrue(self.validator.validuj_heslo("123456"), "Heslo '123456' je platné.")

