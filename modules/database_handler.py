import os
import psycopg2
from modules.config_parser import config


def create_table():
    conn = None
    try:
        database_access = config()
        conn = psycopg2.connect(**database_access)
		
        cur = conn.cursor()
        
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                    CURRENCY_QUERY_HISTORY (
                    DATE_TIME text,
                    BASE_CURRENCY text,
                    ENDPOINT_CURRENCY text,
                    CONVERSION_RATE real)""")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
    
def send_to_db():
    return