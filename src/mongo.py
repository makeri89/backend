from pymodm.connection import connect
from util.config import MONGO_URI


connect(MONGO_URI, alias='app')
