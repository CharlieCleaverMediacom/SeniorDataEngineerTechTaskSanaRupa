# Put your unit tests here

import unittest
import pandas as pd

from etl_pipeline.transform_data import transform_data  # Adjust the import as needed


class TestTransformData(unittest.TestCase):

    def test_transform_data_basic(self):
        """Test the transformation of posts with valid user data."""
        # Sample user data
        users = [
            {"id": 1, "name": "Sana"},
            {"id": 2, "name": "Suresh"}
        ]

        # Sample posts data
        posts = [
            {"userId": 1, "id": 1, "title": "Post 1", "body": "Short body."},
            {"userId": 1, "id": 2, "title": "Post 2", "body": "A longer body that exceeds 150 characters. " * 30}
        ]

        dfs = {'posts': posts, 'users': users}
        result_df = transform_data(dfs)

        # Check the number of rows in the result DataFrame
        self.assertEqual(result_df.shape[0], 2)

        # Check the status of the first post
        self.assertEqual(result_df.loc[0, 'status'], 'concise')
        # Check the status of the second post
        self.assertEqual(result_df.loc[1, 'status'], 'lengthy')

        # Check user details for the first post
        self.assertEqual(result_df.loc[0, 'name'], 'Sana')

    def test_transform_data_missing_user(self):
        # Test transformation with a post that references a non-existing user.
        users = [{"id": 1, "name": "Sana"}]
        posts = [
            {"userId": 1, "id": 1, "title": "Post 1", "body": "Short body."},
            {"userId": 2, "id": 2, "title": "Post 2", "body": "Another body."}
        ]

        dfs = {'posts': posts, 'users': users}
        result_df = transform_data(dfs)

        # Check the number of rows in the result DataFrame
        self.assertEqual(result_df.shape[0], 2)
        # Check user details for the second post
        self.assertTrue(pd.isna(result_df.loc[1, 'name']))

    def test_transform_data_empty_input(self):
        """Test transformation with empty input data."""
        # Create empty DataFrames for posts and users
        empty_posts_df = pd.DataFrame(columns=["userId", "id", "title", "body"])
        empty_users_df = pd.DataFrame(columns=["id", "name"])

        dfs = {'posts': empty_posts_df, 'users': empty_users_df}  # No posts and no users
        result_df = transform_data(dfs)

        # Check if the result DataFrame is empty
        self.assertEqual(result_df.shape[0], 0)


if __name__ == '__main__':
    unittest.main()
