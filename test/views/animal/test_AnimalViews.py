

from test.conftest import TestBase
from flask.testing import FlaskClient

data_mock={
    "name": "animal-test",
    "species": "Mammals",
    "gender": "Female",
    "age": 9,
}
delete_massage={
  "message": "Item deleted."
}
class TestAnimalViews(TestBase):
    
    def setUp(self, client: FlaskClient) -> None:
        response= client.post('/animal',json=(data_mock))
        self.animalId=response.json["animalId"]
        self.animal_data={
            **data_mock,
            "animalId":self.animalId
        }
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json,self.animal_data)
        

    def test_get_animal_with_id(self, client:FlaskClient):
        response = client.get(f"/animal/{self.animalId}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,self.animal_data)

    def test_update_animal_with_new_name(self, client:FlaskClient):
        newName="animal-test-new-name"
        
        response = client.put(f"/animal/{self.animalId}" , json= {
            "name":newName
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'],newName)
    
    def test_delete_animal(self, client:FlaskClient):
        response = client.delete(f"/animal/{self.animalId}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, delete_massage)
