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