from pymodm import MongoModel, fields
from models.target import Target
from models.user import User


class Dive(MongoModel):
    diver_id = fields.ReferenceField(User)
    target_id = fields.ReferenceField(Target)
    date = fields.DateField()
    location_correct = fields.BooleanField()

    class Meta:
        connection_alias = 'app'
        final = True
