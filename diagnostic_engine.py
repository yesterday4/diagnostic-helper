class DiagnosticEngine:
    def __init__(self, problems):
        self.problems = problems
        
    @property
    def problems(self):
        return self._problems

    @problems.setter
    def problems(self, value):
        if not isinstance(value, list):
            raise TypeError("problems must be an list")
        self._problems = value

    def diagnose(self, symptoms_input):
        
        results = []
        for problem in self.problems:
            matching_ids = []
            for value in symptoms_input:
                if value in problem.symptom_ids:
                    matching_ids.append(value)
            
            match_score = len(matching_ids) / len(problem.symptom_ids)
            final_score = problem.b_probability * match_score

            if matching_ids:
                result = (problem, final_score)
                results.append(result)
        
        results_final = sorted(results, key = lambda x: x[1], reverse = True)
        return results_final