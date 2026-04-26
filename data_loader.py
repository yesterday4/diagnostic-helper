import json
from symptom import Symptom
from problem import ProblemFactory

class Loader:
    def __init__(self):
        self.problem_factory = ProblemFactory()
        with open('symptoms_problems.json', 'r') as f:
            self.d = json.load(f)

    def load_symptoms(self):
        symptoms = []
        for symptom in self.d["symptoms"]:
            s = Symptom(symptom["id"], symptom["description"], symptom["categories"])
            symptoms.append(s)
        return symptoms
    
    def load_problems(self):
        problems = []
        for problem in self.d["problems"]:
            p = self.problem_factory.create_problem(problem)
            problems.append(p)
        return problems