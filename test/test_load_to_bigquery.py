# Put your unit tests here

import unittest
import sqlite3
from etl_pipeline.load_to_database import load_data


class TestLoadToDatabase(unittest.TestCase):
    def setUp(self):
        # Use an in-memory SQLite database for testing
        self.db_name = "etl_challenge_Test.db"  # Use in-memory for faster tests
        self.dfs = {
            'enriched_post_df': [
                {
                    'id': 1,
                    'user_id': 1,
                    'title': 'Test Post 1',
                    'body': 'This is a test post body.',
                    'status': 'concise',
                    'user_name': 'Sana',
                    'user_username': 'SanaRupa',
                    'user_email': 'sana@example.com',
                    'user_address': '{"street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough", "zipcode": "92998-3874", "geo": {"lat": "-37.3159", "lng": "81.1496"}}',
                    'user_phone': '1-770-736-8031 x56442',
                    'user_website': 'sanatest.org',
                    'user_company': '{"name": "Romaguera-Crona", "catchPhrase": "Multi-layered client-server neural-net", "bs": "harness real-time e-markets"}'
                },
                {
                    'id': 2,
                    'user_id': 2,
                    'title': 'Test Post 2',
                    'body': 'B' * 200,
                    'status': 'lengthy',
                    'user_name': 'Suresh',
                    'user_username': 'Sureshnaga',
                    'user_email': 'Sureshnaga@example.com',
                    'user_address': '{"street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough", "zipcode": "92998-3874", "geo": {"lat": "-37.3159", "lng": "81.1496"}}',
                    'user_phone': '1-770-736-8031 x56442',
                    'user_website': 'sureshnaga.org',
                    'user_company': '{"name": "Romaguera-Crona", "catchPhrase": "Multi-layered client-server neural-net", "bs": "harness real-time e-markets"}'
                }
            ]
        }

    def test_load_data_creates_table(self):
        load_data(self.dfs, db_name=self.db_name)

        # create connection to check if table exists
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='srk_enriched_posts';""")
        table = cursor.fetchone()
        self.assertIsNotNone(table)
        self.assertEqual(table[0], 'srk_enriched_posts')
        conn.close()

    def test_load_data_inserts_records(self):
        load_data(self.dfs, db_name=self.db_name)

        # Connect conenction to verify the inserted records
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM srk_enriched_posts;")
        count = cursor.fetchone()[0]
        self.assertEqual(count, 2)

        conn.close()

if __name__ == '__main__':
    unittest.main()
