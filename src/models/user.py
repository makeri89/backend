from pymodm import MongoModel, fields


class User(MongoModel):
    first_name = fields.CharField()
    last_name = fields.CharField()
    email = fields.CharField()
    phone = fields.CharField()

    class Meta:
        connection_alias = 'app'
        final = True

    @staticmethod
    def create(first_name, last_name, email):
        user = User(first_name, last_name, email)
        user.save()
        return user

    def to_json(self):
        return {
            'id': str(self._id) or None,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
