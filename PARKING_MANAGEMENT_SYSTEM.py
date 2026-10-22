# Parking lot details
total_spots = 10
vehicles = []  # List of parked vehicles

# Function to show available spots
def show_spots():
    print(f"\nAvailable spots: {total_spots - len(vehicles)} / {total_spots}\n")

# Function to add vehicle
def vehicle_entry():
    if len(vehicles) >= total_spots:
        print("Parking lot is full!\n")
        return
    
    plate = input("Enter vehicle plate number: ")
    entry_time = int(input("Enter entry time (hour in 24hr format): "))
    
    vehicles.append({"plate": plate, "entry_time": entry_time})
    print("Vehicle parked successfully!\n")

# Function to remove vehicle
def vehicle_exit():
    plate = input("Enter vehicle plate number to exit: ")
    for v in vehicles:
        if v["plate"].lower() == plate.lower():
            exit_time = int(input("Enter exit time (hour in 24hr format): "))
            hours_parked = exit_time - v["entry_time"]
            fee = hours_parked * 50  # Rs. 50 per hour
            vehicles.remove(v)
            print(f"Vehicle exited. Hours Parked: {hours_parked}, Fee: Rs.{fee}\n")
            return
    print("Vehicle not found!\n")

# Function to display parked vehicles
def show_vehicles():
    if not vehicles:
        print("No vehicles in the parking lot.\n")
    else:
        print("\n--- Parked Vehicles ---")
        for v in vehicles:
            print(f"Plate: {v['plate']}, Entry Time: {v['entry_time']} hrs")
        print()

# Main loop
while True:
    print("0. Exit")
    print("1. Show Available Spots")
    print("2. Vehicle Entry")
    print("3. Vehicle Exit")
    print("4. Show Parked Vehicles")
    
    choice = input("Enter your choice: ")
    
    if choice == "0":
        print("Exiting Parking Management System...")
        break
    elif choice == "1":
        show_spots()
    elif choice == "2":
        vehicle_entry()
    elif choice == "3":
        vehicle_exit()
    elif choice == "4":
        show_vehicles()
    else:
        print("Invalid choice, try again.\n")
