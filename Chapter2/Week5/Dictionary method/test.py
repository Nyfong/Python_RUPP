def calculate_wages_and_taxes():
    for i in range(1, 11):  # for 10 employees
        print(f"Employee {i}:")
        employee_code = input("Enter employee code: ")
        wage_rate = float(input("Enter wage rate (baht/hour): "))
        hours_worked = float(input("Enter number of hours worked: "))
        
        gross_wage = wage_rate * hours_worked
        
        if gross_wage >= 10000:
            tax_rate = 7
        else:
            tax_rate = 5
        
        tax_to_pay = gross_wage * (tax_rate / 100)
        net_wage = gross_wage - tax_to_pay
        
        print(f"Gross Wage: {gross_wage:.2f} baht")
        print(f"Tax to be Paid: {tax_to_pay:.2f} baht")
        print(f"Net Wage: {net_wage:.2f} baht")
        print()

calculate_wages_and_taxes()
