from data_loader import Loader
from ui import Display
from diagnostic_engine import DiagnosticEngine
from data_logger import Logger

loader = Loader()
symptoms = loader.load_symptoms()
problems = loader.load_problems()

diagnostic_engine = DiagnosticEngine(problems)

logger = Logger()

display = Display(symptoms, diagnostic_engine, logger)
display.run()