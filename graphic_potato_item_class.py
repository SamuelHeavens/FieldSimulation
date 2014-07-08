from graphic_crop_item_class import *
from potato_class import *

import field_resources

class PotatoGraphicsPixmapItem(CropGraphicsPixmapItem):
    """This class provides a graphical representation of a potato crop"""

    #constructor
    def __init__(self):
        self.available_graphics = [":/potato_seed.png", ":/potato_seeling.png",
                                   ":/potato_young.png", ":/potato_mature.png",
                                   ":/potato_old.png"]
        super().__init__(self.available_graphics)
        self.crop = Potato()
