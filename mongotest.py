import pymongo

"""

    client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
"""

client = pymongo.MongoClient("mongodb+srv://gursim211:chhabra1714@gursimran.j9i39.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"gursimran",
    "email":"gursim211@gmail.com",
    "surname":"singh",

}
d= {
    "name":"gursimran",
    "email":"gursim211@gmail.com",
    "surname":"singh",

}
d= {
    "name":"gursimran",
    "email":"gursim211@gmail.com",
    "surname":"singh",

}
db1 =client['mongotest']
coll = db1['test']
coll.insert_one(d )