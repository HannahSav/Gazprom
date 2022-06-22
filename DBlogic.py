import psycopg2
from config import host, user, password, db_name


def connect():
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        print("[INFO] Connected to the DB")
        return connection
    except Exception as e:
        print("[ERROR] Can't connect to the DB")


def create_it():
    try:
        connection = connect()
        with connection.cursor() as cur:
            cur.execute(
                """CREATE TABLE WIKI(
                create_timestamp TIMESTAMP,
                TIME_STAMP TIMESTAMP,
                lang VARCHAR[10],
                wiki VARCHAR[50],
                category VARCHAR[50],
                title VARCHAR PRIMARY KEY,
                auxiliary_text VARCHAR[50]
                );""")
            connection.commit()
            print("[INFO] Created table")
    except Exception as e:
        print("[ERROR] Couldn't create it")

def drop():
    connection = connect()
    with connection.cursor() as cur:
        cur.execute("""DROP TABLE WIKI;""")
    connection.commit()

# def add_elem(create_timestamp, timestamp, language, wiki, category, title, auxiliary_text):
