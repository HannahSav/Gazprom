import json
import DBlogic
from Resourses.config import filename
import Interactive


def creating_db():
    DBlogic.drop(connection)
    DBlogic.create_it(connection)

    for article in articlesList:
        DBlogic.add_elem(connection=connection, create_timestamp=article["create_timestamp"],
                         timestamp=article['timestamp'], language=article['language'], wiki=article['wiki'],
                         category=article['category'], title=article['title'],
                         auxiliary_text=(article['auxiliary_text'] if article.get("auxiliary_text") else ""))

    print("[INFO] Fill all tables\n")


articlesList = []
with open(filename) as data:
    for obj in data:
        articleObj = json.loads(obj)
        articlesList.append(articleObj)

del articlesList[0::2]

connection = DBlogic.connect()
creating_db()

# working with console
while True:
    Interactive.ask(connection)
