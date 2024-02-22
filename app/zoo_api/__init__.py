from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate


from app.zoo_api.views.animal.AnimalsView import blp as AnimalsView
from app.zoo_api.views.animal.AnimalView import blp as AnimalView
from app.zoo_api.views.employee.EmployeesView import blp as EmployeesView
from app.zoo_api.views.employee.EmployeeView import blp as EmployeeView

from app.zoo_api.utils.FlaskDb import FlaskDb
from app.zoo_api.utils.SqlPhat import getSqlPhat

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Zoo REST API "
    app.config["API_VERSION"] = "v0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or getSqlPhat()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db= FlaskDb.getDb()
    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)
    api.register_blueprint(AnimalsView)
    api.register_blueprint(AnimalView)
    api.register_blueprint(EmployeeView)
    api.register_blueprint(EmployeesView)
    return app

