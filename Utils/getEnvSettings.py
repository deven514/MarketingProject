import os
from dotenv import load_dotenv




def getEnvironmentVariable(keyToGet):
        load_dotenv()
        return os.environ.get((keyToGet))










