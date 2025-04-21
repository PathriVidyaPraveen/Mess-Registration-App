from pymongo import MongoClient

client = MongoClient("mongodb+srv://dinesh_23:tc97386@cluster0.7a7ovpk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mess"]
collection_admin = db["admins"]

data_admin = [
    {
    "name" : "Aditya Kumar",
    "mess" : "MESS-A",
    "position": "Admin",
    "email" : "aditya@cse.iith.ac.in",
    "passwd": "aditya95"
},
{
    "name": "Saurabh",
    "mess": "MESS-B",
    "position": "Admin",
    "email" : "saurabh@ph.iith.ac.in",
    "passwd": "saurabhep06"
}
]

collection_admin.insert_many(data_admin)
print("Inserted admin data into database")