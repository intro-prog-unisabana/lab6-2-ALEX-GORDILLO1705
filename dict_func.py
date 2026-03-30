# Write your code here!
def employee_print(employee_info):
    # Crear copia para no modificar el original
    info = employee_info.copy()

    name = info.pop("Name", "N/A")
    salary = info.pop("Salary", "N/A")
    role = info.pop("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    if info:
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")