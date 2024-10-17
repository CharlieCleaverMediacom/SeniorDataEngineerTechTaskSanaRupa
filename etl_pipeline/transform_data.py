import logging
import sys
import pandas as pd

def transform_data(dfs):
    #Transform the extracted data.

    try:
        logging.info("Starting data transformation.")
        # Convert to DataFrame
        posts_df = pd.DataFrame(dfs['posts'])
        users_df = pd.DataFrame(dfs['users'])

        # Add 'status' field
        posts_df['status'] = posts_df['body'].apply(lambda x: 'lengthy' if len(x) > 150 else 'concise')

        # Merge posts with user details
        enriched_posts_df = posts_df.merge(users_df, how='left', left_on='userId', right_on='id', suffixes=('_post', '_user'))

        logging.info("Data transformation completed successfully.")
        return enriched_posts_df
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        sys.exit(1)