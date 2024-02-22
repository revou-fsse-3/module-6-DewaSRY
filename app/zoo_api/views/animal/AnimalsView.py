from flask_smorest import Blueprint
from flask.views import MethodView

from app.zoo_api.model.AnimalModel import AnimalBaseModel
from app.zoo_api.schemas.AnimalSchemas import AnimalSchemasWithId,AnimalSchemas
from app.zoo_api.service.dbModelService.AnimalModelService import AnimalModelService



blp = Blueprint("Animals", __name__, description="Animal route ")

@blp.route("/animal")
class AnimalsViews(MethodView):
    
    @blp.response(200, AnimalSchemasWithId(many=True), description="halloo")
    def get(self):
        items=AnimalModelService.getDb().getDbModalAll()
        return items
    
    @blp.arguments(AnimalSchemas)
    @blp.response(201, AnimalSchemasWithId)
    def post(self ,item_data):
        items=AnimalBaseModel(**item_data)
        AnimalModelService.getDb().postDbModal(items)
        return items
 