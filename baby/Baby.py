import numpy as np

class Baby:
    cute = True
    def __init__(self, height: int, weight: int, loudness: str, hungry: bool) -> None:
        self.height = height
        self.weight = weight
        self.loudness = loudness
        self.hungry = hungry

    def cry(self):
        if self.loudness == "Loud" or self.hungry:
            return "WAAAAA!"
        else:
            return "waaaaa"
    
    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            return "NOOOO"
    
