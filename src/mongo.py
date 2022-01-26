from pymodm.connection import connect
from config import MONGO_URI


connect(MONGO_URI, alias='app')
