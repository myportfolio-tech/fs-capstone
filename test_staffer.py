import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from staffer import db, create_app


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
        
        self.token1 = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkstNjZMQlNsNkRvWTV4NjBmdllNOCJ9.eyJpc3MiOiJodHRwczovL2RvYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYWQwZDg3Y2E1MDRkMDA3MGM4YWE3NCIsImF1ZCI6InN0YWZmZXIiLCJpYXQiOjE2MzA4NzEwNzYsImV4cCI6MTYzMDg3ODI3NiwiYXpwIjoiM3dFck5wdERDcFRrTTRsc3drSlU4S2llbUNmZE1la0YiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTplbXBsb3llZSIsImRlbGV0ZTpwcm9qZWN0IiwiZ2V0OmVtcGxveWVlIiwiZ2V0OnByb2plY3QiLCJwYXRjaDplbXBsb3llZSIsInBhdGNoOnByb2plY3QiLCJwb3N0OmVtcGxveWVlIiwicG9zdDpwcm9qZWN0Il19.BsuY_cFci7IpVTZrIJS1GZr9AUYDCXYngidJ2TKIYpxhHKsYIfess1iTqHMwqIabEkmtCoVfwp71kTfZVD7Ars53jzeeiZ4KbvhKtoOS6C_aHJZSVdBc1REjdHFQ-r8F90RWzq0hW2macMexwaPTRqdygkaDgpmhXj9-u9YeU54kswaAcRjgnrfW6WiGspXu3S_oetYzAHVJDuuFd-ntMEVUsG5r4QjGMO8wRgekbfHQ0TdZrI7d-EXYMjhf4G7zohIKaz7ZdHA2eliUJWi7jENxMK5PbaDamedI9PmIFN5CeBkFjoe0diVQsVDRyN5RoFMIZj7_idRXxUEBoczr9g'
        self.invalid_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkstNjZMQlNsNkRvWTV4NjBmdllNOCJ9.eyJpc3MiOiJodHRwczovL2RvYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYWQwZDg3Y2E1MDRkMDA3MGM4YWE3NCIsImF1ZCI6InN0YWZmZXIiLCJpYXQiOjE2MzA4NzEwNzYsImV4cCI6MTYzMDg3ODI3NiwiYXpwIjoiM3dFck5wdERDcFRrTTRsc3drSlU4S2llbUNmZE1la0YiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTplbXBsb3llZSIsImRlbGV0ZTpwcm9qZWN0IiwiZ2V0OmVtcGxveWVlIiwiZ2V0OnByb2plY3QiLCJwYXRjaDplbXBsb3llZSIsInBhdGNoOnByb2plY3QiLCJwb3N0OmVtcGxveWVlIiwicG9zdDpwcm9qZWN0Il19.BsuY_cFci7IpVTZrIJS1GZr9AUYDCXYngidJ2TKIYpxhHKsYIfess1iTqHMwqIabEkmtCoVfwp71kTfZVD7Ars53jzeeiZ4KbvhKtoOS6C_aHJZSVdBc1REjdHFQ-r8F90RWzq0hW2macMexwaPTRqdygkaDgpmhXj9-u9YeU54kswaAcRjgnrfW6WiGspXu3S_oetYzAHVJDuuFd-ntMEVUsG5r4QjGMO8wRgekbfHQ0TdZrI7d-EXYMjhf4G7zohIKaz7ZdHA2eliUJWi7jENxMK5PbaDamedI9PmIFN5CeBkFjoe0diVQsVDRyN5RoFMIZj7_idRXxUEBoc1111'

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




if __name__ == "__main__":
    unittest.main()