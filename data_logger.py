from datetime import datetime

class Logger:
    def __init__(self, filename = "diagnostic_history.txt"):
        self.filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError("filename must be a string")
        self._filename = value

    def save_results(self, results):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write("*" * 60)
            f.write(f"\nSession: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            if results:
                for result in results:
                    f.write("-" * 30)
                    f.write("\n")
                    f.write(f"Your problem might be: {result[0].name}, with a probability of {result[1] * 100:.1f}%\n")
                    f.write(f"{result[0].get_warning()}\n")
                    f.write(f"The severity of this problem is: {result[0].severity.value}\n")
                    f.write("Try these steps:\n")
                    i = 1
                    for step in result[0].diag_steps:
                        f.write(f"{i}. {step}\n")
                        i += 1
            else:
                f.write("-" * 30)
                f.write("No problems matched the input symptoms\n")