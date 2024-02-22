

from test.conftest import TestBase
from flask.testing import FlaskClient

data_mock={
  "role":"Manager",
  "schedule":"Morning",
  "name":"Surya",
  "email":"sdewaSurya@gmail.com",
  "phone":"this is a phone"
}
delete_massage={
  "message": "Item deleted."
}
class TestEmployeeViews(TestBase):
    
    def setUp(self, client: FlaskClient) -> None:
        response= client.post('/employee',json=(data_mock))
        self.employeeId=response.json["employeeId"]
        self.Employee_data={
            **data_mock,
            "employeeId":self.employeeId
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,self.Employee_data)
        

    def test_get_Employee_with_id(self, client:FlaskClient):
        response = client.get(f"/employee/{self.employeeId}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,self.Employee_data)
        


    def test_update_Employee_with_new_name(self, client:FlaskClient):
        newName="Employee-test-new-name"
        
        response = client.put(f"/employee/{self.employeeId}" , json= {
            "name":newName
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'],newName)
    
    def test_delete_Employee(self, client:FlaskClient):
        response = client.delete(f"/employee/{self.employeeId}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, delete_massage)
