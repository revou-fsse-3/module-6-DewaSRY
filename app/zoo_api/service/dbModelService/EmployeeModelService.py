
from app.zoo_api.service.DbModelService import DbModelService
from app.zoo_api.model.EmployeeModel import EmployeeBaseModel

class EmployeeModelService:
    @staticmethod
    def getDb()-> DbModelService :
        dbAnimal = DbModelService(EmployeeBaseModel)
        return dbAnimal
