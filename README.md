# Cafe Menu with Python

## Description
This project simulates a simple cafe menu system, where users can choose coffee types, view ingredients, and manage daily/weekly revenue. The system calculates the price based on the coffee size and records sales in an SQLite database.

## Features
- **Coffee Menu**: Includes different types of coffee like Espresso, Americano, Latte, etc., with their ingredients and prices.
- **Daily and Weekly Revenue**: Tracks daily sales and calculates weekly revenue.
- **Database Integration**: Uses SQLite to store sales data.

## Installation

### Requirements:
- **Python 3.x**: Ensure Python 3.x is installed.
- **SQLite3**: Comes with Python by default, no separate installation needed.

### Steps to Install and Run:
1. **Clone the repository** or download the project files:
    ```bash
    git clone https://github.com/yasinkrcm/Cafe-Menu-With-python.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd Cafe-Menu-With-python
    ```
3. **Run the program**:
    ```bash
    python cafeMenu.py
    ```
5. **Database Creation**: The program will automatically create a `Cafe.db` SQLite database if it doesn't exist.

### Dependencies:
- Python 3.x (comes with SQLite3 built-in)

## File Structure
Cafe-Menu-With-python/ <br>
│<br>
├── cafeMenu.py # Main program <br>
├── dataBaseConnection.py # Database connection and functions <br>
├── BaseStructure.py # Coffee class and revenue handling <br>
├── Cafe.db # SQLite database for storing sales data <br>
└── README.md # Project documentation<br>

## Usage

### Main Features:
1. **Coffee Menu**: Users can view and choose from various coffee types, and see their ingredients and prices.
2. **Daily Revenue**: Users can track the daily sales for each coffee and calculate total sales.
3. **Weekly Revenue**: The system calculates and displays the weekly revenue.

### Code Walkthrough:
- **`cafeMenu.py`**: The main script that runs the program. It contains the menu, processes customer choices, and interacts with the database.
- **`dataBaseConnection.py`**: This file handles all database-related operations, such as creating tables, inserting data, and fetching daily/weekly revenue.
- **`BaseStructure.py`**: Contains classes like `Coffee` and `Revenue` that define the coffee menu and manage sales calculations.

## License
This project is **not licensed** and can be freely used and modified.

---

For more details, feel free to reach out or contribute to the repository.
