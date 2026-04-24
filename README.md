# Car Diagnostic Application Overview

This application is designed to assist in **diagnosing vehicle faults** by analyzing specific symptoms provided by the user [cite: 2].

---

### Getting Started

To run the application, follow these steps:

1.  **Extract the Files**: Ensure the folder containing all `.py` files and the single `.json` file is extracted (if compressed) [cite: 3].
2.  **Launch via Terminal**: Open a terminal (such as CMD) and execute the command `python main.py` [cite: 3].
3.  **Interface**: The application interface will launch directly within that same terminal window [cite: 4].

---

### How to Use

Once the application is running, the diagnostic process follows a simple workflow:

* **Select a Category**: Choose a category from the displayed list by inputting its corresponding number [cite: 5, 6].
* **Identify Symptoms**: A list of symptoms for that category will appear [cite: 7]. Select one or multiple symptoms by entering their numbers separated by spaces [cite: 8].
* **Review Results**: The system will display possible problems based on your input [cite: 9].

---

### Understanding the Results

For every identified problem, the application provides detailed insights:

* **Probability**: Calculated based on the overall probability of its occurrence and the ratio of matched symptoms [cite: 10].
* **Severity**: Each issue is assigned a severity level along with a specific warning message [cite: 11].
* **Action Plan**: A list of suggested diagnostic and repair steps is provided for each potential problem [cite: 10].
* **Logging**: All diagnostic data, including timestamps, is automatically saved to `diagnostic_history.txt` within the same folder [cite: 21].

---

### Diagnostic Example

> **Your problem might be:** Fuel/compression/spark problems, with a probability of **40.0%** [cite: 13]
> **Warning:** Further operation of the car could lead to further damage! [cite: 14]
> **Severity:** high [cite: 15]
>
> **Suggested Steps:** [cite: 16]
> 1. Check if each cylinder has the correct compression pressure [cite: 17]
> 2. Check that the correct fuel pressure is present [cite: 18]
> 3. Check that the injector opening signal is present [cite: 19]
> 4. If it is a gasoline engine, check for spark [cite: 20]
