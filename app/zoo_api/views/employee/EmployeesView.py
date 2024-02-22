from flask_smorest import Blueprint
from flask.views import MethodView


from app.zoo_api.schemas.EmployeeSchemas import EmployeeSchemas,EmployeeSchemasWithId
from app.zoo_api.service.dbModelService.EmployeeModelService import EmployeeModelService
from app.zoo_api.model.EmployeeModel import EmployeeBaseModel

blp = Blueprint("employees",  __name__, description="employees route ")


@blp.route("/employee")
class EmployeesViews(MethodView):
    
    @blp.response(200, EmployeeSchemasWithId(many=True))
    def get(self):
        return EmployeeModelService.getDb().getDbModalAll()
    
    @blp.arguments(EmployeeSchemas)
    @blp.response(200, EmployeeSchemasWithId)
    def post(self ,  item_data):
        items=EmployeeBaseModel(**item_data)
        EmployeeModelService.getDb().postDbModal(items)
        return items
        


