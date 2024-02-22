
from enum import Enum

class AnimalSpecies(Enum):
    REPTILES="Reptiles"
    MAMMALS="Mammals"
    INVERTEBRATES="Invertebrates"
    AMPHIBIANS="Amphibians"
    INSECT="Insect" 
    FISH="Fish"
    BIRD="Birds"
    def __str__(self) -> str:
        return self.value
    


