"""model type """
from typing import  TypeVar

from app.zoo_api.utils.FlaskDb import FlaskDb

"""test"""
ModelType= TypeVar("ModelType", bound= FlaskDb.getDb().Model)