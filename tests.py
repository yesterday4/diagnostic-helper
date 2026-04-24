import unittest
from ui import Display, ValidationError
from diagnostic_engine import DiagnosticEngine
from problem import SafetyCriticalProblem

# "python -m unittest tests -v" for launching tests

class TestValidateChoice(unittest.TestCase):
    def setUp(self):
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

class TestValidateAnswer(unittest.TestCase):
    def setUp(self):
        diag_engine = DiagnosticEngine([])
        self.display = Display([], diag_engine)

    def test_valid_answer_1(self):
        result = self.display.validate_answer("y")
        self.assertEqual(result, "y")

    def test_valid_answer_2(self):
        result = self.display.validate_answer("n")
        self.assertEqual(result, "n")

    def test_number_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_answer("1")

    def test_wrong_letter_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_answer("a")

    def test_more_than_one_letter_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_answer("yn")

    def test_capital_letter_raises_error(self):
        with self.assertRaises(ValidationError):
            self.display.validate_answer("Y")

class TestDiagnose(unittest.TestCase):
    def setUp(self):
        self.problem_1 = SafetyCriticalProblem(1, "problem_1", "a", "high", 0.1, [1, 2, 3], [])
        self.problem_2 = SafetyCriticalProblem(2, "problem_2", "b", "low", 0.1, [4, 5, 6], [])
        self.diag_engine = DiagnosticEngine([self.problem_1, self.problem_2])

    def test_diagnose_based_on_matching_ids_1(self):
        result = self.diag_engine.diagnose([1, 2, 3])
        self.assertEqual(result[0][0], self.problem_1)
        self.assertAlmostEqual(result[0][1], 0.1*1)

    def test_diagnose_based_on_matching_ids_2(self):
        result = self.diag_engine.diagnose([4, 5, 6])
        self.assertEqual(result[0][0], self.problem_2)
        self.assertAlmostEqual(result[0][1], 0.1*1)

    def test_diagnose_choosing_the_correct_problem_1(self):
        result = self.diag_engine.diagnose([3, 5, 6])
        self.assertEqual(result[0][0], self.problem_2)
        self.assertAlmostEqual(result[0][1], 0.1*(2/3))

    def test_diagnose_choosing_the_correct_problem_2(self):
        result = self.diag_engine.diagnose([2, 3, 4])
        self.assertEqual(result[0][0], self.problem_1)
        self.assertAlmostEqual(result[0][1], 0.1*(2/3))

    def test_diagnose_no_matching_problems(self):
        result = self.diag_engine.diagnose([7, 8, 9])
        self.assertEqual(result, [])

    def test_diagnose_no_input_ids(self):
        result = self.diag_engine.diagnose([])
        self.assertEqual(result, [])