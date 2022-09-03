import json
from csv import DictReader


with open('books.csv') as f:
    reader = DictReader(f)
    books = [{'title': book['Title'], "author": book['Author'], "pages": book['Pages'], "genre": book['Genre']}
             for book in reader]

with open("users.json", "r") as f:
    reader = json.load(f)
    users = [{"name": user['name'], "gender": user["gender"], "address": user["address"], "age": user["age"],
              "books": []} for user in reader]

j = 0

for i in range(len(books)):
    if j == len(users):
        j = 0
    users[j]['books'].append(books[i])
    j += 1


with open("result.json", "w") as f:
    f.write(json.dumps(users, indent=4))
