from datetime import datetime

from application.salary import calculate_salary
from db.people import get_employees

print(datetime.today().date())
if __name__ == '__main__':
    get_employees()
    calculate_salary()
