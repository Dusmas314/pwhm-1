from application import people, salary
import datetime


datetime_today = datetime.date.today()

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(datetime_today)

