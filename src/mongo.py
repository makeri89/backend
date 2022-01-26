from mongoengine import connect
from config import MONGO_URI


connect(host=MONGO_URI)
