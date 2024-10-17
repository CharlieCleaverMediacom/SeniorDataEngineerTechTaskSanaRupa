import sqlite3
import logging
import sys

import pandas as pd


def load_data(dfs, db_name='etl_challenge.db'):
    try:
        logging.info("Starting data loading.")
        conn = sqlite3.connect(db_name)
        # Insert data into enriched_posts table
        if 'enriched_post_df' in dfs and len(dfs['enriched_post_df']) > 0:
            enriched_post_df=pd.DataFrame(dfs['enriched_post_df']).drop_duplicates()
            enriched_post_df.to_sql('srk_enriched_posts', conn, if_exists='replace', index=False)

        # Insert data into users table
        if 'users' in dfs and len(dfs['users'])>0:
            users_df = pd.DataFrame(dfs['users']).drop_duplicates()
            users_df.to_sql('srk_users', conn, if_exists='replace', index=False)

        # Insert data into posts table
        if 'posts' in dfs and len(dfs['posts']) > 0:
            posts_df = pd.DataFrame(dfs['posts']).drop_duplicates()
            posts_df.to_sql('srk_posts', conn, if_exists='replace', index=False)

        conn.commit()
        conn.close()
        logging.info("Data loading completed successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error during data loading: {e}")
        sys.exit(1)