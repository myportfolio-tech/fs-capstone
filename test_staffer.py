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



if __name__ == "__main__":
    unittest.main()