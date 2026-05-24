import ast


sample_employees = {
    "Sunil": 30000,
    "Neha": 35000,
    "Meera": 40000,
}


with open("employees.txt", "w") as f:
    f.write(str(sample_employees))


with open("employees.txt", "r") as f:
    employees = ast.literal_eval(f.read())


with open("employees.txt", "w") as f:
    for name, old_salary in employees.items():
        new_salary = old_salary + (old_salary * 10 / 100)
        line = f"Employee Name: {name}, Old Salary: {old_salary}, New Salary: {new_salary}\n"
        print(line, end="")
        f.write(line)