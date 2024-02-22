from uuid import uuid4
from dataclasses import dataclass

from app.zoo_api.utils.FlaskDb import FlaskDb
from app.zoo_api.service.EnumMemberService import EnumMemberService
from app.zoo_api.entity.EmployeeRole import EmployeeRole
from app.zoo_api.entity.EmployeeSchedule import EmployeeSchedule

db= FlaskDb.getDb()

@dataclass
class EmployeeBaseModel(db.Model,):
    __tablename__= "employee"
    employeeId= db.Column("employee_id",  db.String, primary_key=True)
    role= db.Column("employee_role", db.String)
    schedule= db.Column("schedule", db.String) 
    name= db.Column("name", db.String) 
    email= db.Column("email", db.String) 
    phone= db.Column("phone", db.String) 


    def __init__(self, role :str, schedule:str, name:str, email:str, phone:str ):
      self.employeeId = str(uuid4())
      self.role = EnumMemberService(EmployeeRole).getMatchValue(role)
      self.schedule = EnumMemberService(EmployeeSchedule).getMatchValue(schedule)
      self.name = name
      self.email = email
      self.phone = phone
      
    def update(self, role :str =None, schedule:str=None, name:str=None, email:str=None, phone:str=None ):
      self.role = EnumMemberService(EmployeeRole).getMatchValue(role) if role !=None else self.role
      self.schedule = EnumMemberService(EmployeeSchedule).getMatchValue(schedule) if schedule !=None else self.schedule
      self.name = name if name !=None else self.name
      self.email = email if email !=None else self.email
      self.phone = phone if phone !=None else self.phone
      
    def get_item_dict(self):
        return self.__dict__
    
    def __str__ (self):
        return f"{self.role} {self.name} {self.schedule} {self.email} {self.phon}"




