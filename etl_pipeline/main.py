# This is the main script where you will orchestrate the ETL process, feel free to completely modify the files/structure as you see fit.

import api_client
import transform_data
import load_to_database
import logging

if __name__ == "__main__":
    print("ETL Job Started")

    dfs={}

    # I see more end_points for same api. We can add more end_points to list, in future if we needed to extract more data.
    end_points=['users','posts']

    # Extract phase
    # TODO: Implement data extraction logic
    logging.info("Starting data extraction.")
    for end_point in end_points:
        df = api_client.extract_data(end_point)
        dfs[end_point]=df
    logging.info("Data extraction completed successfully.")

    # Transform phase
    # TODO: Implement data transformation logic
    enriched_posts_df = transform_data.transform_data(dfs)
    dfs['enriched_post_df'] = enriched_posts_df

    # Load phase
    # TODO: Implement data loading logic
    load_to_database.load_data(dfs)
    print("ETL Job Finished")