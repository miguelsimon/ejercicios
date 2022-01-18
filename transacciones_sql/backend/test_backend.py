import unittest
import sqlite3

from backend.savings_backend import init_db, create_user, get_credit, set_credit, transfer

class Test(unittest.TestCase):
    def test_basic_ops(self):
        conn = sqlite3.connect(':memory:')
        init_db(conn)

        create_user(conn, 'pepe', 100)

        self.assertEqual(get_credit(conn, 'pepe'), 100)

    def test_successful_transfer(self):
        conn = sqlite3.connect(':memory:')
        init_db(conn)

        create_user(conn, 'pepe', 100)
        create_user(conn, 'paco', 100)

        transfer(conn, 'pepe', 'paco', 50)

        self.assertEqual(get_credit(conn, 'pepe'), 50)
        self.assertEqual(get_credit(conn, 'paco'), 150)

    def test_insufficient_funds_transfer(self):
        conn = sqlite3.connect(':memory:')
        init_db(conn)

        create_user(conn, 'pepe', 100)
        create_user(conn, 'paco', 100)

        with self.assertRaises(Exception):
            transfer(conn, 'pepe', 'paco', 1000)
