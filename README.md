# Internship Task 4: Temperature Converter Console Application

**Project Name**: Temperature Converter Console App  
**Internship Provider**: Cognifyz Technologies  
**Task Identifier**: Level 2 Intermediate Task 4 - Build a temperature converter program.  
**Compliance Status**: 100% COMPLIANT & VERIFIED (EXCEEDS REQUIREMENTS)

---

## 📋 Assignment Requirements Mapping & Compliance Matrix

Below is a detailed verification mapping of our implementation (`Task4_TemperatureConverter.py`) against the core steps defined by the Cognifyz Technologies Level 2 Task 4 assignment sheet:

### Step 1: Design a program to accept temperature input
* **Requirement**: Structure an input mechanism to collect user temperatures.
* **My Implementation**: Captured via `get_numeric_temperature()` in `Task4_TemperatureConverter.py`. Strips whitespace, validates that it is a valid floating point number, and catches `ValueError` exceptions to gracefully re-prompt on invalid inputs without crashing.

### Step 2: Implement logic for temperature conversion
* **Requirement**: Code the conversion algorithms for Celsius and Fahrenheit.
* **My Implementation**: Isolated the conversion math into `celsius_to_fahrenheit(celsius)` and `fahrenheit_to_celsius(fahrenheit)`. The formulas `F = (C * 9/5) + 32` and `C = (F - 32) * 5/9` are fully verified by automated unit tests in `test_Task4_TemperatureConverter.py`.

### Step 3: Allow users to choose the conversion direction
* **Requirement**: Let users pick Celsius-to-Fahrenheit or Fahrenheit-to-Celsius.
* **My Implementation**: Provided an interactive option menu inside `display_menu()` for choosing directions (Option 1 or Option 2) or exiting the program (Option 3). Invalid selections print a stylized error, wait for user acknowledgment, and safely loop.

### Step 4: Test the program with different input values
* **Requirement**: Test with multiple inputs and check correctness.
* **My Implementation**: Structured standard unit tests in `test_Task4_TemperatureConverter.py` checking multiple input cases: 0°C (freezing), 100°C (boiling), -40° (overlap point), and decimal temperatures like 37°C (human body temp). Additionally, added safety protections for `KeyboardInterrupt` / Ctrl+C.

---

## ✨ Features & Visual Highlights

* **Rich Terminal Aesthetics**: Beautiful terminal formatting with ANSI escape sequences (Magenta headers, Cyan option buttons, Green confirmations, and Bold styling).
* **Validation Shields**: Keeps the application running safely against user typing slips, ensuring robust error handling.
* **Interaction Flow Control**: Automatic screen clearing on startup and menu return, with a user prompt to press Enter before returning to the main menu.
* **Pure Python implementation**: Standard library only, no external third-party dependencies required.

---

## 🖥️ Terminal Interface Preview

Below is a visualization of how the interactive Temperature Converter interface displays in the terminal:

### Main Menu
```text
===================================
    Temperature Converter Menu    
===================================

1. Convert Celsius (°C) → Fahrenheit (°F)
2. Convert Fahrenheit (°F) → Celsius (°C)
3. Exit Program

===================================

Choose an option (1-3): 
```

### Conversion (Option 1)
```text
--- Celsius to Fahrenheit ---
Enter the temperature value: 25

Success: 25.00°C is equal to 77.00°F

Press Enter to return to the main menu... 
```

---

## 🚀 How to Run the Application

No external dependencies are required. The script uses pure, native Python 3 standard library modules.

### Prerequisites
Make sure you have **Python 3.x** installed. Check version:
```bash
python3 --version
```

### Execution Command
Run the main script directly from the project directory:
```bash
python3 Task4_TemperatureConverter.py
```

### Running the Unit Tests
Run the unit test suite to verify math and boundary validation:
```bash
python3 test_Task4_TemperatureConverter.py
```

