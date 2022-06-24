import json
import DBlogic
import config

articlesList = []
with open(config.filename) as data:
    for obj in data:
        articleObj = json.loads(obj)
        articlesList.append(articleObj)

del articlesList[0::2]

connection = DBlogic.connect()
DBlogic.drop(connection)
DBlogic.create_it(connection)

for article in articlesList:
    DBlogic.add_elem(connection=connection, create_timestamp=article["create_timestamp"],
                     timestamp=article['timestamp'], language=article['language'], wiki=article['wiki'],
                     category=article['category'], title=article['title'],
                     auxiliary_text=(article['auxiliary_text'] if article.get("auxiliary_text") else ""))