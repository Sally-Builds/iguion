import requests
from dotenv import load_dotenv
from config.constants import TMDB_API_TOKEN, TMDB_IMAGE_BASE_URL


class MovieAPI:

    def __init__(self):
        self.headers = {'Authorization': f"Bearer {TMDB_API_TOKEN}", 'accept': 'application/json'}

    @classmethod
    def __image_path__(cls, url):
        if isinstance(url, str):
            return TMDB_IMAGE_BASE_URL + url

        return None

    def get_data(self):
        r = requests.get('https://api.themoviedb.org/3/authentication', headers=self.headers)

    def search(self, movie_type, keyword):
        url = (f"https://api.themoviedb.org/3/search/{movie_type}?query={keyword}&include_adult=false&language=en-US"
               f"&page=1")
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return {
                "movies": [
                    {'movie_id': movie['id'],
                     'movie_name': movie['title'] if movie_type == 'movie' else movie['name'],
                     'movie_image': self.__image_path__(movie['poster_path'])}
                    for movie in response.json()["results"]]
            }
        return {"movies": []}

    def get_casts(self, movie_type, movie_id):
        url = f"https://api.themoviedb.org/3/{movie_type}/{movie_id}/aggregate_credits?language=en-US" \
            if movie_type == 'tv' else f'https://api.themoviedb.org/3/{movie_type}/{movie_id}/credits?language=en-US'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            if movie_type == 'tv':
                return {
                    "casts": [
                        {'cast_image': self.__image_path__(cast['profile_path']), 'cast_name': role['character'],
                         'cast_id': role['credit_id']}
                        for cast in response.json()['cast'] for role in cast['roles']]
                }
            else:
                return {
                    "casts": [
                        {'cast_image': self.__image_path__(cast['profile_path']), 'cast_name': cast['character'],
                         'cast_id': cast['credit_id']}
                        for cast in response.json()['cast']]
                }
        return {'casts': []}

    def movie_exist(self, movie_type, movie_id):
        url = f"https://api.themoviedb.org/3/{movie_type}/{movie_id}?language=en-US"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return True

        return False

    def cast_exist_for_movie(self, movie_type, movie_id, cast_id):
        casts = self.get_casts(movie_type, movie_id)['casts']

        for cast in casts:
            if cast['cast_id'] == cast_id:
                return True

        return False

    def get_movie(self, movie_type, movie_id):
        url = f"https://api.themoviedb.org/3/{movie_type}/{movie_id}?language=en-US"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return {'movie_name': response.json()['original_title']} if movie_type == 'movie' else {'movie_name': response.json()['name']}

        return {'movie_name': None}

    def get_cast(self, cast_id):
        url = f"https://api.themoviedb.org/3/credit/{cast_id}"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return {'cast_name': response.json()['media']['character']}

        return {'cast_name': None}

    def movie_images(self, movie_type, movie_id):
        url = f"https://api.themoviedb.org/3/{movie_type}/{movie_id}/images"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return {'images': [self.__image_path__(image['file_path']) for image in response.json()['backdrops'][:10]]}

        return {'images': []}
