from graphic_crop_item_class import *
from wheat_class import *

import field_resources

class WheatGraphicsPixmapItem(CropGraphicsPixmapItem):
    """This class provides a graphical representation of a wheat crop"""

    #constructor
    def __init__(self):
        self.available_graphics = [":/wheat_seed.png", ":/wheat_seeling.png",
                                   ":/wheat_young.png", ":/wheat_mature.png",
                                   ":/wheat_old.png"]
        super().__init__(self.available_graphics)
        self.crop = Wheat()
