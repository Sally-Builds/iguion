from dotenv import load_dotenv
import os

load_dotenv()


TMDB_API_TOKEN = os.getenv('TMDB_API_TOKEN')
TMDB_IMAGE_BASE_URL = os.getenv('TMDB_IMAGE_BASE_URL')
