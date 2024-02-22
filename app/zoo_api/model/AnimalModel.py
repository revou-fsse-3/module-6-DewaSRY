

from uuid import uuid4
from dataclasses import dataclass

from app.zoo_api.utils.FlaskDb import FlaskDb
from app.zoo_api.service.EnumMemberService import EnumMemberService
from app.zoo_api.service.DbModelService import DbModelService


from app.zoo_api.entity.AnimalSpecies import AnimalSpecies
from app.zoo_api.entity.Gender import Gender
from app.zoo_api.entity.AnimalSpecies import AnimalSpecies




db= FlaskDb.getDb()

@dataclass
class AnimalBaseModel(db.Model,):
    __tablename__= "animal"
    animalId= db.Column("animal_id", db.String, primary_key=True)
    name= db.Column("name", db.String)
    species= db.Column("species", db.String)
    gender= db.Column("gender", db.String)
    age= db.Column("age" , db.Integer)

    def __init__(self, name: str ,species: str, gender:str, age:int ):
        self.animalId=str(uuid4())
        self.name=name
        self.species=EnumMemberService(AnimalSpecies).getMatchValue(species)
        self.gender=EnumMemberService(Gender).getMatchValue(gender)
        self.age=age

    def update(self, name: str=None ,species: str=None, gender:str=None, age:int=None ):
        self.name=name if name != None else self.name
        self.species=EnumMemberService(AnimalSpecies).getMatchValue(species) if species != None else self.species
        self.gender=EnumMemberService(Gender).getMatchValue(gender) if gender != None else self.gender
        self.age=age if age != None else self.age
    
    

    def __str__ (self):
        return f"{self.species} {self.name} {self.gender} {self.age}"
    
    def get_item_dict(self):
        print(self.__dict__)
        return self.__dict__


