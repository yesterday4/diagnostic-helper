import json
from classes import Symptom, Problem

class Loader:
    def __init__(self):
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
            p = Problem(problem["id"], problem["name"], problem["category"], problem["severity"], problem["base_probability"], problem["symptom_ids"], problem["diagnostic_steps"])
            problems.append(p)
        return problems