import unittest
from app import app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee", response.data)

    def test_employee_page(self):
        response = self.client.get("/employees")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()