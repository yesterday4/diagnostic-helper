from diagnostic_engine import DiagnosticEngine

class ValidationError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(message)

class Display:
    def __init__(self, symptoms, diagnostic_engine):
        self.symptoms = symptoms
        self.diagnostic_engine = diagnostic_engine

    @property
    def symptoms(self):
        return self._symptoms

    @symptoms.setter
    def symptoms(self, value):
        if not isinstance(value, list):
            raise TypeError("symptoms must be a list")
        self._symptoms = value

    @property
    def diagnostic_engine(self):
        return self._diagnostic_engine

    @diagnostic_engine.setter
    def diagnostic_engine(self, value):
        if not isinstance(value, DiagnosticEngine):
            raise TypeError("diagnostic_engine must be an DiagnosticEngine")
        self._diagnostic_engine = value

    def display_categories(self):
        categories = []
        for symptom in self.symptoms:
            for category in symptom.categories:
                if category not in categories:
                    categories.append(category)
        i = 1
        for category in categories:
            print(f"{i}. {category}")
            i += 1
        return categories
    
    def validate_choice(self, choice, lst):
        number_of_elements = len(lst)
        if choice <= 0:
            raise ValidationError("the number cannot be zero or negative", choice)
        elif choice > number_of_elements:
            raise ValidationError(f"the number cannot be higher than {number_of_elements}", choice)
        else:
            return choice
    
    def choose_category(self):
        categories = self.display_categories()
        while True:
            try:
                chosen_category = self.validate_choice(int(input("Please choose the category: ")), categories)
                break
            except ValueError:
                print("you can only input a number")
            except ValidationError as e:
                print(e.message)
        return categories[chosen_category - 1]
    
    def display_choose_symptoms(self):
        chosen_category = self.choose_category()
        possible_symptoms = []
        for symptom in self.symptoms:
            for category in symptom.categories:
                if category == chosen_category:
                    possible_symptoms.append(symptom)
        i = 1
        print(f"Symptoms in category '{chosen_category}':")
        for symptom in possible_symptoms:
            print(f"{i}. {symptom.description}")
            i += 1
        while True:
            try:
                chosen_symptoms_ids = []
                input_numbers = input("Please choose the symptom/s, separated by spaces: ")
                input_numbers = input_numbers.split()
                for number in input_numbers:
                    number = int(number)
                    chosen_symptom = self.validate_choice(number, possible_symptoms)
                    chosen_symptoms_ids.append(possible_symptoms[chosen_symptom-1].id)
                break
            except ValueError:
                print("you can only input a number")
            except ValidationError as e:
                print(e.message)
        return chosen_symptoms_ids
    
    def display_results(self, results):
        for result in results:
            print("-" * 30)
            print(f"Your problem might be: {result[0].name}, with a probability of {result[1] * 100:.1f}%")
            print(f"{result[0].get_warning()}")
            print(f"The severity of this problem is: {result[0].severity.value}")
            print("Try these steps:")
            i = 1
            for step in result[0].diag_steps:
                print(f"{i}. {step}")
                i += 1

    def validate_answer(self, answer):
        if answer != "y" and answer != "n":
            raise ValidationError("you can only input 'y' or 'n'", answer)
        else:
            return answer
    
    def run(self):
        while True:
            chosen_symptom_ids = self.display_choose_symptoms()
            results = self.diagnostic_engine.diagnose(chosen_symptom_ids)
            self.display_results(results)
            answer = self.validate_answer(input("Would you like to diagnose again? (y/n): "))
            if answer == "n":
                break