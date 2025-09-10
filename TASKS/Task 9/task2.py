#  A UNIQUE VOTERS REGISTRATION SYSTEM

voters_name = set()


while True :
    name = input("Enter your name, (type 'done' to close): ")
    if name == "done":
        break

    if name in voters_name:
        print(f"{name} has already registered.")

    else:
        voters_name.add(name)
        print(f"{name} registered succesfully.")

print(f"\nTotal unique voters required: {len(voters_name)}")