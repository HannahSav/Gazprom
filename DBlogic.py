import psycopg2
from config import host, user, password, db_name


def connect():
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        print("[INFO] Connected to the DB")
        return connection
    except Exception as e:
        print("[ERROR] Can't connect to the DB")


def create_it(connection):
    try:
        with connection.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE CATEGORIES(
                category_id SERIAL PRIMARY KEY,
                category TEXT,
                num_of_titles INTEGER
                );
                CREATE TABLE WIKI(
                create_timestamp TIMESTAMP,
                TIME_STAMP TIMESTAMP,
                lang VARCHAR[10],
                wiki TEXT,
				category_id INTEGER, 
                CONSTRAINT category_id FOREIGN KEY(category_id) REFERENCES CATEGORIES(category_id),
                title VARCHAR PRIMARY KEY,
                auxiliary_text TEXT
                );""")
            connection.commit()
            print("[INFO] Created table")
    except Exception as e:
        print("[ERROR] Couldn't create it")
        print(e)


def drop(connection):
    try:
        with connection.cursor() as cur:
            cur.execute("""DROP TABLE WIKI;
            DROP TABLE CATEGORIES;""")
        connection.commit()
        print("[INFO] deleted it")
    except Exception as e:
        print("[ERROR] Couldn't delete tables")
        print(e)

def add_elem(connection, create_timestamp, timestamp, language, wiki, category, title, auxiliary_text = 0):
    try:
        with connection.cursor() as cur:
            for cat in category:
                cur.execute("""SELECT * FROM CATEGORIES WHERE category = %s""", (cat,))
                connection.commit()
                our_category_string = cur.fetchall()
                #print(str(cat), cat)
                print("our:: ", our_category_string, "\n")
                if our_category_string == []:
                    sql = """INSERT INTO CATEGORIES (category, num_of_titles) VALUES (%s, 1)"""
                    cur.execute(sql, (cat, ))
                else:
                    cur.execute("""UPDATE categories SET num_of_titles = %d WHERE category_id = %d""", our_category_string[2]+1, our_category_string[0])
    except Exception as e:
        print("[INFO] troubles with searching category", category)
        print(e)