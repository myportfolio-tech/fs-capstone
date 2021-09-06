import unittest
import json
import random
import string
import os

from flask_sqlalchemy import SQLAlchemy
from staffer import db, create_app
from staffer.models import Employee, Project


def setup_test_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class StafferTest(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client
        self.database_name = "staffer_tester"
        self.database_path = "postgresql://{}@{}/{}".format(
            'psqladmin:administrator', 'localhost:5432', self.database_name)
        setup_test_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()
        
        self.token1 = os.environ.get('TOKEN_1')
        self.token2 = os.environ.get('TOKEN_2')
        

    def tearDown(self):
        """Executed after reach test"""
        pass

    

#Test home route basic functionality    
    def test_home_route(self):

        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get('success'), True)

#Test /employees basic functionality and data values     
    def test_get_employees(self):

        res = self.client().get('/employees')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get('success'), True)
        self.assertGreaterEqual(data.get('total'), 50)


#Test /projects basic functionality and data values        
    def test_get_all_projects(self):

        res = self.client().get('/projects')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get('success'), True)
        self.assertGreaterEqual(data.get('total'), 0)


#Get Employee with Valid Token    
    def test_get_employee(self):

        res = self.client().get('/employee/1', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.token1}')
            ])
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get('success'), True)
        self.assertGreaterEqual(data.get('id'), 1)


#Get Project with Valid Token    
    def test_get_employee(self):

        res = self.client().get('/project/1', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.token1}')
            ])
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get('success'), True)
        self.assertGreaterEqual(data.get('id'), 1)


#Get Employee with Invalid Token    
    def test_get_employee(self):

        res = self.client().get('/employee/1', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.invalid_token}')
            ])

        self.assertEqual(res.status_code, 400)


#POST Employee with valid Token    
    def test_create_employee(self):
        
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        email = (''.join(random.choice(string.ascii_letters) for i in range(10))) + 'email.com'
        
        res = self.client().post('/employee/create', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.token1}')
            ], data = json.dumps({
                "username": username,
                "email": email,
                "department": "testing"}))

        self.assertEqual(res.status_code, 200)


#POST Project with valid Token    
    def test_create_project(self):

        res = self.client().post('/project/create', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.token1}')
            ], data = json.dumps({
                "tag": random.randint(1, 32767),
                "name": 'Test Project',
                "advisor_id": random.randint(1, 50),
                "manager_id": random.randint(1, 50),
                "director_id": random.randint(1, 50)
                }))

        self.assertEqual(res.status_code, 200)



#DELETE Employee with valid Token    
    def test_delete_employee(self):

        emp = Employee.query.first()

        res = self.client().delete(f'/employee/{emp.id}/delete', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.token1}')
            ])

        self.assertEqual(res.status_code, 200)


#DELETE Project with valid Token    
    def test_delete_project(self):

        proj = Project.query.first()

        res = self.client().delete(f'/project/{proj.id}/delete', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.token1}')
            ])

        self.assertEqual(res.status_code, 200)



if __name__ == "__main__":
    unittest.main()