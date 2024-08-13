import unittest
from app import app

class TestStatusCountEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status_count_missing_params(self):
        response = self.app.get('/status_count')
        self.assertEqual(response.status_code, 400)

    def test_status_count_invalid_time_format(self):
        response = self.app.get('/status_count?start_time=invalid&end_time=invalid')
        self.assertEqual(response.status_code, 500)

    # Add more tests for valid cases

if __name__ == "__main__":
    unittest.main()