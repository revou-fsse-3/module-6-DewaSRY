import flask_unittest
from app.zoo_api import create_app


class TestBase(flask_unittest.ClientTestCase):
      app = create_app()
      app.config["TESTING"]= True
   
