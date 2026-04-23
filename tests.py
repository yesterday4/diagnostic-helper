import unittest
from ui import Display, ValidationError

# python -m unittest tests -v

class TestValidateChoice(unittest.TestCase):
    def setUp(self):
        from diagnostic_engine import DiagnosticEngine
        diag_engine = DiagnosticEngine([])
        self.display = Display([], diag_engine)


    def test_valid_choice(self):
        result = self.display.validate_choice(2, ["a", "b", "c"])
        self.assertEqual(result, 2)

    def test_0_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_choice(0, ["a", "b", "c"])

    def test_negative_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_choice(-1, ["a", "b", "c"])

    def test_too_high_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_choice(4, ["a", "b", "c"])
    