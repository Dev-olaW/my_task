# Task 6
full_name = input("Enter Customer's full name: ")
unit_consumed = int(input("Units consumed (KWh): "))
cost_per_unit = float(input("The Cost Per Unit: "))
total_bill = cost_per_unit * unit_consumed

print("\n \t\t ELECTRICITY BILL FORMATTER      ")
print(f"Customer's full name: \t{full_name}")
print(f"Units consumed (KWh): \t{unit_consumed}")
print(f"Cost per unit: \t\t{cost_per_unit}")
print(f"Total bill: \t\t{total_bill}")
