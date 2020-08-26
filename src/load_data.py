from src.csv_parser import CSVParser
import logging
from src.config import cfg
import src.logger
from itertools import islice
from src.db import Database
import os
import json
from typing import List
from psycopg2.extras import execute_values
import psycopg2

def insert_to_db(rows):  

  cursor = Database.database_connection.cursor()
  tupled_rows = generate_tuple(rows)
  insert_sql= """
  INSERT INTO covid_data_schema.raw_data 
    (
      data
    ) 
    values %s
    """
  execute_values(cursor, insert_sql, tupled_rows, page_size=10000,)
  pass

def generate_tuple(rows):
    # NOTE: Format data into list of tuples for insert query
    query_tpl = []
    for i in range(0, len(rows)):
        tpl = (json.dumps(rows[i]),)
        query_tpl.append(tpl)

    return query_tpl

def load_csv_data():
  Database.create_db_connection()
  try:
    logging.info("Extracting data from data source")
    src_file_path = os.path.join("src", cfg["datasource"]["filename"])
    path_check = os.path.exists(src_file_path)
    csv_rows = CSVParser.parse_csv_from_file(src_file_path)

    batch_size = 1000

    logging.info("Inserting values to database")
    while(True):
      rows = list(islice(csv_rows, 0, batch_size))
      insert_to_db(rows)

      if(len(rows) <= 0):
        break
    
    logging.info("Committing DB Actions")
    Database.commit_db_actions()
    logging.info("Done")
  except Exception as e:
    Database.rollback_db_actions()
    Database.close_db_connection()
    raise e

if(__name__ == "__main__"):
  load_csv_data()
  pass