import requests
from urllib.parse import quote
from config.constants import API_KEY, TMDB_BASE_URL, TMDB_IMAGE_BASE_URL


class MovieAPI:

    def __init__(self):
        self.headers = {'Authorization': f"Bearer {API_KEY}", 'accept': 'application/json'}

    def ping(self):
        r = requests.get(f'{TMDB_BASE_URL}/authentication', headers=self.headers)
        print(r.text)

    def search(self, movie_type, search_term):
        print(movie_type, search_term)
        params = {
            "query": search_term,
            "include_adult": "false",
            "language": "en-US",
            "page": 1
        }
        endpoint = '/tv' if movie_type == 'TV Show' else '/movie'
        url = f"https://api.themoviedb.org/3/search/{endpoint}"

        try:
            res = requests.get(url, headers=self.headers, params=params)
            movies = res.json()["results"]
            movies = [
                {"movie_id": movie["id"], "movie_name": movie["original_name"],
                 "movie_img": f'{TMDB_IMAGE_BASE_URL}{movie["poster_path"]}',
                 "movie_overview": movie["overview"]} for movie in movies]

            return {"status": True, "results": movies}
        except requests.exceptions.RequestException as e:
            # log exception
            print(e)
            return {"status": False, "results": None}

        except Exception as e:
            print(e, 'err')
            return {"status": False, "results": None}

    def movie_credits(self, movie_type, movie_id):
        params = {
            "language": "en-US",
        }
        endpoint = 'tv' if movie_type == 'TV Show' else 'movie'
        url = f"https://api.themoviedb.org/3/{endpoint}/{movie_id}/aggregate_credits"

        try:
            res = requests.get(url, headers=self.headers, params=params)
            print(res.json())
            casts = res.json()["cast"]
            casts = [{"person_id": cast["id"], "character_image": f'{TMDB_IMAGE_BASE_URL}{cast["profile_path"]}',
                      "character_name":
                          role["character"], "credit_id": role["credit_id"]} for cast in casts for role in
                     cast["roles"]]

            return {"status": True, "results": casts}
        except requests.exceptions.RequestException as e:
            # log exception
            print(e)
            return {"status": False, "results": None}

    def does_movie_exist(self, movie_type, movie_id):
        params = {
            "language": "en-US",
        }
        endpoint = 'tv' if movie_type == 'TV Show' else 'movie'
        url = f"https://api.themoviedb.org/3/{endpoint}/{movie_id}"

        try:
            res = requests.get(url, headers=self.headers, params=params)
            movie = res.json()["id"]

            if movie:
                return True

            return False
        except requests.exceptions.RequestException as e:
            print(e)
            return False

    def get_movie_name(self, movie_type, movie_id):
        params = {
            "language": "en-US",
        }
        endpoint = 'tv' if movie_type == 'TV Show' else 'movie'
        url = f"https://api.themoviedb.org/3/{endpoint}/{movie_id}"

        try:
            res = requests.get(url, headers=self.headers, params=params)
            movie = res.json()["name"]

            if movie:
                return movie

            return "Invalid Movie"
        except requests.exceptions.RequestException as e:
            print(e)
            return 'Invalid Movie'

    def get_character_name(self, character_id):
        params = {
            "language": "en-US",
        }
        url = f"https://api.themoviedb.org/3/credit/{character_id}"

        try:
            res = requests.get(url, headers=self.headers, params=params)
            print(res.json(), '----------------------------------------------')
            if res.status_code >= 300:
                return "Unknown Character"
            movie = res.json()["media"]

            if movie:
                return movie["character"]

            return "Unknown Character"
        except requests.exceptions.RequestException as e:
            print(e)
            return "Invalid Movie"
# [ {"person_id": cast["id"], "character_image": cast["profile_path"], "character_name" role["character"], "credit_id": role["credit_id"]} for role in roles for cast in casts]

# {
#     "adult": false,
#     "gender": 2,
#     "id": 17419,
#     "known_for_department": "Acting",
#     "name": "Bryan Cranston",
#     "original_name": "Bryan Cranston",
#     "popularity": 33.197,
#     "profile_path": "/kNyTXGkiSP8W4Gs60hF7UoxZnWN.jpg",
#     "roles": [
#       {
#         "credit_id": "52542282760ee313280017f9",
#         "character": "Walter White",
#         "episode_count": 65
#       }
#     ],
#     "total_episode_count": 65,
#     "order": 0
#   },
#   {
#     "adult": false,
#     "gender": 2,
#     "id": 84497,
#     "known_for_department": "Acting",
#     "name": "Aaron Paul",
#     "original_name": "Aaron Paul",
#     "popularity": 22.42,
#     "profile_path": "/8Ac9uuoYwZoYVAIJfRLzzLsGGJn.jpg",
#     "roles": [
#       {
#         "credit_id": "52542282760ee31328001845",
#         "character": "Jesse Pinkman",
#         "episode_count": 64
#       }
#     ],
#     "total_episode_count": 64,
#     "order": 1
#   },
#   ]
