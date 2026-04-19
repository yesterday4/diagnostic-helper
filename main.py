from data_loader import Loader
from ui import Display
from diagnostic_engine import DiagnosticEngine

loader = Loader()
symptoms = loader.load_symptoms()
problems = loader.load_problems()

diagnostic_engine = DiagnosticEngine(problems)

display = Display(symptoms, diagnostic_engine)
display.run()