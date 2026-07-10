import unittest
from unittest.mock import patch
from database import get_employee_by_id


class TestMockDatabase(unittest.TestCase):

    @patch("database.get_connection")
    def test_mock_connection(self, mock_connection):

        mock_connection.return_value = None

        self.assertIsNone(mock_connection.return_value)


if __name__ == "__main__":
    unittest.main()