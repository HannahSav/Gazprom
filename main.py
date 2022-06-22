import json
import DBlogic

articlesList = []
with open("data.json") as data:
    for obj in data:
        articleObj = json.loads(obj)
        articlesList.append(articleObj)

#убираем ненужные объекты из json
del articlesList[0::2]

for article in articlesList:
    print(article["title"])

DBlogic.create_it()
#DBlogic.drop()