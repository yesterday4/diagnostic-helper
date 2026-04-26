# Car Diagnostic Helper — Report

---

## 1. Introduction

### a) What is this application?

This application is used for diagnosing car problems and faults based on specific symptoms selected by the user.

### b) How to run the program?

Extract the folder containing all `.py` files and the `.json` file (if compressed). Then using a terminal (such as CMD), navigate to the folder and run the following command:

```
python main.py
```

This will launch the application in the same terminal.

### c) How to use the program?

After launching the application, you will first be asked to choose a category from a numbered list. Input the number corresponding to the category you would like to open.

A list of symptoms belonging to that category will then be shown. Choose one or multiple symptoms by inputting their numbers separated by spaces.

Finally, the possible problems based on the selected symptoms will be displayed. For each problem you will see:

- The probability of the problem (based on its overall likelihood of occurrence and how many of its symptoms were matched)
- A warning message corresponding to the problem type
- The severity of the problem
- A list of diagnostic and repair steps

**Example output:**

```
------------------------------
Your problem might be: Fuel/compression/spark problems, with a probability of 40.0%
Further operation of the car could lead to further damage!
The severity of this problem is: high
Try these steps:
1. Check if each cylinder has the correct compression pressure
2. Check that the correct fuel pressure is present
3. Check that the injector opening signal is present
4. If it is a gasoline engine, check for spark
```

All diagnostic results with timestamps are also saved to `diagnostic_history.txt` in the same folder.

---

## 2. Body / Analysis

### The Four OOP Pillars

#### Polymorphism

Polymorphism allows different classes that inherit from the same base class to act differently, usually by overriding methods — the same method has different functionality depending on the class.

In this application polymorphism is used for the `get_warning()` method, which is defined as an abstract method in the abstract class `Problem()`. Each of the 3 classes that inherit from it override this method with their own implementation:

```python
class SafetyCriticalProblem(Problem):
    def get_warning(self):
        return "Further operation of the car could lead to serious injury or death!!!"

class MechanicallyCriticalProblem(Problem):
    def get_warning(self):
        return "Further operation of the car could lead to further damage!"

class NonCriticalProblem(Problem):
    def get_warning(self):
        return "Further operation of the car has no serious risks."
```

When `display_results()` calls `get_warning()`, it does not need to know which subclass it is dealing with — the correct message is returned automatically:

```python
print(result[0].get_warning())
```

#### Abstraction

Abstraction is the use of abstract classes and methods that allows classes inheriting from the abstract class to write their own functionality for these methods. It also forces these classes to implement all abstract methods, and an object cannot be created directly from the abstract base class.

In this application it is used in the same place as the previous pillar: `Problem()` is an abstract class with the abstract method `get_warning()` that must be implemented by each class that inherits from it:

```python
from abc import ABC, abstractmethod

class Problem(ABC):

    @abstractmethod
    def get_warning(self):
        pass
```

#### Inheritance

Inheritance is the act of one or multiple classes inheriting from a base class. These classes then inherit all of the base class's attributes and methods. The `super()` function can also be used to run all of the code from a base class's method and also override it by adding additional code.

In this application inheritance is also present in the same part of the code as the two previous pillars. The 3 different `Problem()` subclasses inherit from the base class:

```python
class SafetyCriticalProblem(Problem):
    ...

class MechanicallyCriticalProblem(Problem):
    ...

class NonCriticalProblem(Problem):
    ...
```

`super()` is not used on any of the methods, because the getters, setters and `__init__` are identical to those in the base class and the `get_warning()` method is completely overridden.

#### Encapsulation

Encapsulation is the use of private and protected attributes and methods that are meant to only be accessed by a certain class or its subclasses. These private and protected attributes are usually not accessed directly — they are accessed using special functions called getters and setters.

In this application it is used for all attributes of all the classes and their subclasses — they are all protected. They are all accessed using getters and data is written into them using setters which also validate the data type:

```python
@property
def id(self):
    return self._id

@id.setter
def id(self, value):
    if not isinstance(value, int):
        raise TypeError("id must be an integer")
    self._id = value
```

---

### Design Pattern

#### Factory Method

The Factory Method is a design pattern where a method or class is used for choosing, based on certain data, the correct subclass for creating an object.

In this application it is used for creating objects of the `Problem()` subclasses: it receives a dictionary, checks the `problem_type` of the problem, and creates an object of the correct subclass:

```python
class ProblemFactory:
    def create_problem(self, data):
        problem_type = ProblemType(data["problem_type"])
        args = (
            data["id"],
            data["name"],
            data["category"],
            data["severity"],
            data["base_probability"],
            data["symptom_ids"],
            data["diagnostic_steps"]
        )
        if problem_type == ProblemType.SAFETY_CRITICAL:
            return SafetyCriticalProblem(*args)
        elif problem_type == ProblemType.MECHANICALLY_CRITICAL:
            return MechanicallyCriticalProblem(*args)
        elif problem_type == ProblemType.NON_CRITICAL:
            return NonCriticalProblem(*args)
        else:
            raise ValueError(f"Unknown problem type: {problem_type}")
```

This design pattern was chosen because these objects need to be created at runtime and their class needs to be chosen based on data read from the `.json` file. Other patterns such as Singleton would not work here, as the goal is to create multiple different objects rather than ensure a single instance exists.

---

### Composition and Aggregation

**Composition** is a type of relationship where one object owns another and the owned object cannot exist independently. The owned object is created inside the owner object.

In this application it is seen inside the `Loader()` class — an object of this class creates an object of the class `ProblemFactory()` and it exists and is used only inside this object:

```python
class Loader:
    def __init__(self):
        with open('symptoms_problems.json', 'r') as f:
            self.d = json.load(f)
        self.problem_factory = ProblemFactory()
```

**Aggregation** is a different type of relationship where an object uses another object but does not own it — both can exist independently.

In this application it is seen inside the `DiagnosticEngine()` class — an object of this class uses objects of the `Problem()` subclasses which are already created previously by the `Loader()`. Also, inside the `Display()` class — an object of this class uses an object of the `DiagnosticEngine()` class and an object of the `Logger()` class which are already created in `main.py`.

---

### Reading from and Writing to a File

In this application all the objects made from `Problem()` subclasses are read from the file `symptoms_problems.json` and saved into dictionaries at first.

All the diagnostic results are saved to the file `diagnostic_history.txt` and timestamps are added for each session:

```python
def save_results(self, results):
    with open(self.filename, "a", encoding="utf-8") as f:
        if results:
            for result in results:
                f.write(f"Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Problem: {result[0].name}\n")
                ...
```

---

## 3. Results and Summary

### a) Results

- The application is able to successfully suggest problems and their probabilities based on symptoms chosen by the user.
- The probability is not highly accurate as the base probabilities were chosen based on personal experience and knowledge rather than statistical data.
- The amount of symptoms and problems is limited for now, but it is enough for some basic diagnosis.
- The process of making the `.json` file was quite lengthy as all the problems and symptoms were written based on personal knowledge and experience.
- The code follows PEP8 style guidelines.

### b) Conclusions

I was able to fulfill all of the requirements, including the use of the four OOP pillars while making this application. It performs as intended and the result is a functional car diagnostic tool. The process of making it allowed me to better understand and practically apply the Python concepts learned during this semester.

### c) Future Prospects

Future upgrades for this application could include:

- The use of a database for the symptoms and the problems, which would facilitate the use of a much greater amount of information.
- Assigning the base probability of each problem based on actual statistical data.
- Adding a graphical user interface (GUI).
- Allowing users to freely type their symptoms and matching them to existing ones using fuzzy or keyword matching.
