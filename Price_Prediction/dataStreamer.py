import pymongo
from pymongo import MongoClient 

cluster  = MongoClient("mongodb+srv://reinis:ulOiNRHPXyH8WslY@cluster0.6zzdz.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Cluster0"]

collection = db["Cluster0"]


