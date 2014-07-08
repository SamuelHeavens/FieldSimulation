from animal_class import *

class Sheep(Animal):
    """Representation of sheep."""
    #Constructor
    def __init__(self):
        #Call superclass
        #growth rate = 1.5; food need 2.5; water need; 3
        super().__init__(3,2.5,3)
        self._type = "Sheep"

    #Polymorphism - override grow method
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 3
            elif self._status == "Adult" and water > self._water_need:
                self._weight += self._growth_rate * 3
            else:
                self._weight += self._growth_rate
        #Increment day growing
        self._days_growing += 1
        #Update the status
        self._update_status()
def main():
    #Create a new sheep
    sheep_animal = Sheep()
    print(sheep_animal.report())
    #Manually grow the crop
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
        
