# AFORE Retirement Investment Calculator

This Python project calculates the estimated amount a user will have at retirement based on their AFORE (Administradoras de Fondos para el Retiro) investments in Mexico. The calculation accounts for:

- Average AFORE returns over the last five years.
- Changes in AFORE investment strategies as users age (e.g., less risky investments for older users).
- User-specific details such as salary and starting age of work.

This is my first self-directed Python project, designed to showcase problem-solving, Python programming, and domain-specific knowledge in retirement planning in Mexico.

## Features
- Flexible input options: Users can choose to start their retirement calculations from today or from when they began working.
- Accurate compaund interest calculation: Utilizes AFORE returns and age-based investment groupings to project compaunded returns over time. 
- Detailed outputs: Provides users with a breakdown of their current investment group, annual returns, and total projected retirement savings.

## Concepts and Libraries Used
Programming Concepts
- Loops: For processing data files and iterating over periods for compound interest calculations.
- Functions: Custom functions in external modules for assigning AFORE groups, calculating default contributions, and determining time periods.
- Modules: Code is modularized with custom Python modules (afore_module_functions, interest_module) for reusability and clarity.
- Dictionaries: Used for efficient indexing of AFORE groups and returns.
- File Handling: Reads and processes real-world data stored in .txt files.
- Error Handling: Validates user inputs to ensure robust operation.
Libraries
- datetime: Extracts and utilizes the current date for precise age and time calculations.

## How It Works
1. The user inputs basic details such as name, birth year, salary, and starting age of work.
2. The program:
- Assigns the user to an AFORE group based on their age.
- Calculates contributions and compound interest for the remaining time in each group.
- Moves the user through successive AFORE groups, adjusting returns accordingly.
The total projected retirement savings are displayed based on the user's details.

