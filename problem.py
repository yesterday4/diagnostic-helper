from enum import Enum
from abc import ABC, abstractmethod

class Severity(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


class ProblemType(Enum):
    MECHANICALLY_CRITICAL = "mechanically_critical"
    SAFETY_CRITICAL = "safety_critical"
    NON_CRITICAL = "non_critical"


class Problem(ABC):
    def __init__(self, id, name, category, severity, b_probability, symptom_ids, diag_steps):
        self.id = id
        self.name = name
        self.category = category
        self.severity = severity
        self.b_probability = b_probability
        self.symptom_ids = symptom_ids
        self.diag_steps = diag_steps

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self._name = value
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        self._category = value

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, value):
        if isinstance(value, Severity):
            self._severity = value
        elif isinstance(value, str):
            self._severity = Severity(value)
        else:
            raise TypeError("severity must be a string or Severity enum")
        
    @property
    def b_probability(self):
        return self._b_probability

    @b_probability.setter
    def b_probability(self, value):
        if not isinstance(value, float):
            raise TypeError("b_probability must be a float")
        self._b_probability = value

    @property
    def symptom_ids(self):
        return self._symptom_ids

    @symptom_ids.setter
    def symptom_ids(self, value):
        if not isinstance(value, list):
            raise TypeError("symptom_ids must be a list")
        self._symptom_ids = value

    @property
    def diag_steps(self):
        return self._diag_steps

    @diag_steps.setter
    def diag_steps(self, value):
        if not isinstance(value, list):
            raise TypeError("diag_steps must be a list")
        self._diag_steps = value

    @abstractmethod
    def get_warning(self):
        pass


class SafetyCriticalProblem(Problem):
    def get_warning(self):
        return "Further operation of the car could lead to serious injury or death!!!"


class MechanicallyCriticalProblem(Problem):
    def get_warning(self):
        return "Further operation of the car could lead to further damage!"


class NonCriticalProblem(Problem):
    def get_warning(self):
        return "Further operation of the car has no serious risks."


class ProblemFactory:
    def create_problem(self, data):
        problem_type = ProblemType(data["problem_type"])
        if problem_type == ProblemType.MECHANICALLY_CRITICAL:
            return MechanicallyCriticalProblem(
                data["id"],
                data["name"],
                data["category"],
                data["severity"],
                data["base_probability"],
                data["symptom_ids"],
                data["diagnostic_steps"])
        elif problem_type == ProblemType.SAFETY_CRITICAL:
            return SafetyCriticalProblem(
                data["id"],
                data["name"],
                data["category"],
                data["severity"],
                data["base_probability"],
                data["symptom_ids"],
                data["diagnostic_steps"])
        elif problem_type == ProblemType.NON_CRITICAL:
            return NonCriticalProblem(
                data["id"],
                data["name"],
                data["category"],
                data["severity"],
                data["base_probability"],
                data["symptom_ids"],
                data["diagnostic_steps"])
        else:
            raise ValueError(f"Unknown problem type: {problem_type}")
