from marshmallow import Schema, fields


class AnimalSchemas(Schema):
    """AnimalSchemas"""
    name= fields.Str()
    species=fields.Str()
    gender=fields.Str()
    age= fields.Int()
    
class AnimalSchemasWithId(AnimalSchemas):
    """animal schemas """
    animalId= fields.Str(dump_only=True)




