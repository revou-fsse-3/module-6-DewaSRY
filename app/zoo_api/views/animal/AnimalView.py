from flask_smorest import Blueprint
from flask.views import MethodView

from app.zoo_api.model.AnimalModel import AnimalBaseModel
from app.zoo_api.schemas.AnimalSchemas import AnimalSchemasWithId,AnimalSchemas
from app.zoo_api.service.dbModelService.AnimalModelService import AnimalModelService



blp = Blueprint("Animal", __name__, description="Animal route ")

        
@blp.route("/animal/<string:item_id>")
class AnimalViews(MethodView):
        
    @blp.response(200, AnimalSchemasWithId)
    def get(self, item_id):
        print(item_id)
        return AnimalModelService.getDb().getDbModal(item_id)
   
   
    @blp.arguments(AnimalSchemas(partial=("name","species","gender","age")))
    @blp.response(200, AnimalSchemasWithId)
    def put(self ,item_data,item_id):
        items= AnimalModelService.getDb().updateDbModel(item_id ,item_data)
        return items
        
    def delete(self,item_id ):
        AnimalModelService.getDb().deleteDbModal(item_id)
        return {"message": "Item deleted."}

