code = "*312#"
data_balance = 1012.65 
USSD_code = input("Dial  the USSD code *312#: ")
if USSD_code != code:
      print("Enter the correct USSD code!")
while USSD_code == code:
    print("1. Buy Data")
    print("2. Gift Data")
    print("3. Data balance")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(f"1. Proceed (Auto-Renew)")
        print(f"2. Proceed (One-off)")
        print(f"99. Back")
        print(f"0. Exit")

        option = int(input("Choose an option: "))

        if option == 1:
             print("You have successfully activated your autorenewal")
             break
        elif option == 2:
             print("You have successfully activated your one-off plan")
             break
        elif option == 99:
             print("Redirecting........")
        elif option == 0:
             print("Exiting. Thank you.")
             break
        
    if choice == 2:
        print(f"1. Daily-weekly PLans")
        print(f"2. Monthly Plans")
        print(f"99. Back")
        print(f"0. Exit")

        decision = int(input("Choose an option: "))

        if decision == 1:
             giftee = input("Enter Giftee Number: ")
            #  if len(giftee) != 11:
            #       print(f"Giftee number must be 11 digit.")
             amount = float(input("Enter withdrawal amount: "))
             if amount <= data_balance:
              data_balance -= amount
              print(f"Withdrawal successful. New balance: {data_balance}")
              break
             else:
              print("Insufficient funds.")
              break
           
                #   print(f"You have successfully activate a Daily-Weekly plan for {giftee}")
                #   break
        elif decision == 2:
             giftee = int(input("Enter Giftee Number: "))
             print(f"You have succesfully activate a Monthly Data Plan for {giftee}")
             break
        
        elif decision == 99:
             print("Redirecting....") 
        elif decision == 0:
             print(f"Exiting. Thank You.")
             break
        
    if choice == 3:
        print(f"Your data balance is: {data_balance} mb")
        break

    if choice == 0:
        print(f"Exiting. Thank you")
        break

    else:
        print("Invalid option. Try again.")