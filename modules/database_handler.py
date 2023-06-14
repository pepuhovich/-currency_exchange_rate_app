import psycopg2
from modules.config_parser import config
from modules.output import get_color
from colorama import Style

    
def send_to_db(datetime, base_currency, endpoint_currency, rate, is_rate_higher):
    conn = None
    try:
        # Load database configuration
        database_access = config()
        conn = psycopg2.connect(**database_access)
		# Create connection cursor
        cur = conn.cursor()
        # Create table if is not created
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                    currency_query_history (
                    date_time TEXT,
                    base_currency TEXT,
                    endpoint_currency TEXT,
                    conversion_rate REAL,
                    is_rate_higher boolean)""")
        # Insert data
        cur.execute("""INSERT INTO currency_query_history
                        (date_time, base_currency, endpoint_currency, conversion_rate, is_rate_higher) 
                        VALUES (%s, %s, %s, %s, %s)""", (datetime, base_currency, endpoint_currency, rate, is_rate_higher))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

def load_from_db():
    conn = None
    try:
        # Load database configuration
        database_access = config()
        conn = psycopg2.connect(**database_access)
		# Create connection cursor
        cursor = conn.cursor()
        # Select database content
        cursor.execute("SELECT * FROM currency_query_history")
        query_history = cursor.fetchall()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
    return query_history

def print_from_db():
    query_history = load_from_db()
    # Print each output to single line
    for query in query_history:
        printing_color = get_color(query[4])
        print(query[0], query[1], query[2], printing_color, query[3], end='')
        print(Style.RESET_ALL)