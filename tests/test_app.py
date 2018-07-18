import unittest
from my_app.app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        data = response.get_data(as_text=True)
        self.assertEqual(data, 'Hello, World!')
