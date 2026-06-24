
from pymongo import MongoClient

uri = "mongodb+srv://aliaftab2106_db_user:ali1234@cluster0.msp2bj4.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)