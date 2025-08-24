seat_number = set()
seat_number = set(range(1,51))

seat = int(input("Enter your seat number (1-50), or 0 to exit: "))

if seat == 0:
    print("Exiting the system.")
    

if seat not in range(1,51):
    print("Invalid seat number.Pleas enter a number between 1 to 50.")
elif seat not in seat_number:
    print(f"Seat number {seat} is already booked.")
else:
    seat_number.remove(seat)
    print(f"Seat {seat} booked successfully")
    print("Remaining seats:", seat_number)