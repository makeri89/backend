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
    def find_all():
        return User.objects.all()

    @staticmethod
    def to_json():
        users = User.find_all()
        result = []
        for user in users:
            result.append(
                {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                }
            )
        return result

    @staticmethod
    def create(first_name, last_name, email):
        User(first_name, last_name, email).save()
