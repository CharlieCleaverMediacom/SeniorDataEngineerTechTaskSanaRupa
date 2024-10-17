# tests/test_api_client.py

import requests
import unittest


class TestAPIClient(unittest.TestCase):
    def test_extract_data(self):
        print("Starting API client test")
        try:
            # Extract data from API
            posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
            users_response = requests.get('https://jsonplaceholder.typicode.com/users')
            posts = posts_response.json()
            users = users_response.json()

            # Validate data
            self.assertIsInstance(posts, list, "Posts should be a list")
            self.assertIsInstance(users, list, "Users should be a list")
            self.assertGreater(len(posts), 0, "Posts should not be empty")
            self.assertGreater(len(users), 0, "Users should not be empty")

            print("API client test passed")
        except Exception as e:
            self.fail(f"API client test failed due to {str(e)}")


if __name__ == '__main__':
    unittest.main()
