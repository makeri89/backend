from pymodm import MongoModel, fields
from models.target import Target
from models.user import User


class Dive(MongoModel):
    diver = fields.ReferenceField(User)
    target = fields.ReferenceField(Target)
    created_at = fields.DateTimeField()
    location_correct = fields.BooleanField()

    class Meta:
        connection_alias = 'app'
        final = True

    @staticmethod
    def create(diver, target, location_correct, created_at):
        dive = Dive(diver, target, created_at, location_correct)
        dive.save()
        return dive

    def to_json(self):
        return {
            'id': str(self._id) or None,
            'diver': self.diver.to_json(),
            'target': self.target.to_json(),
            'location_correct': self.location_correct,
            'created_at': str(self.created_at)
        }
