

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
class TestAnimalsViews(TestBase):
    
    def test_post_animals(self, client: FlaskClient) -> None:
        response= client.post('/animal',json=(data_mock))
        self.animalId=response.json["animalId"]
        animal_data={
            **data_mock,
            "animalId":self.animalId
        }
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json,animal_data)
        client.delete(f"/animal/{self.animalId}")
        





    
