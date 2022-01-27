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
        User(first_name, last_name, email).save()
