
from app.zoo_api.service.DbModelService import DbModelService
from app.zoo_api.model.AnimalModel import AnimalBaseModel


class AnimalModelService:
    @staticmethod
    def getDb()-> DbModelService :
        dbAnimal = DbModelService(AnimalBaseModel)
        return dbAnimal
