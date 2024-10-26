
# Openspace Organizer

## Description

The **Openspace Organizer** is a Python application designed to facilitate seating arrangements for large groups in an efficient manner. The program takes a list of names (students) and organizes them into tables based on specified capacities, ensuring that the seating is optimized to minimize unseated individuals. This tool is especially useful for educational institutions and event planners who need to manage seating effectively.

## Features

- Import a list of names from an Excel file.
- Specify the number of tables and their capacities.
- Dynamically adjust seating arrangements to minimize unseated individuals.
- Add additional tables if needed, with maximum and minimum capacity specifications.
- Export the final seating arrangement to a specified file.

## Installation

To set up the Openspace Organizer, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd openspace_organizer_personal
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pandas` and `openpyxl` installed for reading Excel files. You can install the required packages using pip:
   ```bash
   pip install pandas openpyxl
   ```

4. **Run the Program**:
   Ensure you have Python installed on your system. Run the program using:
   ```bash
   python main.py
   ```

## Usage

1. **Provide a File Path**: When prompted, input the file path of the Excel file containing the student data. The program will verify that the file exists.
   
2. **Specify the Column Name**: You can specify the column name for student names. If you don't provide one, it will default to `Students`. If the specified column does not exist, an error will be raised.

3. **Input Table Information**: Specify the number of tables and their capacities. The program will then organize the seating and inform you about any remaining unseated people.

4. **Add More Tables**: After the initial seating arrangement, you can opt to add more tables by specifying their maximum and minimum capacities.

5. **Export Configuration**: At the end of the program, you can choose to export the new seating configuration to a specified file.

#### User Interaction Flow
```plaintext
Please provide a file path: [user input]
Please specify the column name names extraction: [user input]
There is a total of [X] people to be seated
Please specify number of tables: [user input]
Please specify the table capacity: [user input]
People have been seated
[Displays seating arrangement]
There is a total of: [Y] left unseated
Would you like to add more tables to find them a seat? type: Yes / No [user input]
...
```

#### Sample Seating Arrangement Output
```
Table 1: [Student A, Student B, Student C]
Table 2: [Student D, Student E, Student F]
Table 3: [Student G, Student H]
Remaining Unseated: [Student I]
```


# python-openspace-organizer
