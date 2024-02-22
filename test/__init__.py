

import unittest


from test.views.animal.test_AnimalViews import TestAnimalViews
from test.views.animal.test_AnimalsViews import TestAnimalsViews
from test.views.employee.test_EmployeesViews import TestEmployeesViews
from test.views.employee.test_EmployeeViews import TestEmployeeViews

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite= unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAnimalViews))
    suite.addTest(unittest.makeSuite(TestAnimalsViews))
    suite.addTest(unittest.makeSuite(TestEmployeesViews))
    suite.addTest(unittest.makeSuite(TestEmployeeViews))
    runner.run(suite())
    unittest.main()