# Task 10
school_name = input("Enter school name: ") 
tuition_fee = float(input("Enter tution fee: "))
hostel_fee = float(input("Enter the hoste fee: "))
feeding_fee = float(input("Enter thr feeding fee: "))
total_fee = tuition_fee + hostel_fee + feeding_fee

print(school_name,"School Fees Break" )
print(f"Tuition fee:", tuition_fee) 
print(f"Hostel fee:", hostel_fee)
print(f"Feeding fee:", feeding_fee)
print(f"Total Fee:", total_fee)