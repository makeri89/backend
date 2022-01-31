import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    print(os.getenv('MONGO_URI'))