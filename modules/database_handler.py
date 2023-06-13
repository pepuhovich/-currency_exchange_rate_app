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
    
def send_to_db(datetime, base_currency, endpoint_currency, rate):
    conn = None
    try:
        database_access = config()
        conn = psycopg2.connect(**database_access)
		
        cur = conn.cursor()
        
        cur.execute("""INSERT INTO CURRENCY_QUERY_HISTORY
                        (DATE_TIME, BASE_CURRENCY, ENDPOINT_CURRENCY, CONVERSION_RATE) 
                        VALUES (%s, %s, %s, %s)""", (datetime, base_currency, endpoint_currency, rate))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()