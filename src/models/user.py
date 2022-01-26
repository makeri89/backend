from mongoengine import Document, StringField


class User(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50, unique=True)
    phone = StringField(max_length=20)
