from animal_class import *

class Cow(Animal):
    """A representation of a cow."""
    #Constructor
    def __init__(self):
        #Growth rate of 2; Food need; 5; Water need; 5
        super().__init__(2,5,5)
        self._type = "Cow"


    #Overide/Polymorphism
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 2
            elif self._status == "Adult" and water > self._water_need:
                self._weight += self._growth_rate * 2
            else:
                self._weight += self._growth_rate
        #Increment day growing
        self._days_growing += 1
        #Update the status
        self._update_status()
    
def main():
    #Create a new cow
    cow_animal = Cow()
    print(cow_animal.report())
    #Manually grow the crop
    manual_grow(cow_animal)
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
        
