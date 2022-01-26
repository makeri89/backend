from mongoengine import *


class Target(Document):
    id = StringField()
    town = StringField()
    name = StringField()
    type = StringField()
    x_coordinate = StringField()
    y_coordinate = StringField()
    location_method = StringField()
    location_accuracy = StringField()
    url = StringField()
    created_at = DateField()
