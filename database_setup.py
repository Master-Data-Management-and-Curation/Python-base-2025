import sqlite3
import pandas as pd

def setup_database():
    """
    Creates and populates an SQLite database for use in the course labs.
    """
    try:
        # Create a connection to the database. If the file doesn't exist, it will be created.
        conn = sqlite3.connect('company.db')
        cursor = conn.cursor()
        print("Database created and connected successfully.")

        # Create employees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department_id INTEGER,
                salary REAL
            )
        ''')
        print("Table 'employees' created successfully.")

        # Create departments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                location TEXT
            )
        ''')
        print("Table 'departments' created successfully.")

        # --- Populate the tables ---
        
        # Clear existing data to prevent duplicates on re-run
        cursor.execute('DELETE FROM employees')
        cursor.execute('DELETE FROM departments')

        # Department data
        departments = [
            (1, 'Engineering', 'Building A'),
            (2, 'Sales', 'Building B'),
            (3, 'Human Resources', 'Building A'),
            (4, 'Marketing', 'Building B')
        ]
        cursor.executemany('INSERT INTO departments VALUES (?, ?, ?)', departments)
        print(f"{len(departments)} records inserted into 'departments'.")

        # Employee data
        employees = [
            (101, 'Alice', 1, 95000),
            (102, 'Bob', 2, 80000),
            (103, 'Charlie', 1, 110000),
            (104, 'David', 4, 72000),
            (105, 'Eve', 2, 85000),
            (106, 'Frank', 1, 120000),
            (107, 'Grace', 3, 60000)
        ]
        cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees)
        print(f"{len(employees)} records inserted into 'employees'.")

        # Commit the changes and close the connection
        conn.commit()
        print("Data committed successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':
    setup_database()
    # You can also use this script to generate the CSV files
    # to ensure consistency.
    employees_df = pd.DataFrame([
        {'employee_id': 101, 'name': 'Alice', 'department_id': 1, 'salary': 95000},
        {'employee_id': 102, 'name': 'Bob', 'department_id': 2, 'salary': 80000},
        {'employee_id': 103, 'name': 'Charlie', 'department_id': 1, 'salary': 110000},
        {'employee_id': 104, 'name': 'David', 'department_id': 4, 'salary': 72000},
        {'employee_id': 105, 'name': 'Eve', 'department_id': 2, 'salary': 85000},
        {'employee_id': 106, 'name': 'Frank', 'department_id': 1, 'salary': 120000},
        {'employee_id': 107, 'name': 'Grace', 'department_id': 3, 'salary': 60000},
    ])
    employees_df.to_csv('employees.csv', index=False)
    print("employees.csv created.")

    departments_df = pd.DataFrame([
        {'department_id': 1, 'department_name': 'Engineering', 'location': 'Building A'},
        {'department_id': 2, 'department_name': 'Sales', 'location': 'Building B'},
        {'department_id': 3, 'department_name': 'Human Resources', 'location': 'Building A'},
        {'department_id': 4, 'department_name': 'Marketing', 'location': 'Building B'},
    ])
    departments_df.to_csv('departments.csv', index=False)
    print("departments.csv created.")
