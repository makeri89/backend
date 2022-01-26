from dotenv import dotenv_values

config = dotenv_values()

MONGO_URI = config['MONGO_URI']