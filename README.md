

# PARKING MANAGEMENT SYSTEM

A simple, menu-driven Parking Management System built using Python to manage parking spaces, vehicle entry and exit, and parking fee calculations.

## About

This project simulates a parking lot with **10 parking spaces**. Users can check available spots, register incoming vehicles, remove exiting vehicles, and view currently parked vehicles.

The system calculates parking fees at a rate of **Rs. 50 per hour**.

## Features

- Display available parking spots
- Register vehicle entry
- Store vehicle plate numbers
- Record vehicle entry time
- Register vehicle exit
- Calculate parking duration
- Calculate parking fees
- Display parked vehicles
- Check whether a vehicle exists
- Handle invalid menu choices
- Exit the application

## Technologies Used

- Python

## Python Concepts Practiced

- Variables and data types
- Lists
- Dictionaries
- Functions
- `while` loops
- `for` loops
- Conditional statements
- User input with `input()`
- Type conversion using `int()`
- List operations
- String methods such as `lower()`
- F-strings
- Arithmetic operations

## Parking Fee Calculation

The parking fee is calculated using the following formula:

```text
Parking Duration = Exit Time - Entry Time

Parking Fee = Parking Duration × Rs. 50
```

**Example:**

If a vehicle enters at 10:00 and exits at 13:00:

- Parking duration: 3 hours
- Fee per hour: Rs. 50
- Total parking fee: Rs. 150

## Menu Options

| Option | Function |
|---|---|
| 0 | Exit the system |
| 1 | Show available spots |
| 2 | Register vehicle entry |
| 3 | Register vehicle exit |
| 4 | Show parked vehicles |

## How to Run

1. Clone or download this repository.
2. Open the project folder in your code editor.
3. Make sure Python is installed.
4. Run the following command in the terminal:

```bash
python Parking_Management_System.py
```

## Data Storage

Vehicle records are stored in a Python list using dictionaries. The data remains in memory while the program runs and is not permanently saved to a file or database.

## Purpose

This project was created to practice Python programming fundamentals by building a practical parking management application.

## Future Improvements

- Add date and minute-based time tracking
- Validate entry and exit times
- Prevent duplicate vehicle entries
- Save records permanently using file handling
- Connect the system to a database
- Add different vehicle types and parking rates
- Develop a graphical user interface

## Author

**Fatima Aziz**

GitHub: [fatimaaziz27](https://github.com/fatimaaziz27)

