import pymongo

client = pymongo.MongoClient("mongodb+srv://AyushBisht:ayush2001@cluster0.asbpblu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

a= {
    "name": "ayush",
    "age": 20,
    "email": "ayush@gmail.com"

}

db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(a)