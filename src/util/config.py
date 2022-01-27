from dotenv import dotenv_values

environment_variables = dotenv_values()

MONGO_URI = environment_variables['MONGO_URI']
