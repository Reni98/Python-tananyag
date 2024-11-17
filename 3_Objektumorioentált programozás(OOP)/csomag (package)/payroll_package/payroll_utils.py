# payroll_utils.py

def calculate_average_salary(salaries):
    """Kiszámítja a fizetések átlagát"""
    if not salaries:
        return 0
    return sum(salaries) / len(salaries)

def calculate_total_salary(salaries):
    """Kiszámítja a fizetések összegét"""
    return sum(salaries)
