import requests
import logging
import sys
import os
import pandas as pd

log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_evidence', 'etl_run_log.txt')

# Basic logging configuration
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Logging is configured and the script is starting.")
#Extract data from JSONPlaceholder API.
def extract_data(table_name):
    try:
        table_response = requests.get('https://jsonplaceholder.typicode.com/'+table_name)
        table_response.raise_for_status()
        df_table = pd.json_normalize(table_response.json())
        return df_table
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during data extraction {e} for end point {table_name}")
        sys.exit(1)

