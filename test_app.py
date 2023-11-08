# test_app.py
import unittest
from app import app

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home_page(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        # assert that the response contains the HTML form
        self.assertIn(b'Add a New Task', result.data)

    def test_add_task(self):
        # sends HTTP POST request to the application
        # with the specified path and data
        result = self.app.post('/', data=dict(task="Test Task"), follow_redirects=True)
        
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        # assert that the response contains the new task
        self.assertIn(b'Test Task', result.data)

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
