import psycopg2
from psycopg2.extensions import quote_ident
import io
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from typing import List
import logging
import itertools
from src.config import cfg

# A way for you to create a DB connection using pyscopg2. You can use the code below to create seprate connections or use connection for your whole project

class Database:
    # NOTE: Use this class if you want to utlize one connection for your entire process
    db_usr = cfg["databases"]["registry"]["user"]
    db_pwd = cfg["databases"]["registry"]["password"]
    db_hst = cfg["databases"]["registry"]["host"]
    db_prt = cfg["databases"]["registry"]["port"]
    db_sch = cfg["databases"]["registry"]["database"]
    database_connection = None

    @classmethod
    def create_db_connection(cls):
        cls.database_connection = psycopg2.connect(
            user=cls.db_usr,
            password=cls.db_pwd,
            host=cls.db_hst,
            port=cls.db_prt,
            database=cls.db_sch,
        )

    @classmethod
    def commit_db_actions(cls):
        cls.database_connection.commit()

    @classmethod
    def close_db_connection(cls):
        cls.database_connection.close()

    @classmethod
    def rollback_db_actions(cls):
        cls.database_connection.rollback()

    @classmethod
    def return_select_rows(cls, sql_statement, arg_vals=None):
        try:
            if arg_vals is not None and arg_vals != "":
                cursor = cls.database_connection.cursor()
                cursor.execute(sql_statement, (arg_vals,))
                return cursor
            else:
                cursor = cls.database_connection.cursor()
                cursor.execute(sql_statement)
                return cursor
        except Exception as e:
            raise e

    @classmethod
    def get_cursor_as_dictionary(cls, sql_statement, arg_vals=None):
        if arg_vals is not None and arg_vals != "":
            cursor = cls.database_connection.cursor(
                "my-cursor", cursor_factory=psycopg2.extras.DictCursor
            )
            cursor.execute(sql_statement, (arg_vals,))
            return cursor
        else:
            cursor = cls.database_connection.cursor(
                "my-cursor", cursor_factory=psycopg2.extras.DictCursor
            )
            cursor.execute(sql_statement)
            return cursor
