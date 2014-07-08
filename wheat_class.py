from crop_class import *

class Wheat(Crop):
    """A representation of wheat."""

    #Constructor
    def __init__(self):
        #Call superclass constructor
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Wheat"
        
    #Override grow method for subclass
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        #Increment day growing
        self._days_growing += 1
        #Update the status
        self._update_status()

def main():
    #Create a new potato crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #Manually grow the crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
