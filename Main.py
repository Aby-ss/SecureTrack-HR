import sqlite3

from rich import print, box, text

from rich.tree import Tree
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout 

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)

employee_conn = sqlite3.connect("EmployeeDatabase.db")
cursor = employee_conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS EmployeeDatabase (
               EmployeeID INTEGER PRIMARY KEY,
               Name TEXT,
               Age INTEGER,
               Role TEXT,
               Salary INTEGER
               )
               ''')

password = "4556786"
user_identification = Prompt.ask("Enter Password ")


def add_employee():
    new_employee_name = Prompt.ask("Enter new employee's name ")
    new_employee_ID = Prompt.ask("Enter new employee's ID ")
    new_employee_age = Prompt.ask("Enter new employee's age ")
    new_employee_role = Prompt.ask("Enter new employee's role ")
    new_employee_salary = Prompt.ask("Enter new employee's salary")

    cursor.execute(f"INSERT INTO EmployeeDatabase (EmployeeID, Name, Age, Role, Salary) VALUES (?, ?, ?, ?, ?)", (new_employee_ID, new_employee_name, new_employee_age, new_employee_role, new_employee_salary))

    employee_conn.commit()
    employee_conn.close()

def print_employee_data():
    cursor.execute("SELECT * FROM EmployeeDatabase")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    employee_conn.close()
    
if user_identification == password:
    print(Panel("User Authorised!", box=box.SQUARE, border_style="bold green"))

    print(Panel.fit("Choose an Option:\n1- Add new employee\n2- Discard employee\n3- Print employee database", box = box.SQUARE, border_style="bold white"))

    option_choice = Prompt.ask("Choose a number as your option ")

    if int(option_choice) == 1:
        add_employee()
    elif int(option_choice) == 3:
        print_employee_data()
else:
    
    print(Panel("Incorrect Password", box=box.SQUARE, border_style="bold red"))