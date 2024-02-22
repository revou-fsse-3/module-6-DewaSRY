

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
class TestEmployeesViews(TestBase):
  

    def test_post_employees(self, client: FlaskClient) -> None:
        response= client.post('/employee',json=(data_mock))
        self.employeeId=response.json["employeeId"]
        employee_data={
            **data_mock,
            "employeeId":self.employeeId
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,employee_data)
        client.delete(f"/employee/{self.employeeId}")
        
        



    
