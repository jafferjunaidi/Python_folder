class car:
    def __init__(self, stock):
        self.stock = stock

    def all_cars(self):
        print("Total number of cars is", self.stock)

    def rent_car(self, quantity):
        if quantity <= 0:
            print("❌ The quantity cannot be less than or equal to zero.")
        elif quantity > self.stock:
            print("❌ The quantity cannot exceed the available stock.")
        else:
            self.stock -= quantity
            print("✅ You have rented", quantity, "car(s).")
            print("🚗 Cars remaining:", self.stock)

# Create the car object once
obj = car(100)

while True:
    try:
        userinput = int(input('''
        🚘 Car Rental System
        ---------------------
        1) Display available cars
        2) Rent a car
        3) Exit
        Enter your choice: '''))

        if userinput == 1:
            obj.all_cars()

        elif userinput == 2:
            quantity = int(input("Enter the number of cars you want to rent: "))
            obj.rent_car(quantity)

        elif userinput == 3:
            print("👋 Thank you for using the Car Rental System. Goodbye!")
            break

        else:
            print("⚠️  Invalid choice. Please select 1, 2 or 3.")

    except ValueError:
        print("⚠️  Please enter a valid number.")