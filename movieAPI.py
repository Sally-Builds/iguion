import requests
from dotenv import load_dotenv
import os

load_dotenv()


class MovieAPI:

    def __init__(self, api_key):
        self.headers = {'Authorization': f"Bearer {api_key}", 'accept': 'application/json'}

    def getData(self):
        print(self.headers)
        r = requests.get('https://api.themoviedb.org/3/authentication', headers=self.headers)
        print(r.text)


key = my_variable = os.getenv('TMDB_API_TOKEN')
MovieAPI(key).getData()
