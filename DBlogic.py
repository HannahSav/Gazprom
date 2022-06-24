from datetime import datetime

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
                object_id SERIAL PRIMARY KEY,
                create_timestamp TIMESTAMP,
                timestamp TIMESTAMP,
                language TEXT,
                wiki TEXT,
                title TEXT,
                auxiliary_text TEXT
                );
                
                CREATE TABLE CONNECTING(
                object_id INTEGER,
                category_id INTEGER,
                CONSTRAINT object_id FOREIGN KEY (object_id) references WIKI(object_id),
                CONSTRAINT category_id FOREIGN KEY (category_id) references CATEGORIES(category_id)
                );
                """)
            connection.commit()
            print("[INFO] Created table")
    except Exception as e:
        print("[ERROR] Couldn't create it")
        print(e)


def drop(connection):
    try:
        with connection.cursor() as cur:
            cur.execute("""
            DROP TABLE CONNECTING;
            DROP TABLE WIKI;
            DROP TABLE CATEGORIES;""")
        connection.commit()
        print("[INFO] deleted it")
    except Exception as e:
        print("[ERROR] Couldn't delete tables")
        print(e)

def add_elem(connection, create_timestamp, timestamp, language, wiki, category, title, auxiliary_text = 0):
    try:
        with connection.cursor() as cur:
            # creating object

            sql = """INSERT INTO WIKI (create_timestamp, timestamp, language, wiki, title, auxiliary_text) VALUES (%s, %s, %s, %s, %s, %s) RETURNING object_id"""
            cur.execute(sql, (str(create_timestamp), str(timestamp), language, wiki, title, auxiliary_text))
            obj_id = cur.fetchone()[0]

            for cat in category:
                sql = """SELECT * FROM CATEGORIES WHERE category = %s"""
                cur.execute(sql, (cat,))
                connection.commit()
                row = cur.fetchone()
                cat_id = 0
                if not row:

                    #creating category

                    sql = """INSERT INTO CATEGORIES (category, num_of_titles) VALUES (%s, %s) RETURNING category_id"""
                    cur.execute(sql, (cat, int(1)))
                    cat_id = cur.fetchone()[0]
                else:

                    #updating category

                    cat_id = row[0]
                    sql = """UPDATE categories SET num_of_titles = %s WHERE category_id = %s"""
                    cur.execute(sql, (int(row[2])+1, int(row[0])))

                #creating connection

                sql = """INSERT INTO CONNECTING (category_id, object_id) VALUES (%s, %s)"""
                cur.execute(sql, (cat_id, obj_id))

    except Exception as e:
        print("[INFO] troubles with searching category", category)
        print(e)