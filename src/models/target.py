from pymodm import MongoModel, fields


class Target(MongoModel):
    name = fields.CharField()
    town = fields.CharField()
    type = fields.CharField()
    x_coordinate = fields.CharField()
    y_coordinate = fields.CharField()
    location_method = fields.CharField()
    location_accuracy = fields.CharField()
    url = fields.CharField()
    date = fields.DateTimeField()

    class Meta:
        connection_alias = 'app'
        final = True

    @staticmethod
    def find_all():
        return Target.objects.all()

    @staticmethod
    def to_json():
        pass
