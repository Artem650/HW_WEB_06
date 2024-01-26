import psycopg2
from contextlib import contextmanager
from psycopg2 import Error


@contextmanager
def create_connection():

    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='web_dz6', user='postgres', password='15061992')
        yield conn
        conn.commit()
    except Error as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()