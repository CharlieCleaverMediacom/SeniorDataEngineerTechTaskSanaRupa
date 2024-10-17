## Sequence of tasks
    
- Extracts user and post data from JSONPlaceholder API.
- Transforms data to add a `status` field based on post length.
- Merges post data with user details.
- Loads transformed data into SQLite database.
- SQL queries for analyzing the data.

# Evidence
- Databases were created with name in etl_challenge.db as shown in the evidence screenshot.
- etl_run_log.txt in evidence folder will generate the log for the etl_pipeline scripts.
- run sql_results.py file to get the results.
- several screenshots were added for evidence folder.

# Database

- Can delete the etl_challenge.db, etl_challenge_Test.db files
- Run the main.py which will create etl_challenge.db with the tables.
- Run test_load_to_bigquery to create the etl_challenge_Test.db

# Extra

- Have added the sql_results.py file to see the sql query results once the etl_challenge.db is generated.
- main file was included with list option for api_client, if new end_point needs to be added/extracted we can add to the list.

# Enhancement

- Can make the code dynamic and have all the end_points data gets extracted and transformed before inserting into db.
- Can use multi processing if the data transforming is going to take time when we will have huge data dataset.
- Multiprocessing can be done for enriched posts dataframe grouping based on userId.
- Can use big query connections instead of sqlite once I have details about GCP project and access.
