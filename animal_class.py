import random
class Animal:
    """An animal."""
    #Constructor
    def __init__(self, growth_rate, water_need, food_need):
        #Setting attributes with initial values
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = 5
        self._water_need = 5
        self._status = "Baby"
        self._type = "Common"

        #^Private attributes.

    def needs(self):
        return {"water need":self._water_need,"food need":self._food_need}
    #Report of the current state of animal

    def report(self):
        return{"Type":self._type,"Status":self._status,"Weight (kg)":self._weight,"Days growing":self._days_growing}

    def grow(self,water,food):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #Increment days growing
        self._days_growing += 1
        #Update the status
        self._update_status()
        
    def _update_status(self):
        if self._weight > 50:
            self._status = "Old"
        elif self._weight > 40:
            self._status = "Adult"
        elif self._weight > 30:
            self._status = "Young"
        elif self._weight > 20:
            self._status = "Child"
        elif self._weight == 0:
            self._status = "Unborn"

def auto_grow(animal, days):
    #grow the crop
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    #get the light and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 10")  
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10):"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 10")
    #grow the crop
    animal.grow(food,water)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else: print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program.")

def main():
    #instaniate the class
    new_animal = Animal(1,5,5)
    manage_animal(new_animal)
    
if __name__ == "__main__":
    main()
    
