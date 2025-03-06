import unittest
from app import app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Flask App!', response.data)


if __name__ == '__main__':
    unittest.main()
