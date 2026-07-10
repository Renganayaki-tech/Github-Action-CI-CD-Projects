import unittest
import mysql.connector

from database import (
    add_employee,
    get_employee_by_id,
    get_connection
)


class TestDatabase(unittest.TestCase):

    def setUp(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE id=1001"
        )

        conn.commit()

        cursor.close()
        conn.close()

    def test_add_employee(self):

        add_employee(
            1001,
            "Renganayaki",
            "Python"
        )

        employee = get_employee_by_id(1001)

        self.assertIsNotNone(employee)

        self.assertEqual(employee["name"], "Renganayaki")

        self.assertEqual(employee["department"], "Python")


if __name__ == "__main__":
    unittest.main()