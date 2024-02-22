from flask_smorest import Blueprint
from flask.views import MethodView


from app.zoo_api.schemas.EmployeeSchemas import EmployeeSchemas,EmployeeSchemasWithId
from app.zoo_api.service.dbModelService.EmployeeModelService import EmployeeModelService
from app.zoo_api.model.EmployeeModel import EmployeeBaseModel

blp = Blueprint("employee",  __name__, description="employees route ")




@blp.route("/employee/<string:item_id>")
class AnimalViews(MethodView):
        
    @blp.response(200, EmployeeSchemasWithId)
    def get(self, item_id: str):
       return EmployeeModelService.getDb().getDbModal(item_id)
   
    @blp.arguments(EmployeeSchemas(partial=("name", "role", "schedule", "email","phone")))
    @blp.response(200, EmployeeSchemasWithId)
    def put(self ,item_data,item_id):
        items= EmployeeModelService.getDb().updateDbModel(item_id,item_data )
        return items
        
    def delete(self,item_id ):
        EmployeeModelService.getDb().deleteDbModal(item_id)
        return {"message": "Item deleted."}
