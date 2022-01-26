from mongoengine import *
from datetime import datetime

from models.target import Target
from models.user import User


class Dive(Document):
    diver_id = ReferenceField(User)
    target_id = ReferenceField(Target)
    date = DateTimeField(default=datetime.now())
    location_correct = BooleanField()