from enum import Enum

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Symptom:
    def __init__(self, id, description, categories):
        self.id = id
        self.description = description
        self.categories = categories

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be an integer")
        self._id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be a string")
        self._description = value

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if not isinstance(value, list):
            raise TypeError("categories must be a list")
        self._categories = value

class Problem:
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