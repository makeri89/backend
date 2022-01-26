import email
from mongoengine import *
from config import MONGO_URI

from models.user import User


connect(host=MONGO_URI)
    
user = User(
    first_name = 'test',
    last_name = 'tester',
    email = 'test@example.com',
    phone = '0501234567'
)

user.save()

print(user.id)