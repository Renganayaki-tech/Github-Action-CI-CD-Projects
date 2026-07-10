import unittest

from unittest.mock import patch

from app import app


class TestEmployeeRoutes(unittest.TestCase):

    def setUp(self):

        app.config["TESTING"] = True

        self.client = app.test_client()

    @patch("app.get_all_employees")
    def test_employee_list(self, mock_get_all):

        mock_get_all.return_value = [

            {
                "id":1,
                "name":"Renganayaki",
                "department":"Python"
            },

            {
                "id":2,
                "name":"Karthik",
                "department":"DevOps"
            }

        ]

        response = self.client.get("/employees")

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b"Renganayaki",
            response.data
        )

        self.assertIn(
            b"Karthik",
            response.data
        )

        self.assertIn(
            b"Python",
            response.data
        )

        self.assertIn(
            b"DevOps",
            response.data
        )


if __name__ == "__main__":
    unittest.main()